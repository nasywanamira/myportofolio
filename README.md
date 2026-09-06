Nama : Nasywa Namira Suhendro
NPM : 2506532196
Kelas : PBP C

# Tugas 1
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