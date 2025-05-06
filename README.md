# Seberapa IF Kamu?

Filter kuis interaktif berbasis Python untuk menguji seberapa paham kamu dengan dasar-dasar informatika. Program ini bekerja seperti filter TikTok dengan pertanyaan yang muncul acak dan dijawab melalui gerakan kepala (kiri/kanan) menggunakan webcam.

## 👨‍💻 Anggota
- Nama: [Nama Lengkap]
- NIM: [NIM Mahasiswa]
- GitHub: [github.com/username]

## 🚀 Cara Instalasi

1. Clone repositori ini:
```bash
git clone https://github.com/username/seberapa-if-kamu.git
cd seberapa-if-kamu
```

2. Buat dan aktifkan virtual environment (opsional tapi disarankan):
```bash
python -m venv venv
source venv/bin/activate  # untuk Linux/macOS
venv\Scripts\activate   # untuk Windows
```

3. Instal dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Cara Menjalankan Program

```bash
python main.py
```

Program akan menggunakan webcam, menampilkan pertanyaan, dan mendeteksi gerakan kepala untuk menjawab. Skor akan ditampilkan di akhir sesi.

## 📁 Struktur Folder

```
seberapa-if-kamu/
├── main.py
├── quiz_logic.py
├── head_tracker.py
├── requirements.txt
├── README.md
└── assets/
    └── soal.json
```

## 📚 Referensi
- OpenCV Documentation: https://docs.opencv.org/
- Effect House TikTok: https://effecthouse.tiktok.com/learn/

## 📝 Logbook
- Minggu 1: Ide dan perencanaan filter
- Minggu 2: Pembuatan logic kuis dan deteksi gerakan kepala
- Minggu 3: Integrasi dan pengetesan
- Minggu 4: Finalisasi dan dokumentasi

## ⚠️ Catatan
Pastikan kamera sudah terdeteksi sebelum menjalankan program. Gerakkan kepala ke **kiri (A)** atau **kanan (B)** untuk memilih jawaban.