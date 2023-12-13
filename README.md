# UAS-PBO

NAMA KELOMPOK:
1. Julia Dwi Azizah (G1F022009)
2. Thesa Febriani (G1F022033)
3. Selma Mulkya Nisa (G1F022055)



## Penjelasan kode

  <img width="587" alt="Cuplikan layar 2023-12-13 174902" src="https://github.com/ThesaFebriani/UAS_PBO_KEL/assets/147154548/a18949f6-a4b8-4f92-8486-f6c581b65057">

  
  Penjelasan:

  Kode diatas merupakan potongan kode program untuk menerjemahkan DNA ke RNA dan Protein. Dalam program ini kami  menggunakan dua buah kelas yaitu kelas DNATranslator dan kelas DNAConverteraap. Kode diatas merupakan kode dari bagian kelas DNATranslator. Kelas ini bertanggung jawab untuk melakukan translasi urutan DNA ke urutan RNA dan kemudian ke urutan asam amino (protein). Metode-metodenya (transcribe_to_rna dan translate_to_protein) mengimplementasikan logika untuk mengonversi urutan DNA menjadi urutan RNA dan kemudian menerjemahkannya ke urutan asam amino dengan bantuan tabel kodon.
  
  Kemudian di kelas ini terdapat atribut yaitu tabel kodon atau "CODON_TABLE" yang merupakan sebuah dictionary yang digunakan untuk mencocokkan kodon RNA dengan asam amino yang sesuai. Dalam kode diatas , CODON_TABLE adalah sebuah variabel kelas yang dapat diakses oleh semua instance dari kelas DNATranslator. def __init__(self, dna_sequence): adalah konstruktor kelas (__init__). Ketika objek dari kelas DNATranslator dibuat, metode ini akan dijalankan. Parameter dna_sequence adalah urutan DNA yang akan disimpan di dalam objek sebagai atribut dna_sequence. Fungsi upper() dipanggil pada urutan DNA ini untuk memastikan bahwa urutan DNA disimpan dalam huruf kapital. def transcribe_to_rna(self): Metode ini mengambil urutan DNA yang disimpan dalam objek (yang telah diubah menjadi huruf kapital) dan mengganti setiap timin (T) dengan urasil (U), sehingga menerjemahkan urutan DNA menjadi urutan RNA.

  Kemudian terdapat method def translate_to_protein(self): untuk mentraslasikan rna menjadi protein. rna_sequence = self.transcribe_to_rna(): Metode transcribe_to_rna dipanggil untuk mengonversi urutan DNA ke urutan RNA. Urutan RNA yang dihasilkan disimpan dalam variabel rna_sequence. Kemudian menambahkan variabel kosong yang akan digunakan untuk menyimpan urutan protein yang dihasilkan.

  for i in range(0, len(rna_sequence), 3): merupakan perulangan RNA dengan langkah sebesar 3 (karena dalam kode genetik, kodon memiliki panjang 3 nukleotida). 
  codon = rna_sequence[i:i + 3]: Membuat potongan dari urutan RNA yang merupakan sebuah kodon, dengan panjang 3 nukleotida. if len(codon) == 3: berfungsi untuk memeriksa apakah potongan yang diambil benar-benar merupakan kodon yang lengkap. protein_sequence += self.CODON_TABLE.get(codon, 'X'):  berguna untuk mencari kodon dalam CODON_TABLE yang telah didefinisikan sebelumnya di kelas DNATranslator. Jika kodon ditemukan, asam amino yang sesuai ditambahkan ke protein_sequence. Jika tidak ditemukan, 'X' (maksudnya kodon yang tidak diketahui) ditambahkan sebagai penanda kodon yang tidak dikenal. return protein_sequence: Mengembalikan urutan asam amino yang dihasilkan setelah semua kodon diurutkan.


  <img width="575" alt="Cuplikan layar 2023-12-13 175045" src="https://github.com/ThesaFebriani/UAS_PBO_KEL/assets/147154548/a4065ab9-e60f-40fd-ba04-370a0d6b8442">

  
  Penjelasan:

  Gambar diatas merupakan kode untuk mengatur antar muka atau GUI dari program ini. Dimana terdapat sebuah kelas yang bernama DNAConverterapp, kelas ini menggunakan tkinter untuk membuat antarmuka pengguna grafis atau GUI, untuk engatur elemen-elemen GUI seperti label, entry , tombol terjemahan, dan area teks untuk menampilkan hasil terjemahan. Metode translate_sequence digunakan untuk mengambil input dari pengguna, menggunakan objek DNATranslator untuk menerjemahkan input, dan menampilkan hasilnya di area teks.

  Method __init__: Ini adalah konstruktor kelas yang dipanggil saat objek dari kelas DNAConverterApp dibuat. Method translate_sequence:  dipanggil saat tombol "Terjemahkan" ditekan yang akan mengambil urutan DNA dari input, membuat objek DNATranslator untuk menerjemahkan urutan tersebut ke urutan RNA dan protein, dan kemudian menampilkan hasilnya di area teks.

  def __init__(self, root): adalah konstruktor kelas DNAConverterApp. Method ini dipanggil saat objek dari kelas dibuat. Parameter root adalah referensi ke objek Tk dari Tkinter, yang menjadi elemen utama dari GUI. self.root = root: adalah inisialisasi atribut root dari objek DNAConverterApp, yang menyimpan referensi ke objek Tk yang diberikan saat objek DNAConverterApp dibuat. self.root.title("Penerjemah DNA"): Mengatur judul jendela aplikasi menjadi "Penerjemah DNA". self.label = tk.Label(root, text="Masukkan Urutan DNA:"): Membuat label dengan teks "Masukkan Urutan DNA:" yang akan ditampilkan di jendela aplikasi. self.label.pack(): Menempatkan label ke dalam jendela aplikasi menggunakan metode pack() dari Tkinter, yang mengatur tata letak elemen-elemen dalam GUI. self.entry = tk.Entry(root): Membuat elemen Entry yang merupakan kotak input untuk pengguna memasukkan urutan DNA. self.entry.pack(): Menempatkan kotak input ke dalam jendela aplikasi menggunakan metode pack().


  <img width="307" alt="image" src="https://github.com/ThesaFebriani/UAS_PBO_KEL/assets/147154548/afe03354-07ec-4f6a-aff8-889c0e96d34c">

  Penjelasan:

  Gambar diatas merupakan tampilan hasil dari program yang kami buat, dimana kita bisa mengubah DNA menjadi RNA, kemudian diubah menjadi protein. 


  



