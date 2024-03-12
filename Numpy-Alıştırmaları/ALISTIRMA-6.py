"""

SORU: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
almaktadır. Zip kullanarak ders bilgilerini bastırınız

"""

Ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
Kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kredisi,kod,kont in zip(Kredi,Ders_kodu,kontenjan):
    print(f"kredisi {kredisi} olan {kod} kodlu dersin kontenjanı {kont} kişidir.")


"""

zip() fonksiyonu, iki veya daha fazla iterable'ı birleştirerek eşleşen elemanlardan oluşan
bir tuple serisi oluşturan bir built-in fonksiyondur. yani bize demetleri, listeleri, sözlükleri vs. eşleştirmemizi sağlar.
hepsi karşılığına göre davranır. 1. index eşleştirilen diğer listeden 1. indexle eşlenir

"""