def hitung_frekuensi(teks, kata):
    teks = teks.lower()
    kata = kata.lower()
    
    for char in ['.', ',', '!', '?', ';', ':']:
        teks = teks.replace(char, ' ')
    
    daftar_kata = teks.split()
    
    frekuensi = daftar_kata.count(kata)
    
    return frekuensi

teks = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dihitung: ")

frekuensi = hitung_frekuensi(teks, kata)

print(f"Kata '{kata}' ada {frekuensi} buah.")