Nama : Nasywa Namira Suhendro
NPM : 2506532196
Kelas : PBP C

### Tugas 1
1. Ya, saya menggunakan elemen semantik HTML5 seperti <header>, <main>, <section>, dan <article>. Elemen-elemen ini membantu menstrukturkan dokumen web secara hierarkis dan logis, tidak hanya menggunakan tag <div> saja. Dengan membagi halaman menjadi <section id="profile"> dan <section id="experiences">, alur konten yang saya buat menjadi terpisah jelas secara semantik. Penggunaan tag <article> pada tiap kartu experience (misalnya RISTEK, SISTECH, dan DDP 0) mempertegas bahwa tiap kartu merupakan satu informasi utuh. Selain mempermudah keterbacaan kode, struktur ini mendukung aksesibilitas dan optimasi mesin pencari (SEO).

2. Tantangan tata letak utama yang dihadapi adalah menangani tata letak multi-kolom saat viewport mengecil/menyempit:
- Hero Grid (Profil & Foto): Pada layar desktop, teks profil dan foto sejajar secara horizontal. Saat berpindah ke layar mobile, foto dan blok teks rentan terpotong atau saling tumpang tindih. Evaluasi yang saya lakukan adalah mengubah tata letak dari multi-kolom menjadi kolom tunggal bertumpuk (stacked vertical layout) menggunakan media queries, sehingga foto berada di posisi proporsional dan teks bio tetap terbaca tanpa horizontal overflow.
- Experience Cards: Kartu experience saya yang berjajar 3 kolom di desktop dievaluasi menggunakan CSS Grid (`repeat(auto-fit, minmax(...))`). Ketika dibuka di ponsel, kartu-kartu tersebut otomatis menyesuaikan menjadi 1 kolom vertikal agar paragraf deskripsi tidak terlalu sempit dan teks tidak terpotong secara berantakan.

3. Batasan terbesar yang saya rasakan sebagai static web murni ada pada dua aspek: 
- seluruh data (seperti daftar experiences) masih bersifat hardcoded langsung di dalam markup HTML. Ketika ingin memperbarui data profil atau menambah pengalaman baru, saya harus mengubah baris kode secara manual, yang tentu tidak efisien dan rentan merusak layout jika datanya semakin banyak. 
Kedua, saya sempat kebablasan meng-explore via youtube hingga ingin menambahkan elemen-elemen dan animasi ikon menggunakan JavaScript, namun harus dibatasi demi memenuhi aturan tugas yang mensyaratkan murni HTML5 dan CSS3. Hal ini menyadarkan saya bahwa CSS  mempunyai batasam dalam menangani interaksi pengguna tingkat lanjut dan efek visual yang kompleks.

Berdasarkan batasan tersebut, fungsionalitas dinamis yang paling ingin saya tambahkan pada iterasi selanjutnya adalah:
- Pengelolaan data menggunakan database Django: Menyimpan data profil dan riwayat pengalaman di database agar penambahan/pembaruan konten dapat dilakukan secara dinamis melalui sistem/panel admin tanpa mengubah berkas HTML secara langsung
- Penerapan JavaScript untuk interaktivitas: Menambahkan skrip JavaScript guna meningkatkan interaksi pengguna dan memperindah tampilan web, seperti pembuatan animasi mikro, interaksi tombol yang lebih responsif, hingga penggunaan kit yang lebih kreatif

### AI Disclosure

- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi Percakapan: [Sesi Percakapan Gemini](https://share.gemini.google/NIMQI5M5d5fQ)
- Strategi Prompting
Saya menggunakan prompt bertahap dengan menyuruh AI Agent memposisikan dirinya sebagai mentor saya (agar tidak memberikan jawaban instant secara langsung) dan melampirkan screenshot tampilan web dan potongan kode yang bermasalah. Pertanyaan difokuskan ke solusi praktis, seperti cara membersihkan script pihak ketiga (Font Awesome), merapikan teks justify yang renggang, membetulkan layering/z-index, dan membagi commit bertahap di VS Code.
-Bagian yang Dibantu AI:
  1. Mengecek aturan tugas agar web tetap murni HTML5 dan CSS3 (menghapus script JS Font Awesome dan memperbaiki tag html yang bersarang).
  2. Memperbaiki masalah tampilan teks, seperti jarak kata yang terlalu renggang
  3. Membetulkan posisi huruf dan layer (z-index) pada bagian nama dan foto profil.
  4. Memberikan panduan cara melakukan commit bertahap (partial staging) lewat menu Source Control di VS Code.
- Keterbatasan AI & Perbaikan Mandiri:
  - AI sempat memberikan kode SVG yang terlalu panjang di HTML. Saya memilih untuk tidak memakainya dan menggantinya dengan file gambar lokal di folder static/img/ agar kodenya lebih rapi dan simpel.
  - Seluruh isi portofolio (bio, riwayat organisasi, kartu pengalaman, dan tema warna neobrutalism) saya tentukan dan rapikan sendiri.




### Tugas 2

## Deskripsi Proyek Tugas 2
Pada Tugas 2 ini, saya melakukan pembaruan pada website portofolio dengan mengimplementasikan konsep MVT (Model-View-Template) menggunakan framework Django. Data experience yang sebelumnya ditulis secara hardcoded di dalam HTML, kini telah diubah menjadi dinamis dengan menyimpannya ke dalam database. Dan juga menambahkan section/model baru yaitu Education.
- Fitur & Implementasi Utama:
* Pembuatan Model Django: Membuat model `Experience` dan `Education` di `models.py` untuk mendefinisikan struktur data portofolio.
* Migrasi Database: Menggunakan perintah `makemigrations` dan `migrate` untuk menerapkan struktur model ke dalam database.
* Push Data via Shell: Memasukkan data awal portofolio ke dalam database secara langsung melalui interactive console (`python manage.py shell`).
* Integrasi View dan Template: Mengambil data dari database melalui `views.py` dan menampilkannya secara dinamis pada halaman web menggunakan template tags Django.
* Pengurutan Data: Menerapkan logika pengurutan (`order_by`) pada view agar data portofolio yang ditampilkan selalu berurutan dengan rapi.

1. Ketika pengguna membuka halaman portofolio baru, browser mengirimkan request ke server yg pertama kali diterima oleh urls.py sebagai main gate. File ini kemudian mengarahkan rute tersebut ke urls.py tingkat aplikasi, yg bertugas mencocokan URL dengan fungsi yang tepat di dalam view. Fungsi view akan memproses permintaan ini dan meminta data riwayat yang diperlukan kepada model. Model kemudian bertugas mengambil data portofolio tersebut dari database dan mengembalikannya ke view. Setelah data diterima, view akan menyisipkan data dinamis tersebut ke dalam template HTML, lalu merendernya menjadi halaman web utuh yang dikirimkan kembali ke browser pengguna untuk ditampilkan sebagai response.

2. Data untuk bagian portofolio baru sebaiknya disimpan dalam models dan tidak ditulis langsung di dalam template agar aplikasi bersifat dinamis, bukan statis (hardcoded). Dari segi kemudahan pemerihaan (maintainability), menyimpan data di model memungkinkan saya untuk menambah atau mengubah isi portofolio melalui database tanpa harus membongkar dan mengedit kode HTML, sehingga meminimalisir risiko merusak desain halam web. Sementara itu, untuk pengembangan aplikasi (scalability) ke depannya, penggunaan model sangat memudahkan saya jika nanti data experience sudah semakin banyak, karena saya bisa dengan mudah memanfaatkan fitur advanced seperti search, filtering, atau pagination yang tidak akan bisa dilakukan secara efisien jika data diketik manual satu per satu di dalam template html.

3. Perintah makemigrations dan migrate pada Django memiliki peran yang berbeda namun saling melengkapi dalam mengelola database. makemigrations berfungsi seperti pembuat draf rancangan, di mana perintah ini akan mendeteksi setiap perubahan yang saya buat pada file models.py (contohnya menambahkan kelas baru atau mengubah field) dan mencatatnya ke dalam sebuah file migrasi tanpa mengubah database yang asli. Sebaliknya, migrate adalah perintah eksekutor yang menerapkan rancangan file migrasi tsb secara langsung ke dalam struktur database fisik, seperti membuat/menghapus tabel. Contohnya, ketika saya baru saja selesai menulis kode untuk model Education, saya harus menjalankan makemigrations terlebih dahulu utk membuat footage perubahannya, lalu dilanjut dengan menjalankan migrate agar Django benar2  menciptakan tabel Education tsb di dalam sistem database saya

## AI Disclosure
- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi Percakapan: [Sesi Percakapan Gemini](https://share.gemini.google/z8ZhKSEfqYdb)
- Strategi Prompting
Saya menggunakan prompt secara bertahap dan interaktif dengan melampirkan screenshot terminal PWS serta tampilan web untuk melakukan debugging. Saya meminta AI untuk bertindak sebagai mentor dan troubleshooter yang bantu menjelaskan penyebab error saat eksekusi Django shell dan memberikan arahann untuk solusi perbaikannya langkah demi langkah.
- **Bagian yang Dibantu AI:**
-Bagian yang Dibantu AI:
1. Memperbaiki masalah tampilan teks, seperti jarak kata yang terlalu renggang
2. Melakukan debugging dan mengatasi error saat meng-update data, seperti `NameError` (variabel terlewat) dan `FieldError` (salah nama atribut).
3. Membantu menyusun unit test
- Keterbatasan AI & Perbaikan Mandiri:
1. AI sempat keliru mengasumsikan nama field untuk institusi pendidikan sebagai `title` (mengikuti pola model sebelumnya), yang ternyata memicu `FieldError`. Saya kemudian mengecek kembali model saya dan menyadari bahwa nama field yang benar adalah `school`, lalu memperbaikinya secara mandiri di shell.

### Tugas 3

## Deskripsi Proyek Tugas 3
Pada Tugas 3 ini, saya mengimplementasikan penggunaan skeleton template html untuk menambahkan projects menggunakan form, menghapus projects, menyajikan data projects, dan mengedit data projects ke halaman web yang dibungkus terlebih dahulu dalam format JSON. Saya melakukan refactoring untuk setiap berkas html yg memiliki struktur kode identik seperti `base.html`, `education.html`, `experience.html`, `projects.html`, dan `education.html`. dilakukan extend terhadap template utama dan menerapkan mekanisme form & data delivery utk bagian `Education`.

## Pertanyaan Reflektif
1. Penggunaan `ModelForm` pada Django jauh lebih efisien dibandingkan membuat form HTML secara manual karena kita tidak perlu lagi mendefinisikan elemen input, label, atau tipe data satu per satu dari awal. Django akan secara otomatis menurunkan konfigurasi form langsung dari model yg sudah kita buat di `models.py` (inherit), sekaligus menangani proses validasi data secara centralized melalui method `is_valid()` dan penyimpanan data ke database cukup dengan memanggil method `save()`. Selain itu, kita diwajibkan menyertakan tag `{% csrf_token %}` sebagai bentuk proteksi keamanan dari serangan CSRF (*Cross-Site Request Forgery*)
2. Dalam pengembangan aplikasi web modern, format data JSON jauh lebih disukai dibandingkan XML karena struktur penulisannya yg jauh lebih ringkas dan ringan berbasih pasangan *key-value*. Hal ini membuat ukuran data yg dikirim melalui jaringan menjadi lebih kecil dan hemat *bandwidth* karena tidak memerlukan tag pembuka dan penutup yang berulang seperti pada XML. Selain itu, JSON secara alami merupakan turunan dari JavaScript, sehingga website maupun aplikasi modern dapat langsung memproses (*parse*) datanya dengan cepat tanpa memerlukan parser XML DOM tambahan yg rumit. lalu format JSON juga memiliki keterbacaan yang sangat baik bagi developer dan sudah menjadi format standay yg paling umum digunakan pada arsitektur REST API lintas platform.
3. Alur yang terjadi saat mengembalikan data portofolio dalam bentuk JSON dimulai ketika web mengirimkan *request* ke URL rute JSON (misalnya `/education/json/`). URL tersebut kemudian ditangkap oleh `urls.py` dan diteruskan ke fungsi view terkait yg bertugas mengambil sekumpulan data riwayat portofolio dari database menggunakan ORM Django, menghasilkan data berupa *QuerySet*. Selanjutnya, *QuerySet* yang berisi objek model Python akan diproses menggunakan modul serializer bawaan Django untuk diubah bentuknya menjadi format teks raw JSON (`serializers.serialize("json", ...)`). Teks JSON ini kemudian dikembalikan oleh view ke web di dalam objek `HttpResponse` dengan tipe konten `application/json`. Proses *serialization* ini sangat penting karena data di dalam Django berbentuk objek Python yang kompleks dan berada di memori server, sehingga datanya harus diubah terlebih dahulu ke dalam format standar seperti JSON agar dapat dikirim melalui protokol HTTP dan dipahami oleh aplikasi klien.

## AI Disclosure
- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi Percakapan: [Sesi Percakapan Gemini](https://share.gemini.google/QdmdCiNcqk9j)
- Strategi Prompting:
  Saya menggunakan pendekatan bertahap dan interaktif dengan meminta panduan untuk menyusun UI and UX design, melampirkan tangkapan layar kode, pesan *error* Django di web, serta terminal untuk meminta bantuan *debugging*. Saya mengarahkan AI untuk memandu penyusunan struktur CRUD secara runut, mendiagnosis akar penyebab *exception*, dan memberikan instruksi perbaikan kode tanpa merombak struktur templat yang sudah ada.

- Bagian yang Dibantu AI:
  1. Menyusun implementasi `EducationForm` di `forms.py` serta fungsi CRUD (`create_education`, `edit_education`, `delete_education`, dan `get_education_json`) di `views.py`.
  2. Melakukan *debugging* pada `AttributeError: 'function' object has no attribute 'META'` akibat argumen `request` yang terlewat pada pemanggilan `render()` di *view*.
  3. Mengatasi `TypeError: edit_education() got an unexpected keyword argument 'id'` dengan menyinkronkan parameter pada fungsi *view* dan rute URL.
  4. Merapikan tata letak dan *styling* action button (`Edit`, `Delete`, serta `+ Add education`) menggunakan animasi transisi CSS agar matching dengan komponen *navbar*.

- Keterbatasan AI & Perbaikan Mandiri:
  1. AI sempat menyarankan penulisan blok `<style>` di dalam templat HTML dan merombak tata letak kartu secara berlebihan, namun saya memutuskan untuk tetap mempertahankan struktur kode awal templat saya dan memindahkan seluruh aturan gaya ke berkas `style.css`.
  2. Perubahan gaya pada tombol sempat tidak muncul akibat peramban memuat berkas CSS statis lama dari memori *cache*. Masalah ini diselesaikan secara mandiri melalui *hard refresh* (*empty cache*) pada peramban.
  3. Sempat terjadi error sintaks tanda petik ganda (`""`) pada atribut tombol templat yang kemudian dikoreksi secara mandiri saat meninjau kembali berkas HTML.


### Tugas 4

## Deskripsi Tugas 4
Pada Tugas 4 ini, saya mengimplementasikan sistem autentikasi, manajemen sesi (*session*), penggunaan *cookies*, serta otorisasi berbasis peran (*role-based access control*) ke dalam portofolio web saya. Pengguna kini dapat mendaftar melalui form registrasi, masuk menggunakan form *login*, dan keluar melalui *logout*. Informasi sesi seperti waktu login terakhir dicatat dan ditampilkan pada antarmuka pengguna. 
Selain itu, saya menerapkan pembagian hak akses menjadi empat tingkatan peran: pengunjung tanpa login, pengguna biasa, peran Editor yang ditetapkan melalui Django Group, dan pemilik portofolio (*superuser*). Di sisi *backend*, saya menerapkan *server-side validation* yang menolak akses tidak valid dengan respons HTTP 403 Forbidden. Di sisi tampilan (*frontend*), visibilitas action button pada kartu project disesuaikan secara kondisional: peran Editor hanya diizinkan untuk mengubah (*edit*) data, pemilik portofolio memiliki akses penuh untuk menambah, mengedit, dan menghapus project, serta seluruh pengguna yang telah terautentikasi dapat memberikan maupun membatalkan bintang (*star*). Saya juga menyempurnakan *styling* navigasi dan tata letak responsif (*mobile layout*) agar antarmuka tetap rapi di berbagai ukuran layar.
  
## AI Disclosure
- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi Percakapan: [Sesi Percakapan Gemini](https://share.gemini.google/6ve8xLVrQDRQ)
- Strategi Prompting:
  Saya memanfaatkan AI sebagai pendamping belajar (*study buddy*) dan konsultan interaktif sepanjang pengerjaan tugas. Saya menggunakan pendekatan diskusi bertahap dengan menunjukkan tangkapan layar desktop untuk meminta masukan perbaikan visual, validasi alur logika autentikasi, serta memastikan implementasi peran berjalan sesuai panduan tugas tanpa mengabaikan aspek estetika desain.

- Bagian yang Dibantu AI:
  1. Konsultasi dan panduan penyesuaian desain antarmuka (*UI styling*) pada komponen navigation bar
  2. Memberikan saran perbaikan layout (*mobile layout*) menggunakan media query CSS agar elemen navbar dan content card tetap rapi di layar ponsel.
  3. Memandu alur pemahaman konsep otorisasi berbasis peran (pembedaan hak akses antara pengunjung umum, pengguna biasa, peran Editor melalui Django Group, dan superuser).
  4. Diskusi penataan visibilitas elemen antarmuka (tombol aksi pada kartu proyek) agar hanya tampil sesuai peran pengguna yang aktif.

- Keterbatasan AI & Perbaikan Mandiri:
  1. AI sempat memberikan asumsi keliru mengenai fitur yang belum terpasang, sehingga saya melakukan pengecekan mandiri pada basis kode untuk memvalidasi fungsionalitas yang sebenarnya sudah aktif.
  2. Rekomendasi struktur penulisan kelas CSS dari AI disaring dan disederhanakan kembali secara mandiri agar tetap ringkas serta tidak merombak hierarki templat yang sudah ada.
  3. Mengatasi kendala pembaruan visual statis yang tertahan memori singgahan (*browser cache*) secara mandiri melalui *hard refresh*.


  ### Tugas 5

## Deskripsi Tugas 5
Pada Tugas 5  ini, saya menerapkan seluruh pola interaktivitas dari Tutorial 5 pada halaman **Education**. Halaman **Education** kini hanya merender kerangka halaman, lalu data diambil secara terpisah dari endpoint JSON (`/api/education/`) menggunakan `fetch()`. Repsons JSON disusun secara manual dengan `JsonResponse` agar dapat menyertakan informasi **star** dari Tugas 4 (jumlah **star**, status **star** pengguna yang sedang login, dan daftar nama pengguna yang memberi **star**). Halaman juga menampilkan tiga kondisi: *loading* saat data dimuat, data kosong, dan *error* saat data gagal dimuat.

Fitur pencarian berdasarkan nama isntitusi berjalan lewat AJAX tanpa me-*reload* halaman, dengan *debouncing* 300ms sehingga permintaan hanya dikirim setelah penggunaan berhenti mengetik. `AbortController` dipakai untuk membatalkan permintaan lama agar hasil pencarian yang usang tidak menimpa hasil terbaru.
Form tambah *Education* kini berada di dalam modal (Popover API) pada halaman daftar dan dikirim dengan Fetch API ke view `create_education`. View ini hanya menerima POST, memeriksa hak akses di dalam view (`is_superuser`, bukan hanya menyembunyikan tombol di template), memvalidasi input dengan `EducationForm`, lalu membalas JSON dengan status JSON dengan status HTTP yang sesuai: 201 saat berhasil, 400 saat validasi gagal, dan 403 saat pengguna tidak berhak. Token CSRF dikirim lewat header `X-CSRFToken` (dibaca dari cookie `csrftoken`) dan juga lewat field `csrfmiddlewaretoken` dari `{% csrf_token %}`. Setelah data berhasil ditambahkan, modal tertutup dan daftar diperbarui tanpa *reload*. Hak akses dari Tugas 4 tetap berlaku, yaitu pengunjung yang belum login dapat membaca data, sedangkan penambahan dan penghapusan hanya dapat dilakukan oleh pemilik portofolio (*superuser*).
Hasil penambahan data diberitahukan lewat notifikasi *toast*, baik saat berhasil maupun saat gagal, termasuk pesan kesalahan validasi dari server. Untuk perlindungan XSS, setiap nilai teks yang disisipkan ke HTML lewat JavaScript di-*escape* dengan `escapeHtml`, dan input dibersihkan di sisi server dengan `strip_tags` pada method `clean_<field>` di `EducationForm` (ditambah validasi skema URL pada `clean_logo`). Pengujian dilakukan dengan memasukkan payload `<img src="x" onerror="alert('XSS!')">`, yang ditolak server dan tidak memunculkan *alert*. Saya juga merapikan *styling* tombol, *search bar*, dan tata letak kartu agar seragam di halaman Projects dan Education.

## Pertanyaan Reflektif
1.  *Debouncing* adalah teknik untuk menunda eksekusi sebuah fungsi sampai ada jeda waktu tertentu tanpa *event* baru. Setiap kali pengguna mengetik, *timer* sebelumnya dibatalkan dengan `clearTimeout`, lalu *timer* baru dimulai dengan `setTimeout`. Fungsi pencarian hanya berjalan jika pengguna berhenti mengetik selama `SEARCH_DEBOUNCE_DELAY` (300 ms pada proyek ini).
Tanpa *debouncing*, *event* `input` memicu satu permintaan untuk setiap karakter. Mencari "Universitas" berarti 11 permintaan berturut-turut. Hal ini membebani server dan *database*, memboroskan *bandwidth*, dan membuat tampilan berkedip karena grid di-*render* ulang terus. Permintaan lama juga bisa selesai belakangan dan menimpa hasil pencarian yang lebih baru (*race condition*), sehingga selain *debouncing* saya memakai `AbortController` untuk membatalkan permintaan sebelumnya. *Debouncing* berbeda dari *throttling*: *debouncing* menunggu sampai *event* berhenti, sedangkan *throttling* membatasi fungsi agar hanya berjalan sekali per interval.'
2. `fetch()` mengembalikan sebuah `Promise` yang baru selesai setelah server membalas. Keyword `await` (hanya dapat dipakai dalam `async function`) menghentikan eksekusi di baris tersebut sampai *Promise* selesai, lalu memberikan nilainya, yaitu objek `Response`. Pola yg sama dipakai pada `await response,json()` untuk membaca isi *body*.
Jika `await` tidak dipakai, kode di bawahnya langsung berjalan tanpa menunggu server. Variabel `response` hanya berisi *Promise* yang masih *pending*, bukan `Response`, sehingga `response.ok` bernilai `undefined` dan `response.json()` menimbulkan `TypeError`  karena *Promise* tidak memiliki *method* tersebut. Data juga belum tersedia saat grid di-*render*, sehinngga halaman bisa terus menampilkan *loading* atau kosong. Selain itu, `try/catch` tidak menangkap kegagalan `fetch()` karena *rejection*nya terjadi di luar alur kode tersebut.
3. XSS adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke halaman web yang kemudian dijalankan di *browser* pengguna lain. Pada *stored XSS*, *payload* disimpan ke *database* lalu ikut dieksekusi setiap kali data tersebut ditampilkan. Dampaknya serius: kode yang disisipkan dapat membaca cookies atau token CSRF, mengirim permintaan atas nama korban, atau mengubah tampilan halaman.
*Template* Django melakukan *auto-escaping* pada setiap `{{ variabel}}`, sehingga karakter seperti `<`, `>`, `&`, `"`, dan `'` diubah menjadi *entity* dan tampil sebagai teks biasa. Pada AJAX, data JSON disisipkan ke *template literal* lalu dipasang lewat `innerHTML`. Django tidak lagi terlibat, sehingga *browser* mem-*parse* string tersebut sebagai HTML sungguhan dan menjalankan atributnya (seperti `onerror`).
Mitigasi yang saya terapkan ada dua lapis. Pertama di sisi klien setiap  nilai teks dibungkus `escapeHtml()` sebelum masuk ke `innerHTML` (`showToas` sudah memakai `textContent`). Kedua, di sisi server `strip_tags` dipasang pada `clean_<field>` di `EducationForm`, ditambah validasi URL pada `clean_logo`. `strip_tags` bukan pengganti *escaping*, sehingga *escaping* saat menampilkan data tetap menjadi pertahanan utama.

## AI Disclosure
- Tool yang digunakan: Gemini
- Tautan Log / Sesi Percakapan: [Sesi Percakapan Gemini](https://gemini.google.com/app/8e3d85e8b82c1c61)
- Strategi Prompting: 
  Saya memakai AI sebagai pendamping *debugging* dan konsultan implementasi. Saya mengunggah berkas tugas dan tutorial (PDF), kode proyek (`views.py`, `urls.py`, `models.py`, `forms.py`, *template* HTML), serta tangkapan layar *error* dan tampilan *browser*. Dari situ saya meminta analisis penyebab *error* dan perbaikan bertahap, lalu menguji setiap perubahan sendiri di *browser* sebelum lanjut ke langkah berikutnya.

- Bagian yang Dibantu AI:
  1. Menganalisis *error* `NoReverseMatch` pada `toggle_star_education` yang disebabkan pola URL `<uuid:id>`, padahal model `Education` memakai ID *integer*.
  2. Menemukan kesalahan pada halaman Education: nama variabel JavaScript yang tidak konsisten, nama *field* yang masih memakai *field* Projects, sisa blok `{% if education_list %}`, dan *typo* `stared_by` pada `prefetch_related`.
  3. Membantu *styling* kartu *education*, *search bar*, dan penyeragaman tombol (warna, font, dan tata letak grid) agar konsisten di halaman Projects dan Education.

- Keterbatasan AI & Perbaikan Mandiri:
  1. AI tidak dapat menjalankan kode saya dan awalnya belum melihat seluruh berkas, sehingga beberapa saran (nama *field*, nama *class* CSS) berdasarkan asumsi. Saya memeriksa basis kode sendiri dan menyesuaikannya dengan struktur proyek yang sebenarnya.
  2. Kode *template* dari AI memakai *class* generik yang tidak cocok dengan desain Education saya, sehingga tampilan awal berbeda. Saya menyesuaikan nama *class*, teks label, dan CSS secara mandiri agar konsisten dengan gaya portofolio.
  3. Sebagian perubahan sempat tertempel tidak lengkap sehingga halaman Education kosong. Saya menelusuri sendiri bagian mana yang masih memakai versi lama dan memperbaikinya.
  4. Seluruh fungsionalitas saya uji sendiri: akses sebagai pengunjung, pengguna biasa, dan superuser; kondisi *loading*/kosong/*error*; *debouncing* lewat tab Network; status 201/400/403; serta *payload* XSS. Perubahan CSS yang tidak langsung tampak diatasi dengan *hard refresh*.



### Tugas 6

## Deskripsi Tugas 6

Pada Tugas 6 ini, saya melanjutkan pengembangan halaman **Education** dengan menerapkan Django REST Framework (DRF). Model dan data pendidikan dari tugas sebelumnya tetap digunakan, sedangkan penyajian serta pengelolaan datanya sekarang dilakukan melalui endpoint `/api/v1/education/`. Jika pada Tugas 5 respons JSON disusun secara manual menggunakan `JsonResponse`, pada tugas ini saya menggunakan `EducationSerializer` yang diturunkan dari `ModelSerializer`. Serializer mengatur representasi data, memvalidasi input, serta menyediakan informasi star berupa jumlah star, status star pengguna yang sedang login, dan nama pengguna pemberi star. Field hasil perhitungan tersebut bersifat *read-only*.

Endpoint Education dibagi menjadi daftar, detail, dan star. Endpoint daftar mendukung GET untuk membaca serta POST untuk menambahkan data. Endpoint detail mendukung GET, PUT, PATCH, dan DELETE, sedangkan endpoint star menerima POST dari akun yang sudah login. Pencarian berdasarkan nama institusi dilakukan melalui parameter query `school`. Respons menggunakan status HTTP sesuai hasil operasi, yaitu 201 ketika data berhasil dibuat, 400 untuk input tidak valid, 403 untuk tindakan yang tidak diizinkan, 404 untuk data yang tidak ditemukan, dan 204 setelah data berhasil dihapus.

Hak akses diterapkan melalui `IsPortfolioOwnerOrEditorOrReadOnly` dan `SessionAuthentication`. Pengunjung tanpa login dapat membaca daftar dan detail pendidikan. Pengguna biasa dapat memberikan atau membatalkan star, Editor dapat mengubah data melalui PUT/PATCH, dan pemilik portofolio (*superuser*) dapat menambah, mengubah, serta menghapus data. Endpoint star menggunakan `IsAuthenticated`, dengan identitas pemberi star selalu diambil dari `request.user`. Pemeriksaan akses pada view edit Education lama juga disesuaikan agar Editor dapat mengubah data.

Pada sisi tampilan, halaman Education menggunakan `fetch()` untuk menampilkan, mencari, menambah, mengedit, menghapus, dan memberikan star tanpa me-*reload* halaman. Pengeditan dilakukan melalui modal yang diisi dengan data terbaru dari API, kemudian mengirim perubahan menggunakan PATCH. Notifikasi toast menampilkan hasil operasi maupun pesan kesalahan dari server. Pencarian tetap menggunakan *debouncing* 300 ms dan `AbortController`. Saya juga menambahkan tombol Reset pencarian serta indikator jumlah hasil untuk membantu pengguna mengetahui hasil pencariannya.

Setiap permintaan yang mengubah data menyertakan header `X-CSRFToken`. Input teks dibersihkan melalui `strip_tags` pada method `validate_<field>` di serializer, sedangkan nilai teks yang dimasukkan ke HTML melalui JavaScript tetap di-*escape* menggunakan `escapeHtml()`. Pengujian Education ditulis menggunakan `APITestCase` untuk memeriksa hak akses setiap peran, validasi input, perilaku star, serta perlindungan CSRF. Pada permintaan yang ditolak, test juga memeriksa database untuk memastikan data tidak berubah.

Untuk menjalankan proyek, saya mengaktifkan virtual environment, memasang dependency melalui `python -m pip install -r requirements.txt`, menjalankan `python manage.py migrate`, lalu menyalakan server dengan `python manage.py runserver`. Seluruh test aplikasi, termasuk test Projects dari Tutorial 07, dijalankan menggunakan `python manage.py test main`.

## Pertanyaan Reflektif

1. REST (*Representational State Transfer*) adalah gaya arsitektur untuk merancang komunikasi antara klien dan server dengan memperlakukan data sebagai *resource* yang diakses melalui URL. Pada proyek saya, endpoint `/api/v1/education/` digunakan untuk kumpulan data pendidikan, sedangkan `/api/v1/education/{id}/` digunakan untuk satu data pendidikan. Operasinya menggunakan method HTTP sesuai tujuan, seperti GET untuk membaca, POST untuk menambahkan, PUT/PATCH untuk memperbarui, dan DELETE untuk menghapus data.

   Mengembalikan JSON saja belum cukup untuk menyebut API sebagai RESTful karena JSON merupakan format representasi data. Perancangan API juga perlu mengikuti prinsip REST, seperti pemisahan klien dan server, antarmuka yang konsisten, serta komunikasi *stateless*. Pada komunikasi *stateless*, setiap request membawa informasi yang diperlukan untuk diproses tanpa bergantung pada konteks percakapan request sebelumnya. Implementasi tugas ini sendiri menggunakan sesi login Django sesuai ketentuan `SessionAuthentication`, sehingga penggunaan JSON dan method HTTP belum membuktikan seluruh batasan REST terpenuhi.

   PUT digunakan untuk mengirim representasi pengganti suatu resource, sedangkan PATCH digunakan untuk memperbarui sebagian field. Contohnya, PUT dapat dipakai ketika saya mengirim ulang seluruh field wajib Education, seperti `school`, `degree`, `start_year`, dan `description`. PATCH lebih sesuai ketika saya hanya ingin mengganti `degree` tanpa mengirim ulang field lainnya. Pada implementasi saya, PATCH menggunakan `partial=True` agar field yang tidak dikirim tetap mempertahankan nilai sebelumnya. Field opsional pada PUT tetap mengikuti aturan serializer yang digunakan.

2. Serializer pada Django REST Framework berperan untuk mengubah objek model menjadi representasi data yang dapat dikirim ke klien, sekaligus memvalidasi input sebelum disimpan ke database. Pada proyek saya, `EducationSerializer` menggunakan `ModelSerializer` agar definisi field dan proses dasar penyimpanannya mengikuti model `Education`. Daftar field ditulis secara eksplisit supaya informasi yang ditampilkan API dapat dikendalikan, termasuk memastikan data akun sensitif tidak ikut dikirim.

   Dibandingkan menyusun dictionary secara manual dengan `JsonResponse` pada Tugas 5, serializer membuat representasi data dan validasi input lebih terpusat. View cukup mengirim data ke serializer, memanggil `is_valid()`, lalu menjalankan `save()` jika input valid. Aturan pembersihan teks ditempatkan pada method `validate_<field>`, sedangkan field seperti `star_count` dan `is_starred` dihitung menggunakan `SerializerMethodField`. Dengan demikian, logika yang sama dapat digunakan pada endpoint daftar, detail, tambah, dan update tanpa ditulis berulang di setiap view.

   Serializer juga menyediakan pesan kesalahan per field yang dapat dikembalikan dengan status 400 dan ditampilkan melalui toast. Namun, serializer tidak otomatis menjalankan validasi dari `EducationForm`, sehingga aturan yang diperlukan untuk input API tetap harus diterapkan pada serializer.

3. Autentikasi adalah proses mengenali identitas pengguna, sedangkan otorisasi adalah proses menentukan tindakan yang boleh dilakukan pengguna tersebut. Pada proyek saya, `SessionAuthentication` mengenali akun melalui sesi login Django dan mengisi `request.user`. Setelah identitas diketahui, permission class memeriksa apakah peran pengguna mengizinkan method request yang dikirim.

   Contohnya, pengguna biasa yang sudah login diperbolehkan memberikan star tetapi tetap ditolak saat mencoba menambahkan pendidikan. Editor diperbolehkan melakukan PUT/PATCH, tetapi tidak dapat membuat atau menghapus data. Superuser memiliki akses untuk seluruh operasi pengelolaan Education.

   Hak akses harus diperiksa di server karena menyembunyikan tombol hanya mengatur tampilan antarmuka. Pengguna masih dapat mengirim request secara langsung melalui Console browser atau aplikasi penguji API. Permission class memastikan request yang tidak diizinkan ditolak sebelum perubahan diproses. Karena itu, test penolakan juga memeriksa isi database untuk membuktikan bahwa data tetap sama setelah request ditolak.

4. Permintaan yang mengubah data tetap memerlukan token CSRF karena `SessionAuthentication` menggunakan cookie sesi yang dapat dikirim otomatis oleh browser. Kondisi ini dapat dimanfaatkan situs berbahaya untuk mencoba mengirim permintaan menggunakan sesi pengguna yang masih aktif. Token CSRF membantu server memvalidasi bahwa permintaan menyertakan token yang sesuai dengan cookie CSRF pengguna.

   Pada proyek saya, request POST, PATCH, dan DELETE melalui Fetch menyertakan header `X-CSRFToken`. Template Education juga merender `{% csrf_token %}` agar cookie CSRF tersedia, termasuk untuk pengguna biasa dan Editor yang dapat memberikan star. Pemeriksaan CSRF tetap diperlukan meskipun data dikirim dalam format JSON.

   Test menggunakan `force_authenticate` belum cukup untuk membuktikan perlindungan tersebut karena method ini langsung menetapkan pengguna pada request tanpa menjalankan autentikasi sesi yang sebenarnya. Oleh karena itu, saya menggunakan `APIClient(enforce_csrf_checks=True)` dan `.login()` untuk membentuk sesi login. Test kemudian mengirim request perubahan tanpa token dan memeriksa bahwa responsnya 403 serta database tidak berubah. Request dengan token valid juga diuji agar operasi yang diizinkan tetap dapat berjalan.

## AI Disclosure

- Tool yang digunakan  
  Gemini

- Tautan Log / Sesi Percakapan  
  https://share.gemini.google/ECb8dJNEs6Li

- Strategi Prompting  
  Saya menggunakan AI sebagai pendamping implementasi dan *debugging* secara bertahap. Saya melampirkan PDF tutorial dan tugas, ZIP kode proyek, serta tangkapan layar kode dan terminal. Saya meminta AI menyesuaikan implementasi dengan model Education yang sudah ada, memeriksa seluruh checklist tugas, dan memberikan petunjuk perubahan pada bagian kode tertentu.

- Bagian yang Dibantu AI

  1. Menyusun `EducationSerializer`, validasi input teks dan logo, serta field informasi star yang bersifat *read-only*.
  2. Menyusun permission empat peran dan endpoint Education untuk daftar, detail, CRUD, pencarian, serta star.
  3. Mengintegrasikan endpoint DRF dengan halaman Education melalui Fetch, termasuk modal edit, toast, CSRF, dan escaping.
  4. Menyusun test hak akses, validasi, star, dan CSRF, serta membantu menelusuri kesalahan nama file saat proses staging dan commit.

- Keterbatasan AI & Penyesuaian Selama Pengerjaan

  1. Saran awal AI menggunakan `EducationForm(prefix='edit')`, sehingga nama input berubah menjadi `edit-school`, sementara JavaScript mencari `school`. Setelah ketidaksesuaian ditemukan, AI memberikan koreksi menjadi `EducationForm(auto_id='edit_%s')` agar ID input tetap unik dan nama field sesuai dengan JavaScript.
  2. Panduan AI menggunakan nama file `tests_education_api.py`, sedangkan file yang saya buat bernama `test_education_api.py`. Perbedaan nama tersebut menyebabkan `git add` gagal. Perintah kemudian disesuaikan dengan nama file yang benar-benar ada di proyek.
  3. AI dapat memeriksa kode dan menjalankan test pada salinan proyek, tetapi hasilnya perlu dibedakan dari kondisi terbaru di laptop maupun deployment
  4. Saya menerapkan perubahan melalui VS Code secara bertahap, menyesuaikan bagian kode yang berubah, dan menggunakan hasil terminal serta tangkapan layar untuk meninjau masalah yang muncul. Proses ini menunjukkan bahwa saran AI tetap perlu diperiksa terhadap struktur proyek dan hasil eksekusi yang sebenarnya.