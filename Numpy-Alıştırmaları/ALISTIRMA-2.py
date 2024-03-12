"""
SORU: Verilen listeye aşağıdaki adımları uygulayınız

adım 1: verilen listenin eleman sayısına bakınız
adım 2: Sıfırıncı ve onuncu insdexteki elemanları çağırınız
adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturunuz
adım 4: Sekizinci indeksteki elemanı siliniz.
adım 5: Yeni bir eleman ekleyiniz.
adım 6: Sekizinci indekse "N" elemanı tekrar ekleyiniz.

Verilen liste = "lst"

"""

lst = ["D","A","T","A","S","C","I","E","N","C","E"]


################################

adım1 = len(lst)
print(adım1)

################################

# İlk indeksteki elemanı çağır
adım2 = ilk_eleman = lst[0]

# Onuncu indeksteki elemanı çağır
onuncu_eleman = lst[10]

print("0. indeksteki eleman:", ilk_eleman)
print("10. indeksteki eleman:", onuncu_eleman)

################################

adım3 = yeni_lst = lst[:4]
print(yeni_lst)

################################
#adım4

del lst[8]
print(lst)

################################

adım5 = lst.append("BAKİ")
print(lst)

################################

tekrar_tanimla = ["D","A","T","A","S","C","I","E","N","C","E"]
tekrar_tanimla.insert(8,"N") #tekrar tanımladıktan sonra listeye insert metodunu kullanarak ilk parametreye hangi indekse istediğimiz ikinci parametreye de ne koyacağımızı yazıyoruz.

print(tekrar_tanimla)

#################################

