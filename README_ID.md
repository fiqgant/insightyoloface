# InsightYOLOFace

*Baca dalam [Bahasa Inggris](README.md)*

Repositori ini berisi skrip untuk deteksi wajah menggunakan YOLOv3 dan pengenalan wajah menggunakan InsightFace. Repositori ini juga mencakup skrip gabungan yang memanfaatkan YOLOv3 dan InsightFace untuk deteksi wajah.

## Daftar Isi
- [Gambaran Umum](#gambaran-umum)
- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
  - [Deteksi Wajah dengan YOLOv3](#deteksi-wajah-dengan-yolov3)
  - [Pengenalan Wajah dengan InsightFace](#pengenalan-wajah-dengan-insightface)
  - [Gabungan YOLOv3 dan InsightFace](#gabungan-yolov3-dan-insightface)
  - [Menentukan Sumber Video](#menentukan-sumber-video)
- [Instruksi Spesifik Platform](#instruksi-spesifik-platform)
  - [Windows](#windows)
  - [macOS (Apple)](#macos-apple)
  - [Linux](#linux)
- [Hasil](#hasil)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Gambaran Umum

Repositori ini menyediakan skrip Python berikut:

- **`yolov3.py`**: Mendeteksi wajah dalam video menggunakan model YOLOv3.
- **`insightface.py`**: Melakukan deteksi wajah menggunakan model InsightFace.
- **`combined.py`**: Menggabungkan YOLOv3 dan InsightFace untuk mendeteksi wajah menggunakan YOLOv3 dan InsightFace.

## Persyaratan

- Python 3.x
- OpenCV
- NumPy
- InsightFace

## Instalasi

1. **Clone repositori:**

    ```bash
    git clone https://github.com/fiqgant/arcyoloface.git
    cd arcyoloface
    ```

2. **Buat dan aktifkan lingkungan virtual (opsional tetapi direkomendasikan):**

    ### Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    ### macOS (Apple) dan Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instal paket Python yang diperlukan:**

    ```bash
    pip install -r requirements.txt
    ```

    Jika `requirements.txt` tidak tersedia, Anda dapat menginstal paket secara manual:

    ```bash
    pip install opencv-python numpy insightface
    ```

4. **Unduh model YOLOv3:**

    - Tempatkan bobot YOLOv3 (`yolov3-wider_16000.weights`) dan file konfigurasi (`yolov3-face.cfg`) di direktori `models`. Anda dapat mengunduhnya dari [sini](https://github.com/sthanhng/yoloface).

## Penggunaan

### Deteksi Wajah dengan YOLOv3

Skrip `yolov3.py` mendeteksi wajah dalam video menggunakan model YOLOv3.

1. **Jalankan skrip deteksi wajah YOLOv3:**

    ```bash
    python yolov3.py
    ```

2. **Output:**

    Skrip akan menampilkan video dengan wajah yang terdeteksi diberi tanda kotak hijau, bersama dengan skor kepercayaan (akurasi) untuk setiap wajah.

### Pengenalan Wajah dengan InsightFace

Skrip `insightface.py` melakukan deteksi dan pengenalan wajah menggunakan model InsightFace.

1. **Jalankan skrip pengenalan wajah InsightFace:**

    ```bash
    python insightface.py
    ```

2. **Output:**

    Skrip akan menampilkan video dengan wajah yang terdeteksi diberi tanda kotak biru. Untuk setiap wajah yang terdeteksi, akan ditampilkan skor akurasi.

### Gabungan YOLOv3 dan InsightFace

Skrip `combined.py` menggabungkan YOLOv3 dan InsightFace untuk mendeteksi wajah menggunakan YOLOv3 dan mengenali wajah menggunakan InsightFace.

1. **Jalankan skrip gabungan YOLOv3 dan InsightFace:**

    ```bash
    python combined.py
    ```

2. **Output:**

    Skrip akan menampilkan video dengan wajah yang terdeteksi oleh YOLOv3 dan InsightFace. Deteksi YOLOv3 ditandai dengan kotak hijau, sedangkan deteksi InsightFace ditandai dengan kotak biru. Akurasi setiap deteksi dan jumlah total wajah yang terdeteksi oleh masing-masing model akan ditampilkan.

### Menentukan Sumber Video

Anda dapat menentukan sumber video dalam skrip dengan mengedit baris `cap = cv2.VideoCapture()`. Berikut adalah contoh cara menggunakan berbagai sumber video:

#### 1. **Menggunakan File Video (misalnya, `video.mov`)**:

```python
cap = cv2.VideoCapture('video.mov')
```

Tempatkan file video di direktori yang sama dengan skrip Anda atau berikan path lengkapnya.

#### 2. **Menggunakan Webcam**:

```python
cap = cv2.VideoCapture(0)
```

Ini akan menggunakan webcam default pada sistem Anda. Jika Anda memiliki beberapa webcam, Anda dapat mengubah indeksnya (`0`, `1`, dll.) untuk memilih yang lain.

#### 3. **Menggunakan Stream CCTV (Kamera IP)**:

```python
cap = cv2.VideoCapture('rtsp://username:password@ip_address:port/stream')
```

Ganti `username`, `password`, `ip_address`, `port`, dan `stream` dengan nilai yang sesuai untuk kamera CCTV Anda.

- **Contoh**: Jika IP kamera Anda adalah `192.168.1.100`, portnya adalah `554`, dan path streamnya adalah `h264`, maka akan terlihat seperti ini:

  ```python
  cap = cv2.VideoCapture('rtsp://admin:12345@192.168.1.100:554/h264')
  ```

#### 4. **Mengatasi Kegagalan Sumber Video**:

Jika sumber video gagal dibuka (misalnya, file tidak ditemukan atau kamera tidak terhubung), skrip akan menampilkan pesan kesalahan dan keluar dengan baik:

```python
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()
```

## Instruksi Spesifik Platform

### Windows

1. **Instal Python 3.x**: Unduh dan instal Python dari [python.org](https://www.python.org/downloads/windows/).

2. **Instal Git**: Unduh dan instal Git dari [git-scm.com](https://git-scm.com/download/win).

3. **Instal OpenCV dan Dependensi Lainnya**: Instal paket Python yang diperlukan dengan mengikuti instruksi di atas.

4. **Jalankan Skrip**: Gunakan `cmd` atau PowerShell untuk menavigasi ke direktori proyek Anda dan jalankan skrip sesuai dengan bagian penggunaan.

### macOS (Apple)

1. **Instal Python 3.x**: Instal Python menggunakan Homebrew:

    ```bash
    brew install python
    ```

2. **Instal Git**: Git biasanya sudah terpasang di macOS. Jika tidak, instal menggunakan Homebrew:

    ```bash
    brew install git
    ```

3. **Instal OpenCV dan Dependensi Lainnya**: Ikuti langkah-langkah instalasi yang telah disediakan di atas.

4. **Jalankan Skrip**: Buka Terminal, navigasi ke direktori proyek Anda, dan jalankan skrip sesuai dengan bagian penggunaan.

### Linux

1. **Instal Python 3.x**: Python sering kali sudah terpasang. Jika tidak, instal menggunakan manajer paket Anda (misalnya, `apt` untuk Ubuntu/Debian):

    ```bash
    sudo apt-get install python3 python3-pip
    ```

2. **Instal Git**: Instal Git menggunakan manajer paket Anda:

    ```bash
    sudo apt-get install git
    ```

3. **Instal OpenCV dan Dependensi Lainnya**: Ikuti langkah-langkah instalasi yang telah disediakan di atas.

4. **Jalankan Skrip**: Gunakan Terminal untuk menavigasi ke direktori proyek Anda dan jalankan skrip sesuai dengan bagian penggunaan.

## Hasil

Anda dapat mengharapkan hasil berikut dari skrip:

- **YOLOv3**: Kotak hijau di sekitar wajah yang terdeteksi dengan skor kepercayaan.
- **InsightFace**: Kotak biru di sekitar wajah yang dikenali dengan skor akurasi.
- **Gabungan**: Baik kotak hijau maupun biru, menunjukkan deteksi YOLOv3 dan InsightFace.

## Kontribusi

Jika Anda memiliki perbaikan, perbaikan bug, atau fitur tambahan yang ingin Anda lihat, jangan ragu untuk me-*fork* repositori ini dan membuat *pull request*. Kontribusi selalu diterima!

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.