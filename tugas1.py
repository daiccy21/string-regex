def is_anagram(word1, word2):
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    if len(word1) != len(word2):
        return False
    
    count = {}
    
    for char in word1:
        count[char] = count.get(char, 0) + 1
    
    for char in word2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    
    return True

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if is_anagram(kata1, kata2):
    print(f"{kata1} adalah anagram dari {kata2}.")
else:
    print(f"{kata1} bukan anagram dari {kata2}.")