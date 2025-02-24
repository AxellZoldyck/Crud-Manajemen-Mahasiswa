
---

# CRUD Sistem Manajemen Mahasiswa

Sistem Manajemen Mahasiswa berbasis SQLite ini memungkinkan pengguna untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data mahasiswa dalam sebuah database. Program ini mendukung operasi penambahan mahasiswa, menampilkan data mahasiswa, pencarian mahasiswa berdasarkan NIM, serta pembaruan dan penghapusan data mahasiswa.

## Fitur
- **Tambah Mahasiswa**: Menambahkan mahasiswa baru ke dalam database dengan memasukkan nama, NIM, dan jurusan.
- **Lihat Semua Mahasiswa**: Menampilkan daftar semua mahasiswa yang ada dalam database.
- **Cari Mahasiswa**: Mencari data mahasiswa berdasarkan NIM.
- **Update Mahasiswa**: Memperbarui data mahasiswa berdasarkan NIM (nama dan jurusan).
- **Hapus Mahasiswa**: Menghapus mahasiswa berdasarkan NIM.

## Teknologi
- **Python**: Bahasa pemrograman yang digunakan untuk sistem ini.
- **SQLite**: Sistem manajemen basis data relasional yang digunakan untuk menyimpan data mahasiswa.

## Persyaratan
- Python 3.x
- Modul `sqlite3` (modul ini sudah termasuk dalam distribusi Python standar).

## Instalasi
1. Pastikan Python 3.x sudah terpasang di komputer Anda.
2. Unduh atau salin kode ini ke dalam file Python, misalnya `sistem_mahasiswa.py`.
3. Jalankan program menggunakan terminal atau command prompt dengan mengetikkan:
   ```
   python sistem_mahasiswa.py
   ```

## Struktur Kode

### 1. **Fungsi `get_db_connection()`**
   Fungsi ini digunakan untuk membuat koneksi ke database SQLite `kampus.db`.

   ```python
   def get_db_connection():
       conn = sqlite3.connect(DB_NAME)
       conn.row_factory = sqlite3.Row
       return conn
   ```

### 2. **Fungsi `create_table()`**
   Fungsi ini akan memeriksa dan membuat tabel `mahasiswa` jika belum ada dalam database.

   ```python
   def create_table():
       conn = get_db_connection()
       conn.execute("""
           CREATE TABLE IF NOT EXISTS mahasiswa (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nama TEXT,
               nim TEXT,
               jurusan TEXT
           )
       """)
       conn.commit()
       conn.close()
   ```

### 3. **Fungsi `tambah_mahasiswa()`**
   Fungsi ini memungkinkan pengguna untuk menambahkan mahasiswa baru ke dalam database dengan memasukkan nama, NIM, dan jurusan.

   ```python
   def tambah_mahasiswa():
       nama = input("Masukkan Nama: ")
       nim = input("Masukkan NIM: ")
       jurusan = input("Masukkan Jurusan: ")
       conn = get_db_connection()
       conn.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (?, ?, ?)", (nama, nim, jurusan))
       conn.commit()
       conn.close()
       print("Mahasiswa Berhasil Ditambahkan!")
   ```

### 4. **Fungsi `lihat_mahasiswa()`**
   Fungsi ini akan menampilkan daftar semua mahasiswa yang ada di dalam database.

   ```python
   def lihat_mahasiswa():
       conn = get_db_connection()
       mahasiswa = conn.execute("SELECT * FROM mahasiswa").fetchall()
       conn.close()
       if not mahasiswa:
           print("Belum ada mahasiswa dalam database.")
           return
       print("\n=== DAFTAR MAHASISWA ===")
       for mhs in mahasiswa:
           print(f"ID: {mhs['id']}, Nama: {mhs['nama']}, NIM: {mhs['nim']}, Jurusan: {mhs['jurusan']}")
   ```

### 5. **Fungsi `cari_mahasiswa()`**
   Fungsi ini memungkinkan pencarian data mahasiswa berdasarkan NIM.

   ```python
   def cari_mahasiswa():
       nim = input("Masukkan NIM: ")
       conn = get_db_connection()
       mahasiswa = conn.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim,)).fetchone()
       conn.close()
       if mahasiswa:
           print(f"Nama: {mahasiswa['nama']}")
           print(f"NIM: {mahasiswa['nim']}")
           print(f"Jurusan: {mahasiswa['jurusan']}")
       else:
           print("Mahasiswa Tidak Ditemukan!")
   ```

### 6. **Fungsi `update_mahasiswa()`**
   Fungsi ini memungkinkan pembaruan data mahasiswa berdasarkan NIM.

   ```python
   def update_mahasiswa():
       nim = input("Masukkan NIM mahasiswa yang akan diperbarui: ")
       conn = get_db_connection()
       mahasiswa = conn.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim,)).fetchone()
       if not mahasiswa:
           print("Mahasiswa Tidak Ditemukan!")
           conn.close()
           return
       nama_baru = input("Masukkan Nama Baru: ") or mahasiswa["nama"]
       jurusan_baru = input("Masukkan Jurusan Baru: ") or mahasiswa["jurusan"]
       conn.execute("UPDATE mahasiswa SET nama = ?, jurusan = ? WHERE nim = ?", (nama_baru, jurusan_baru, nim))
       conn.commit()
       conn.close()
       print("Data Mahasiswa Berhasil Diperbarui!")
   ```

### 7. **Fungsi `hapus_mahasiswa()`**
   Fungsi ini digunakan untuk menghapus mahasiswa berdasarkan NIM.

   ```python
   def hapus_mahasiswa():
       nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
       conn = get_db_connection()
       cursor = conn.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
       conn.commit()
       conn.close()
       if cursor.rowcount:
           print("Mahasiswa Berhasil Dihapus!")
       else:
           print("Mahasiswa Tidak Ditemukan!")
   ```

### 8. **Fungsi `main()`**
   Fungsi ini menjalankan menu interaktif untuk sistem manajemen mahasiswa.

   ```python
   def main():
       create_table()
       while True:
           print("\n=== SISTEM MANAJEMEN MAHASISWA ===")
           print("1. Tambah Mahasiswa")
           print("2. Lihat Semua Mahasiswa")
           print("3. Cari Mahasiswa")
           print("4. Update Mahasiswa")
           print("5. Hapus Mahasiswa")
           print("6. Keluar")
           pilihan = input("Pilih Menu (1-6): ")
           if pilihan == "1":
               tambah_mahasiswa()
           elif pilihan == "2":
               lihat_mahasiswa()
           elif pilihan == "3":
               cari_mahasiswa()
           elif pilihan == "4":
               update_mahasiswa()
           elif pilihan == "5":
               hapus_mahasiswa()
           elif pilihan == "6":
               print("Keluar Dari Program. Sampai Jumpa!")
               break
           else:
               print("Pilihan Tidak Valid! Silahkan Coba Lagi.")
   ```

## Cara Penggunaan

1. Setelah menjalankan program, pilih menu yang tersedia.
2. Masukkan data sesuai dengan opsi yang dipilih.
3. Program akan menampilkan pesan yang sesuai dengan operasi yang dilakukan (misalnya: mahasiswa berhasil ditambahkan, data ditemukan, dll).
4. Program akan terus berjalan sampai pengguna memilih opsi untuk keluar.

## Lisensi
MIT License

---
