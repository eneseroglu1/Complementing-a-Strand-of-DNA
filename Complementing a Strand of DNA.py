

def reversecomp(dna): # DNA parametresini veriyoruz.
  reversedna = dna[::-1] # dna[::-1] sondan başlayıp başa doğru yazdır diyoruz. Yani ters çeviriyoruz.
  complement = reversedna.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper() 
  # ters çevrilmiş DNA'da tamamlayıcıları yerine yazdırıyoruz. Upper komutuyla da harfleri büyütüyoruz 
  return complement 
  # Oluşan değeri döndürüyoruz. İlerde tekrardan bu fonksiyonu kullanabilmek bu komutu çağırabilmek için bunu yazıyoruz.
print("Çıktımız : "+reversecomp('AAAACCCGGT')) # Çıktıyı yazdırıyoruz.


