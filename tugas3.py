def hapus_spasi_berlebih(teks):
    return ' '.join(teks.split())

teks = input("Masukkan kalimat: ")

hasil = hapus_spasi_berlebih(teks)

print(f"Output: '{hasil}'")