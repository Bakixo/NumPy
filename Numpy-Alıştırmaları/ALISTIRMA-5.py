"""
SORU: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de 
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız
"""

ogrenciler = ["ALİ", "VELİ","AYŞE","TALAT","ZEYNEP","ECE"]

for i,ogrenci in enumerate(ogrenciler):
    if i <= 2:
        print(f"Mühendislik fakültesi {i} . öğrenci {ogrenci}")
    else:
        print(f"Tıp fakültesi {i} . öğrenci {ogrenci}")
    

#enumerate hem index hem de öğrencileri gezme fırsatı veriyor.