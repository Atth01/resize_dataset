# 🖼️ Image Resizer dengan OpenCV

Skrip Python ini digunakan untuk me-resize semua gambar di dalam folder tertentu dan menyimpannya ke folder lain dengan ukuran yang telah ditentukan (default: 512x512 pixel).

---

## 📦 Kebutuhan

- Python 3.x
- OpenCV (`opencv-python`)

Install dependensi dengan:

```bash
pip install -r requirements.txt

# Yang perlu diganti itu nama input foldernya diganti sama output foldernya boleh rubah namanya
# Input foldernya harus udah data gambar yang mau di resize, ini gambarnya di resize ke ukuran 512x512 piksel
input_folder = "kaps"  # Folder yang berisi gambar-gambar
output_folder = "kaps_resize"  # Folder untuk menyimpan hasil resize

# Instalasi
# extension yang dibutuhin itu tinggal ketika di terminal "pip install -r  requirements.txt" tinggal enter ntar dia langsung unduh extension yang dibutuhin

# Tahap - tahapnya resize:
# 1. Bisa buat folder dulu di dalam folder ini, nanti diisi gambar mentahnya
# 2. Udah gitu di skrip cek.py itu yang nama input folder yang "kaps" diganti sama nama folder yang dibuat
# 3. Output foldernya juga rubah
# 4. Udah gitu tinggal jalanin aja "python cek.py" nanti dia resize otomatis  
