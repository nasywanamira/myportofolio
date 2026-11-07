from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from main.models import Education


class EducationAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner = User.objects.create_superuser('edu-owner', password='test-password')
        cls.visitor = User.objects.create_user('edu-visitor', password='test-password')
        cls.editor = User.objects.create_user('edu-editor', password='test-password')
        cls.editor.groups.add(Group.objects.create(name='Editor'))
        cls.education = Education.objects.create(
            school='Universitas Indonesia', degree='Sistem Informasi', start_year='2025',
            description='Belajar pengembangan aplikasi.',
        )

    def setUp(self):
        self.list_url = reverse('api:education-list')
        self.detail_url = reverse('api:education-detail', args=[self.education.pk])
        self.star_url = reverse('api:education-star', args=[self.education.pk])
        self.payload = {
            'school': 'Sekolah Baru', 'degree': 'Sains', 'start_year': '2020',
            'end_year': '', 'description': 'Kegiatan sekolah.', 'logo': '',
        }

    def test_public_read_search_and_empty(self):
        self.assertEqual(self.client.get(self.list_url).status_code, 200)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data['is_starred'])
        self.assertEqual(set(response.data), {
            'id', 'school', 'degree', 'start_year', 'end_year', 'description', 'logo',
            'star_count', 'is_starred', 'starred_by_names',
        })
        self.assertEqual(len(self.client.get(self.list_url, {'school': 'INDONESIA'}).data), 1)
        self.assertEqual(self.client.get(self.list_url, {'school': 'not-found'}).data, [])

    def test_guest_and_visitor_writes_rejected_without_changes(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            with self.subTest(user=user):
                self.assertEqual(self.client.post(self.list_url, self.payload, format='json').status_code, 403)
                for method in ('put', 'patch'):
                    response = getattr(self.client, method)(self.detail_url, self.payload, format='json')
                    self.assertEqual(response.status_code, 403)
                self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
                self.education.refresh_from_db()
                self.assertEqual(self.education.school, 'Universitas Indonesia')
                self.assertEqual(Education.objects.count(), 1)

    def test_editor_patch_and_put(self):
        self.client.force_authenticate(self.editor)
        self.assertEqual(self.client.patch(self.detail_url, {'school': 'Nama Baru'}, format='json').status_code, 200)
        self.education.refresh_from_db()
        self.assertEqual(self.education.school, 'Nama Baru')
        self.assertEqual(self.education.degree, 'Sistem Informasi')
        self.assertEqual(self.client.put(self.detail_url, self.payload, format='json').status_code, 200)
        self.education.refresh_from_db()
        self.assertEqual(self.education.degree, 'Sains')

    def test_editor_create_delete_rejected_without_changes(self):
        self.client.force_authenticate(self.editor)
        self.assertEqual(self.client.post(self.list_url, self.payload, format='json').status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.education.refresh_from_db()
        self.assertEqual(self.education.school, 'Universitas Indonesia')
        self.assertEqual(Education.objects.count(), 1)

    def test_owner_crud_and_missing(self):
        self.client.force_authenticate(self.owner)
        response = self.client.post(self.list_url, self.payload, format='json')
        self.assertEqual(response.status_code, 201)
        url = reverse('api:education-detail', args=[response.data['id']])
        self.assertTrue(Education.objects.filter(pk=response.data['id']).exists())
        self.assertEqual(self.client.patch(url, {'degree': 'Baru'}, format='json').status_code, 200)
        self.assertEqual(self.client.put(url, self.payload, format='json').status_code, 200)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b'')
        self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(Education.objects.count(), 1)

    def test_validation_and_cleaning(self):
        self.client.force_authenticate(self.owner)
        for field, value in [
            ('school', '   '), ('degree', '<b></b>'), ('start_year', '<i></i>'),
            ('description', '<script></script>'), ('logo', 'javascript:alert(1)'),
            ('logo', '//evil.example/a.png'),
        ]:
            with self.subTest(field=field, value=value):
                response = self.client.post(self.list_url, {**self.payload, field: value}, format='json')
                self.assertEqual(response.status_code, 400)
                self.assertIn(field, response.data)
        self.assertEqual(Education.objects.count(), 1)
        response = self.client.post(self.list_url, {
            **self.payload, 'school': '<b>Sekolah</b>', 'logo': '/static/img/makara.png',
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['school'], 'Sekolah')
        self.assertEqual(self.client.put(self.detail_url, {'school': 'Incomplete'}, format='json').status_code, 400)
        self.education.refresh_from_db()
        self.assertEqual(self.education.school, 'Universitas Indonesia')

    def test_star_uses_logged_in_account(self):
        self.assertEqual(self.client.post(self.star_url).status_code, 403)
        self.assertEqual(self.education.starred_by.count(), 0)
        for user in (self.visitor, self.editor, self.owner):
            self.client.force_authenticate(user)
            response = self.client.post(self.star_url, {'user': self.owner.pk}, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['is_starred'])
            self.assertEqual(response.data['star_count'], 1)
            self.assertEqual(list(self.education.starred_by.all()), [user])
            self.assertFalse(self.client.post(self.star_url).data['is_starred'])
            self.assertEqual(self.education.starred_by.count(), 0)

    def test_computed_fields_read_only(self):
        self.client.force_authenticate(self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, 'id': self.education.pk, 'star_count': 99,
            'is_starred': True, 'starred_by_names': 'forged', 'starred_by': [self.visitor.pk],
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data['id'], self.education.pk)
        self.assertEqual(response.data['star_count'], 0)
        self.assertFalse(response.data['is_starred'])
        self.assertEqual(response.data['starred_by_names'], '')

    def test_wrong_method(self):
        self.client.force_authenticate(self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, 405)
        self.assertEqual(self.client.get(self.star_url).status_code, 405)

    def test_session_without_csrf_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username='edu-owner', password='test-password'))
        response = client.post(self.list_url, self.payload, format='json')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Education.objects.count(), 1)

    def test_session_with_csrf_and_editor_star(self):
        client = APIClient(enforce_csrf_checks=True)
        for user in (self.visitor, self.editor):
            self.assertTrue(client.login(username=user.username, password='test-password'))
            page = client.get(reverse('main:show_education'))
            self.assertEqual(page.status_code, 200)
            token = client.cookies['csrftoken'].value
            response = client.post(self.star_url, HTTP_X_CSRFTOKEN=token)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['is_starred'])
            client.logout()

    def test_legacy_editor_access(self):
        self.client.force_login(self.editor)
        url = reverse('main:edit_education', args=[self.education.pk])
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.post(url, self.payload).status_code, 302)
        self.education.refresh_from_db()
        self.assertEqual(self.education.school, 'Sekolah Baru')
        self.assertEqual(self.client.post(reverse('main:create_education'), self.payload).status_code, 403)
        self.assertEqual(self.client.post(reverse('main:delete_education', args=[self.education.pk])).status_code, 403)
        self.assertTrue(Education.objects.filter(pk=self.education.pk).exists())