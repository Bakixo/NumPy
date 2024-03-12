"""

Question : Write a program to extract each digit from an integer in the reverse order 

For example, if the given int is 7536, the output shall be "6 3 5 7", with a space separating the digits

------------------------

Soru: Bir tamsayıdan her rakamı ters sırada çıkaran bir program yazın

Örneğin, verilen int 7536 ise, çıktı "6 3 5 7" olacak ve rakamlar arasında boşluk bırakılacaktır.

"""

srl =input("Number? :")

çevir = srl[::-1]

k = " ".join(çevir)

print(k)