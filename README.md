## Nama: Pearlita Anindya Prameswari

## NPM: 2506547670

## Kelas: PBP C



### Deskripsi Proyek: 

Website portofolio yang sudah di-deploy sekarang memiliki section profile yang berisi identitas saya sebagai mahasiswa Sistem Informasi Universitas Indonesia. Terdapat foto saya, kontak saya (LinkedIn, Email, dan GitHub) yang dilengkapi dengan CSS tombol yang akan langsung me-redirect pengunjung ke situs-situs terkait, serta deskripsi tentang saya. Kemudian saya menambahkan section Experiences untuk mendeskripsikan pengalaman berorganisasi serta pengalaman bekerja saya sebagai Asisten Dosen. Selain itu, saya juga menambahkan section Education untuk mendeskripsikan pengalaman pendidikan saya. Header website yang dilengkapi dengan hover. Apabila navigation bar di-hover, tiap-tiap opsi navigation bar akan berubah menjadi warna accent-dark.

Kemudian, website yang telah di-deploy sekarang juga memiliki section yang menampilkan informasi akademik dan pengalaman saya. Pada section Experience, ditampilkan pengalaman organisasi dan pengalaman bekerja saya. Pada section Education, ditampilkan riwayat pendidikan saya, baik dari gelar, institusi, nilai (IPK), dan periode pendidikan. Data pada kedua section dikelola menggunakan model Django sehingga dapat ditampilkan secara dinamis pada halaman portofolio.

Data kedua section juga dapat ditambahkan, diperbarui, dihapus, dan dicari melalui fitur yang telah terhubung dengan database Django. Proses input dan update data menggunakan Django `ModelForm`, sedangkan fitur pencarian dilakukan berdasarkan data yang dimasukkan pengguna. Website juga sekarang telah menyediakan endpoint JSON untuk mengambil data Experience dan Education melalui serialization. Dengan demikian, informasi pada portofolio tidak lagi ditulis secara statis pada HTML. Informasi sekarang dapat dikelola dan ditampilkan secara dinamis melalui Django.

### Tugas 1

1. Saya menggunakan elemen semantik HTML5 seperti <section> dan <container> untuk membagi atau mengelompokkan section-section, yaitu experiences dan education agar tidak tercampur. ELemen semantik tersebut membantu dari segi readbility kode yang telah saya buat. Selain itu, kedua elemen semantik tersebut membantu mempermudah penulisan CSS menjadi lebih ringkas.
2. Tantangan yang saya rasakan adalah pada pembuatan garis vertikal untuk experience dan education serta titik pink untuk menandakan "title". Tantangan yang saya rasakan ada pada saat memastikan bagaimana garis yang berada di bawah titik tidak "bocor" atau panjangnya tidak melebihi posisi titik. Saya mengevaluasinya dengan mengecek sati-satu bagian yang penting dan mengatur jarak padding dan position menggunakan ukuran yang fleksibel sehingga saat dibuka di mobile garis dan titiknya tetap menempel rapih. Saya juga melakukan trial and error untuk beberapa padding dan margin, saya coba satu per satu ukuran lalu me-refresh dan melihat apakah sudah tepat dan rapih. Tantangan lainnya muncul di efek hover pada timeline (experience dan education). Awalnya, efek hover yang memunculkan background di tiap timeline items dapat berjalan secara normal tanpa ada kendala. Namun, masalah mulai muncul ketika saya memutuskan untuk mengubah font menjadi Poppins. Font Poppins sendiri memang cenderung lebih besar dibanding font yang sebelumnya digunakan (Segoe UI). Oleh karena itu, saat saya mencoba untuk meng-hover mouse saya ke timeline item, "kebocoran" pada text dan background terjadi, mengakibatkan saya harus men-setting ulang paddingnya. Hal ini juga terjadi pada proses penambahan navigation bar. Navigation bar awalnya hanya terdiri dari satu elemen, belum ada masalah. Mulai muncul masalah ketika saya mencoba untuk menambahkan 2 navigation bar baru untuk Experiences dan Education, navigation bar menjadi terlalu panjang apabila website dijalankan di mobile. Saya kemudian mencoba untuk men-setting tampilan CSS mobile melalui @media. Saya mencoba untuk mengecilkan gap dan font size. Namun hal tersebut belum berhasil, saya kemudian mencoba untuk mengubah flex-direction site-header menjadi column dan men-set gap. Kemudian saya set alignment untuk header 1 (nama saya) menjadi rata kiri dan navigation bar menjadi rata kanan dan saya menggunakan flex-wrap untuk mencegah content keluar dari layout. Saya banyak melakukan trial and error di bagian ini serta saya juga banyak membaca mengenai flexbox pada CSS melalui website MDN Web Docs (https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts#multi-line_flex_containers_with_flex-wrap).
3. Batasan yang saya rasakan saat mencoba menyajikan informasi secara optimal adalah semua masih serba manual. Contohnya, apabila saya ingin menambahkan experience baru, saya tidak bisa langsung menambahkan di web. Saya harus membuka file kode portofolio saya dan mengedit index.html, menambahkan informasi baru, lalu push ke github serta pws. Hal ini juga perlu dilakukan apabila ada kesalahan pada data (saya mengalaminya, dapat terlihat di commit github saya yang mem-fix typo) dan harus diedit secara manual. Proses ini memakan waktu yang cukup banyak apabila data yang ada sering berubah. Fungsionalitas dinamis yang ingin saya persiapkan dan tambahkan pada iterasi proyek selanjutnya adalah saya ingin membuat fitur yang memungkinkan data portofolio saya dapat diedit sehingga saya dapat mengubah informasi yang diperlukan melalui sebuah form dan menyimpan perubahan tersebut tanpa harus mengubah struktur kode saya secara manual.

AI Disclosure:

1. Saya menggunakan Generative AI Gemini pada proses membuat style CSS line dan dot pada section experience dan education. Detail prompting serta analisis pribadi saya terhadap jawaban yang diberikan Gemini:

Prompt:
"Apakah garis dengan titik pada tiap experience dan education merupakan CSS yang ideal untuk website portofolio? Bagaimana saya bisa menerapkannya? Mohon jangan berikan saya contoh kodenya, berikan saya referensi sumber yang bisa saya baca."
Jawaban:
Gemini men-suggest CSS tersebut adalah CSS yang baik, Gemini mulai menjelaskan kepada saya terkait bagaimana mengimplementasinya, yaitu dengan menggunakan border-left TANPA memberikan kode secara langsung. Gemini juga men-direct saya ke situs seperti W3Schools, CSS-Tricks, dan MDN Web Docs. Selanjutnya saya mencoba untuk membuat garis border-left sambil membaca dokumentasi dari MDN Web Docs (https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left). Awalnya saya mencoba satu per satu baris kode yang ada di dokumentasi tersebut. Lalu saya bertanya lebih lanjut mengenai penggunaan before dan after dalam kasus ini.

Prompt:
"Saya sudah membuat garis vertikal untuk tiap experience, saya agak stuck dan bingung untuk bagian dot di atas garis. Apakah kamu ada saran? Berikan website referensi untuk dibaca dan jangan beri kode langsung."
Jawaban:
Gemini memberikan saran untuk mengimplementasikan before dan after, kemudian memberikan saya website MDN Web Docs untuk dibaca (https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before dan https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after). Awalnya saya mencoba untuk mengimplementasi apa yang berada di website tersebut secara mentah-mentah untuk melihat bagaimana cara kerjanya (saya melakukan trial and error). Lalu, setelahnya saya mulai mengimplementasikan before untuk garis vertikal dan after untuk dot (mirip seperti saat membuat garis tetapi radius dibuat menjadi 50%). Kemudian, muncul masalah posisi (padding dan margin) titik dan garis yang "bocor" atau garis melebihi dot. Akhirnya saya menanyakan kembali kepada Gemini.

Prompt:
"Saya sudah mengimplementasikan before dan after, tetapi dot dan garis vertikalnya masih tidak sesuai. Saya tidak ingin garis vertikalnya "bocor" hingga melebihi dot. Yang paling mengganggu adalah adanya garis yang "bocor" ke bawah setelah experience terakhir, apakah kamu memiliki saran..?"

Jawaban:
Gemini kemudian memberikan saran terkait implementasi last child lalu memberikan contoh kode yang tentunya saya lakukan verifikasi ulang dengan website MDN Web Docs (https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child). Lalu saya langsung menerapkan "display: none" pada bagian timeline-items:last-child::before tujuannya untuk menghapus garis yang "bocor" melebihi dot di bagian bawah. Terkait implementasinya, saya banyak sekali melakukan trial and error karena ada beberapa bagian di dokumentasi yang cukup membingungkan.

2. Saya menggunakan Generative AI Gemini untuk berkonsultasi terkait mobile tap interaction dan macam-macam pseudoclass yang ada di CSS.

Prompt:
"Saya ingin membuat website saya juga interaktif di mobile, tidak hanya di desktop. Kalau saya ingin membuat tap interaction, pseudoclass apa yang harus saya gunakan? Berikan sumber informasi dan sumber belajar terkait agar saya bisa belajar lebih lanjut mengenai ini."
Jawaban:
Gemini memberikan suggestion terkait implementasi focus dan active pada CSS saya. Kemudian, Gemini memberikan dan men-direct saya menuju website MDN Web Docs terkait dokumentasi pseudoclass active dan focus (https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus dan https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active). Kemudian saya kembali mencari di internet terkait tap action CSS property (https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action). Setelah benar-benar memahaminya, saya baru meng-add active di file CSS saya dan onclick di index.html. Awalnya, saya hanya meng-add onclick="" pada beberapa komponen timeline item untuk melihat apakah benar-benar berhasil. Setelah saya mencoba untuk membukanya lewat handphone saya, saya kemudian baru menambah onclick ke seluruh timeline items (experience dan education).

### Tugas 2

1. Alur yang terjadi saat pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada *browser*:
   Awalnya pengguna akan membuka halaman portofolio (bisa experience ataupun education). Kemudian, browser akan mengirimkan request ke proyek Django, yang pertama kali menerima adalah `urls.py `yang mengarahkan request ini ke aplikasi main. Pada `urls.py` aplikasi, url tersebut dipetakan menuju view yang sesuai (apabila Experience, ke `show_experience` dan apabila Education, ke `show_education`). Kemudian, `view` akan mengambil data terkait (experience atau education) melalui model (dengan `Experience.objects.all()` atau `Education.objects.all()`). Data-data yang telah diambil akan dimasukkan ke context dan dikirim ke template (`experience.html` atau `education.html`). Kemudian, pada template digunakan *Django Template Language* untuk me-loop data dan menampilkan tiap *object* ke HTML. Setelah di-*render*, Django kemudian mengirimkan hasil HTML tersebut ke browser sampai akhirnya pengguna dapat melihat halaman portofolio yang dipilih (experience atau education).

2. Data bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template karena model dapat membuat data menjadi lebih mudah dikelola. Selain itu, model membuat data menjadi lebih terstruktur di dalam database. Template seharusnya hanya bertugas untuk menampilkan data tersebut. Selain dari segi pengelolaan, apabila data langsung ditulis pada template, setiap kali ada perubahan (penambahan, penghapusan, atau peng-editan data) kode HTML harus diubah secara manual. Hal ini tentunya membuat website lebih sulit dipelihara dan kurang fleksibel. Namun, dengan model, perubahan data dapat dilakukan tanpa harus mengubah template (file HTML) secara langsung. Data juga menjadi lebih mudah dikembangkan, misalnya dengan penambahan object atau menambahkan field lain. Dengan begitu, pemisahan data dan tampilan membuat website menjadi lebih rapi, mudah dipelihara, dan mudah dikembangkan.

3. Perbedaan `makemigrations` dan `migrate` pada Django adalah `makemigrations` digunakan untuk membuat *file migration* berdasarkan perubahan yang dilakukan pada model. File tersebut akan berisi instruksi mengenai perubahan struktur database yang diperlukan. `migrate` digunakan untuk menerapkan migration tersebut ke *database* sehingga struktur database benar-benar dapat diperbarui. Contohnya adalah saat saya mengubah *field* `started_at` dan `ended_at` pada kedua model dari `DateTimeField` menjadi `DateField`. Saat saya menjalankan `makemigrations`, perintah tersebut akan mencatat perubahan yang saya lakukan. Kemudian, perintah `migrate` akan menerapkan perubahan tersebut ke *database.*

#### AI Disclosure:

- **Tool yang digunakan:** ChatGPT

- **Sesi percakapan:** https://chatgpt.com/share/6aa783ce-eb70-83ec-8b34-0b845ca25325

- **Strategi prompting:** Saya menggunakan Generative AI untuk berkonsultasi terkait branching GitHub supaya lebih terstruktur. Saya melontarkan berbagai pertanyaan kemudian saya kembali meng-*explore branching* pada GitHub melalui website GitHub itu sendiri serta beberapa sumber di internet seperti (GitHub Docs serta Medium).

- **Bagian spesifik yang dibantu:**

1. *Branching* dan tips meng-*commit* sesuai *branch* yang direkomendasikan
2. Pesan *commit* yang sesuai apabila dilakukan sebuah perubahan pada *branching*

- **Keterbatasan AI & Perbaikan Mandiri:**

1. Ada beberapa hal yang AI berikan kepada saya (contohnya kode *unit test*) yang tidak sesuai dengan model saya. Tentu saja, saya tidak menggunakan *unit test* tersebut dan hanya berfokus pada tips *branching* dan *commit*

### Tugas 3

1. Penggunaan `ModelForm` pada Django dilakukan untuk memudahkan penambahan/update data pada website. ModelForm digunakan sebagai bantuan untuk membuat form sesuai dengan model yang telah dibuat. Hal ini membuat proses validasi dan field tidak perlu dibuat secara manual dan secara langsung melalui struktur HTML. Selain itu, `ModelForm `dapat membuat proses memasukkan data menjadi lebih mudah karena data dari form dapat disimpan langsung menggunakan `form.save()`. `{%csrf_token%}` digunakan untuk melindungi form yang telah dibuat dari serangan *Cross-Site Request Forgery (CSRF)*, yaitu serangan fiber yang menipu pengguna agar tanpa sadar melakukan tindakan atau mengirimkan request tidak sah ke sebuah aplikasi/web di mana pengguna sedan aktif. Token tersebut berfungsi untuk memastikan bahwa request yang dikirim bukan merupakan request palsu yang dibuat pihak lain dan berasal dari website asli. Selain itu, karena form yang telah dibuat melakukan request POST yang dapat mengubah data di server, token CSRF wajib ditambahkan sebagai bagian dari mekanisme perlindungan tersebut.

2. JSON lebih sering digunakan dalam *Web Development* modern karena formatnya yang dinilai lebih sederhana dan ringan jika dibandingkan dengan XML. Struktur JSON lebih mudah dibaca karena menggunakan pasangan *key-value* sehingga lebih praktis untuk digunakan dalam pertukaran data antara server dan *client*. Selain itu, JSON juga memiliki dukungan yang baik dalam JavaScript dan dapat digunakan oleh berbagai bahasa pemrograman. Oleh karena itu, banyak dilakukan penggunaan JSON dalam API untuk menerima dan mengirimkan data antara *front-end* dan *back-end*.

3. Saat fungsi `view` dipanggil, data diambil dari *database* dengan model Django. Data tersebut kemudian akan diubah menjadi format JSON dengan serialization. Kemudian, JSON akan dikembalikan pada client melalui `HttpResponse`. Serialization diperlukan untuk mengubah data dari object Django menjadi format JSON yang bisa dibaca oleh *client*.

#### AI Disclosure:

- **Tools yang digunakan:** ChatGPT dan Gemini
- **Sesi percakapan**:
  https://chatgpt.com/c/6aae9338-1874-83ec-9356-a771d66fbcf7
  https://share.gemini.google/3mFTsYxpfcwJ

- **Strategi Prompting**: Saya menggunakan Generative AI ChatGPT dan Gemini untuk berkonsultasi terkait implementasi fitur update pada Django (penggunaan ModelForm dan validasi input) serta pengelolaan branching pada GitHub. Saya memberikan pertanyaan secara bertahap mengenai cara kerja update data, penggunaan DecimalField, dan pengaturan widget dan atribut pada form. Kemudian, saya menyesuaikan kembali dengan struktur project yang saya gunakan. Untuk konsultasi branching GitHub, saya mengirimkan kendala yang saya miliki kemudian memahami dan menyesuaikan solusi yang diberikan Gemini pada struktur project saya. Selain itu, saya juga melakukan eksplorasi mandiri melalui GitHub dan sumber dokumentasi lain.

- **Bagian spesifik yang dibantu:**

1. Implementasi fitur *update data* pada Django
2. Penggunaan `ModelForm` untuk update data
3. Pengaturan `DecimalField` untuk input GPA pada sectio education, termasuk `max_digits` dan `decimal_places`
4. Penggunaan `NumberInput` dan pengaturan `attrs` pada form.
5. Pemahaman mengenai pembagian validasi antara model dan form
6. Pemahaman mengenai kondisi branch yang tertinggal dari main dan cara sinkronisasi branch dengan main
7. Saran mengenai penggunaan Git command seperti `git fetch`, `git merge`, dan `git push`.

- **Keterbatasan AI & Perbaikan Mandiri:**

1. Beberapa saran yang diberikan oleh Generative AI perlu disesuaikan dengan struktur model, form, dan kode yang telah saya buat. Oleh karena itu, saya tidak semata-mata menggunakan seluruh kode atau solusi yang diberikan.
2. Untuk konsultasi GitHub, Generative AI memberikan beberapa alternatif penyelesaian. Namun, saya tetap melakukan pengecekan pada kondisi *branch* dan *repository* yang saya miliki sebelum menjalankan *command* yang diberikan.
3. Saya melakukan pengujian secara mandiri untuk memastikan implementasi Django dan perubahan pada *branch* dapat berjalan sesuai dengan kebutuhan *project*.
