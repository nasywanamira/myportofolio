from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Project, Education
from main.permissions import IsPortfolioOwnerOrReadOnly, IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ProjectSerializer, EducationSerializer


@api_view(["GET", "HEAD", "POST"]) # membungkus fungsi menjadi API view DRF: ia menyediakan Request, renderer untuk Response, penanganan exception API, dan penolakan method yang tidak didaftarkan.
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
# menentukan cara mengenali akun serta aturan akses. Tulis dekorator dalam urutan yang ditunjukkan.
def project_list(request):
    if request.method in ("GET", "HEAD"):
        projects = Project.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            projects = projects.filter(title__icontains=title)
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = ProjectSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# request.query_params membaca parameter pencarian. title__icontains tetap memakai pola pencarian Django yang sudah kamu kenal. order_by membuat urutan hasil konsisten.
# prefetch_related("starred_by") mengambil relasi star untuk sekumpulan proyek sehingga serializer tidak perlu mengambil daftar pemberi star berulang untuk setiap kartu.
# Pada POST, request.data membaca input melalui parser DRF, termasuk JSON dan form. Ini berbeda dari request.POST yang dipakai pada form POST Django.
# is_valid(raise_exception=True) menghentikan alur ketika input salah, dengan response 400 dan error per field. .save() hanya dijalankan ketika input valid.
# Response(serializer.data, status=...) menerima data Python. Kita tidak perlu memanggil json.dumps atau menulis content_type secara manual.


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_detail(request, project_id):
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"), pk=project_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ProjectSerializer(
        project, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_list(request):
    context = {"request": request}
    if request.method in ("GET", "HEAD"):
        # Ambil relasi pemberi star sekaligus untuk mengurangi query berulang
        # saat serializer menghitung star dan membaca nama pengguna tiap kartu.
        # ID menjadi pembeda urutan ketika beberapa institusi bernama sama.
        educations = Education.objects.prefetch_related("starred_by").order_by("school", "id")
        school = request.query_params.get("school", "").strip()
        if school:
            educations = educations.filter(school__icontains=school)
        return Response(EducationSerializer(educations, many=True, context=context).data)
    serializer = EducationSerializer(data=request.data, context=context)
    # Hentikan request dengan respons 400 beserta error per field jika input salah.
    # save() hanya dijalankan setelah seluruh validasi berhasil.
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_detail(request, education_id):
    education = get_object_or_404(Education.objects.prefetch_related("starred_by"), pk=education_id)
    context = {"request": request}
    if request.method in ("GET", "HEAD"):
        return Response(EducationSerializer(education, context=context).data)
    if request.method == "DELETE":
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # Instance education membuat save() memperbarui objek yang sudah ada.
    # PATCH menerima sebagian field, sedangkan PUT memerlukan seluruh field wajib.
    serializer = EducationSerializer(
        education, data=request.data, partial=request.method == "PATCH", context=context,
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    # DELETE berhasil mengembalikan body kosong.
    # Frontend harus melewati pemanggilan response.json() untuk status 204.
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def education_star(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    # Identitas pemberi star berasal dari sesi login, bukan ID kiriman klien.
    # Endpoint bersifat toggle, sehingga dua POST akan menambah lalu membatalkan
    # star. Frontend menonaktifkan tombol selama request dan tidak retry otomatis.
    if education.starred_by.filter(pk=request.user.pk).exists():
        education.starred_by.remove(request.user)
    else:
        education.starred_by.add(request.user)
    return Response(EducationSerializer(education, context={"request": request}).data)