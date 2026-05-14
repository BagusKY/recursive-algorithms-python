# ♟️ Recursive Algorithms Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Algorithm](https://img.shields.io/badge/Algorithm-Recursion-green?style=for-the-badge)
![Backtracking](https://img.shields.io/badge/Technique-Backtracking-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### Project Visualisasi Algoritma Rekursif & Backtracking

Implementasi interaktif algoritma rekursif klasik menggunakan Python dengan visualisasi terminal, animasi, statistik proses, dan simulasi backtracking secara real-time.

</div>

---

# 📌 Tentang Project

Project ini berisi implementasi beberapa permasalahan klasik dalam ilmu komputer menggunakan teknik:

* Rekursi (Recursion)
* Backtracking
* Visualisasi Algoritma
* Simulasi Pencarian Solusi

Seluruh program dibuat menggunakan Python dan berjalan langsung di terminal/command prompt tanpa memerlukan library eksternal.

Tujuan utama project ini adalah:

* memahami konsep rekursi,
* mempelajari algoritma backtracking,
* memvisualisasikan proses pencarian solusi,
* meningkatkan logika pemrograman,
* dan membuat pembelajaran algoritma menjadi lebih menarik serta interaktif.

---

# 🚀 Daftar Program

## 1. ♛ N-Queens Visual Solver

Program ini menyelesaikan permasalahan N-Queens, yaitu menempatkan N ratu pada papan catur berukuran N×N tanpa ada ratu yang saling menyerang.

### ✨ Fitur

* Algoritma recursive backtracking
* Animasi proses solving
* Visualisasi papan catur
* Simulasi penempatan ratu
* Efek backtracking real-time
* Statistik proses solving
* Sistem replay interaktif
* Tampilan terminal modern

### 🖥️ Preview

```text
♛ · · ·
· · ♛ ·
· ♛ · ·
· · · ♛
```

---

## 2. ♞ Knight's Tour Visual Solver

Program ini menyelesaikan masalah Knight’s Tour, yaitu membuat kuda catur mengunjungi seluruh kotak papan tepat satu kali.

### ✨ Fitur

* Recursive backtracking solver
* Simulasi pergerakan kuda
* Animasi terminal interaktif
* Visualisasi langkah real-time
* Tracking posisi kuda
* Statistik performa algoritma
* Tampilan papan catur dinamis
* Sistem replay otomatis

### 🖥️ Preview

```text
 0  5 14  9 20
13  8 19  4 15
18  1  6 21 10
 7 12 23 16  3
24 17  2 11 22
```

---

## 3. 🎒 Advanced Knapsack Solver

Program ini menyelesaikan Knapsack Problem, yaitu mencari kombinasi barang terbaik tanpa melebihi target berat.

### ✨ Fitur

* Recursive subset searching
* Simulasi backtracking
* Visualisasi progress berat
* Interactive terminal interface
* Tracking solusi terbaik
* Statistik proses pencarian
* Progress bar kapasitas tas
* Animasi solving real-time

### 🖥️ Preview

```text
Selected Items:
Weight : 2
Weight : 5
Weight : 9
Weight : 14

Total Weight : 30
```

---

# 📂 Struktur Project

```text
recursive-algorithms-python/
│
├── README.md
├── n_queens.py
├── knights_tour.py
└── knapsack.py
```

---

# ⚙️ Kebutuhan Sistem

## Software

* Python 3.x
* Terminal / CMD / PowerShell

## Library

Tidak memerlukan library tambahan.

Semua program menggunakan module bawaan Python.

---

# ▶️ Cara Menjalankan Program

## 1. Clone Repository

```bash
git clone https://github.com/your-username/recursive-algorithms-python.git
```

---

## 2. Masuk ke Folder Project

```bash
cd recursive-algorithms-python
```

---

## 3. Jalankan Program

### Menjalankan N-Queens Solver

```bash
python n_queens.py
```

---

### Menjalankan Knight’s Tour Solver

```bash
python knights_tour.py
```

---

### Menjalankan Knapsack Solver

```bash
python knapsack.py
```

---

# 🧠 Konsep Algoritma

## 🔁 Rekursi (Recursion)

Rekursi adalah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri secara berulang sampai kondisi tertentu tercapai.

Contoh sederhana:

```python
def fungsi():
    fungsi()
```

Rekursi sering digunakan dalam:

* pencarian solusi,
* traversal data,
* algoritma matematika,
* dan backtracking.

---

## 🔄 Backtracking

Backtracking adalah teknik algoritma yang bekerja dengan cara:

1. mencoba sebuah kemungkinan,
2. mengecek apakah solusi valid,
3. lalu kembali (backtrack) jika solusi gagal.

Teknik ini sering digunakan dalam:

* Sudoku Solver
* Maze Solver
* Pathfinding
* N-Queens
* Knight’s Tour
* Permasalahan kombinasi

---

# 📊 Fitur Utama Program

| Fitur              | N-Queens | Knight’s Tour | Knapsack |
| ------------------ | -------- | ------------- | -------- |
| Algoritma Rekursif | ✅        | ✅             | ✅        |
| Backtracking       | ✅        | ✅             | ✅        |
| Animasi Terminal   | ✅        | ✅             | ✅        |
| Input Interaktif   | ✅        | ✅             | ✅        |
| Statistik Solving  | ✅        | ✅             | ✅        |
| Simulasi Visual    | ✅        | ✅             | ✅        |
| Replay System      | ✅        | ✅             | ✅        |

---

# 📈 Statistik yang Ditampilkan

Setiap program akan menampilkan:

* Total langkah rekursi
* Jumlah backtracking
* Waktu eksekusi
* Status solusi
* Kondisi papan saat ini
* Hasil solusi akhir
* Tracking proses solving

---

# 🎯 Tujuan Pembelajaran

Project ini dibuat untuk:

* memahami algoritma rekursif,
* mempelajari teknik backtracking,
* meningkatkan kemampuan problem solving,
* melatih logika pemrograman Python,
* dan memvisualisasikan algoritma kompleks secara interaktif.

---

# 💡 Ukuran Input yang Direkomendasikan

| Program       | Ukuran Aman |
| ------------- | ----------- |
| N-Queens      | 4 – 8       |
| Knight’s Tour | 5 – 6       |
| Knapsack      | 5 – 10 item |

Input yang terlalu besar dapat menyebabkan waktu eksekusi lebih lama karena algoritma backtracking mencoba sangat banyak kemungkinan solusi.

---

# 🖥️ Contoh Output Terminal

## ♛ N-Queens

```text
Placing Queen #4

♛ · · ·
· · ♛ ·
· ♛ · ·
· · · ♛

Solution Found Successfully!
```

---

## ♞ Knight’s Tour

```text
Current Move : 18
Knight Position : (2, 4)

0  5 14  9 20
13 8 19 4 15
18 1 6 21 10
```

---

## 🎒 Knapsack

```text
CURRENT BAG

Weight : 5
Weight : 9
Weight : 14

Capacity Usage : [##############------] 70%
```

---

# 🔥 Keunggulan Project

* Visualisasi algoritma secara real-time
* Tampilan terminal modern dan interaktif
* Simulasi backtracking yang jelas
* Struktur kode rapi dan mudah dipahami
* Cocok untuk pembelajaran algoritma
* Ringan dan mudah dijalankan
* Tidak membutuhkan library tambahan
* Friendly untuk pemula

---

# 👨‍💻 Author

Project ini dibuat sebagai implementasi algoritma rekursif dan backtracking menggunakan Python.

---

# ⭐ Kesimpulan

Project ini menunjukkan bagaimana algoritma rekursif dan backtracking dapat digunakan untuk menyelesaikan berbagai permasalahan kompleks melalui proses pencarian solusi secara sistematis.

Dengan pendekatan visual dan interaktif, proses pembelajaran algoritma menjadi lebih menarik, mudah dipahami, dan lebih menyenangkan untuk dipelajari.

---

<div align="center">

### Terima Kasih Sudah Mengunjungi Repository Ini

⭐ Jika project ini menarik, jangan lupa berikan star pada repository.

</div>
