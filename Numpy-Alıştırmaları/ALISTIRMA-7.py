"""

SORU: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir

"""

kume1 =set(["Data","Python"])     
kume2 =set(["Data","Function","qcut","lambda","Python","miuul"])

result = kume2.issuperset(kume1)
if result == True:
    dif_set = kume2.difference(kume1)
    print(dif_set)