"""
SORU: Argüman olarak bir liste alan, listenin 
içerisindeki tek ve çift sayıları ayrı listelere atayan 
ve bu listeleri return eden bir fonksiyon yazınızı

argüman liste = "l"
"""

l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []

def func(lst):
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list
func(l)

print("Even List:", even_list)
print("Odd List:", odd_list)
