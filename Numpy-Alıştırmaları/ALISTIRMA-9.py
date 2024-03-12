"""

Question: Write a program that will give you the sum of 3 digits

---------------------------------------------------------------

Soru: 3 rakamın toplamını verecek programı yazınız.

"""

sayi = int(input("Number: "))

a = sayi%10 #sayinin 10 a bölümünden kalanı alıyoruz birler basamağı için
num = sayi // 10
b = num % 10
c = num // 10

print(a+b+c)