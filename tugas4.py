def cari_kata_terpendek_terpanjang(teks):
    daftar_kata = teks.split()
    
    kata_terpendek = daftar_kata[0]
    kata_terpanjang = daftar_kata[0]
    
    for kata in daftar_kata:
        if len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        if len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
    
    return kata_terpendek, kata_terpanjang

teks = input("Masukkan kalimat: ")

terpendek, terpanjang = cari_kata_terpendek_terpanjang(teks)

print(f"Terpendek: {terpendek}, Terpanjang: {terpanjang}")