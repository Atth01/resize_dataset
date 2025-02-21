import cv2
import os

# Folder input dan output
input_folder = "gambar"  # Folder yang berisi gambar-gambar
output_folder = "hasil_resize"  # Folder untuk menyimpan hasil resize

# Pastikan folder output ada
os.makedirs(output_folder, exist_ok=True)

# Ambil semua file dalam folder input
file_list = os.listdir(input_folder)

# Filter hanya file gambar (ekstensi umum: jpg, jpeg, png)
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp")  # Bisa ditambah jika perlu
image_files = [f for f in file_list if f.lower().endswith(valid_extensions)]

# Jika tidak ada gambar, tampilkan pesan
if not image_files:
    print(f"❌ Tidak ada gambar dalam folder '{input_folder}'.")
else:
    print(f"📂 Ditemukan {len(image_files)} gambar dalam '{input_folder}', memproses...")

    # Loop melalui semua gambar dalam folder
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Baca gambar
        img = cv2.imread(input_path)

        if img is None:
            print(f"❌ Gagal membaca {filename}, mungkin format tidak didukung.")
            continue

        print(f"✅ Memproses {filename} - Ukuran Asli: {img.shape}")

        # Resize ke ukuran yang diinginkan
        new_size = (512, 512)  # Ubah ukuran sesuai kebutuhan
        resized_img = cv2.resize(img, new_size)

        # Simpan hasil resize
        success = cv2.imwrite(output_path, resized_img)

        if success:
            print(f"✅ {filename} telah diresize dan disimpan ke '{output_folder}'")
        else:
            print(f"❌ Gagal menyimpan {filename}, cek izin folder atau format file.")

    print(f"🎉 Proses selesai! Semua gambar telah diresize dan disimpan di '{output_folder}'")
