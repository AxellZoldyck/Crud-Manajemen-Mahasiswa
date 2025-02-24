### CRUD Sistem Manajemen Siswa ###

import sqlite3

DB_NAME = "kampus.db"

def get_db_connection():
    """Membuat koneksi ke database SQLite"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn 

def create_table():
    """Membuat Table Mahasiswa Jika Belum Ada"""
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

def tambah_mahasiswa():
    """Menambahkan Mahasiswa Baru"""
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (?, ?, ?)", (nama, nim, jurusan))
        conn.commit()
        print("Mahasiswa Berhasil Ditambahkan!")
    except sqlite3.IntegrityError:
        print("Nim sudah ada! Gunakan NIM lain.")
        conn.close()

def lihat_mahasiswa():
    """Menampilkan Semua Mahasiswa"""
    conn = get_db_connection()
    mahasiswa = conn.execute("SELECT * FROM mahasiswa").fetchall()
    conn.close()

    if not mahasiswa:
        print("Belum ada mahasiswa dalam database.")
        return
    
    print("\n=== DAFTAR MAHASISWA ===")
    for mhs in mahasiswa:
        print(f"ID: {mhs['id']}, Nama: {mhs['nama']}, NIM: {mhs['nim']}, Jurusan: {mhs['jurusan']}")
    print("==============================")

def cari_mahasiswa():
    """Mencari Mahasiswa Berdasarkan NIM"""
    nim = input("Masukkan NIM: ")
    conn = get_db_connection()
    mahasiswa = conn.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim,)).fetchone()
    conn.close()

    if mahasiswa:
        print("\n=== DATA MAHASISWA ===")
        print(f"Nama: {mahasiswa['nama']}")
        print(f"NIM: {mahasiswa['nim']}")
        print(f"Jurusan: {mahasiswa['jurusan']}")
        print("==============================")
    else:
        print("Mahasiswa Tidak Ditemukan!")

def update_mahasiswa():
    """Mengupdate Data Mahasiswa"""
    nim = input("Masukkan NIM mahasiswa yang akan diperbarui: ")
    conn = get_db_connection()
    mahasiswa = conn.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim,)).fetchone()

    if not mahasiswa:
        print("Mahasiswa Tidak Ditemukan!")
        conn.close()
        return
    
    print("\n=== DATA MAHASISWA SEBELUM UPDATE ===")
    print("Nama: {mahasiswa[nama]}, Jurusan: {mahasiswa[jurusan]}")

    nama_baru = input("Masukkan Nama Baru: ") or mahasiswa["nama"]
    jurusan_baru = input("Masukkan Jurusan Baru: ") or mahasiswa["jurusan"]

    conn.execute("UPDATE mahasiswa SET nama = ?, jurusan = ? WHERE nim = ?", (nama_baru, jurusan_baru, nim))
    conn.commit()
    conn.close()
    print("Data Mahasiswa Berhasil Diperbarui!")

def hapus_mahasiswa():
    """Menghapus Mahasiswa Berdasarkan NIM"""
    nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
    conn = get_db_connection()
    cursor = conn.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim))
    conn.commit()
    conn.close()

    if cursor.rowcount:
        print("Mahasiswa Berhasil Dihapus!")
    else:
        print("Mahasiswa Tidak Ditemukan!")

def main():
    """Menjalankan Menu Interaktif"""
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

if __name__== "__main__":
    main()
    
