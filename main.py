import string

def sezar_sifreleme(metin, anahtar):
  alfabe = string.ascii_uppercase + string.ascii_lowercase
  şifreli_metin = ""
  for karakter in metin:
    if karakter in alfabe:
      yeni_karakter = alfabe[(alfabe.index(karakter) + anahtar) % len(alfabe)]
      şifreli_metin += yeni_karakter
    else:
      şifreli_metin += karakter
  return şifreli_metin

def sezar_sifre_cozme(metin, anahtar):
  alfabe = string.ascii_uppercase + string.ascii_lowercase
  açık_metin = ""
  for karakter in metin:
    if karakter in alfabe:
      yeni_karakter = alfabe[(alfabe.index(karakter) - anahtar) % len(alfabe)]
      açık_metin += yeni_karakter
    else:
      açık_metin += karakter
  return açık_metin

metin = input("Metin Girin: ")
anahtar = 3

şifreli_metin = sezar_sifreleme(metin, anahtar)
print("Şifreli metin:", şifreli_metin)

açık_metin = sezar_sifre_cozme(şifreli_metin, anahtar)
print("Açık metin:", açık_metin)
