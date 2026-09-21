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