
"""
SORU : Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

Adım 1: Key değerlerine erişiniz.
Adım 2: Value'lara erişiniz.
Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım 5: Antonio'yu dictionary'den siliniz.


Verilen sözlük yapısı = "dict"

"""

dict ={'Christian': ["America", 18],
       'Daisy':["England", 12],
       'Antonio': ["Spain", 22],
       'Dante': ["Italy", 25]}

#################################

adım1 = dict.keys()
print(adım1)

#################################

adım2 = dict.values()
print(adım2)


#################################

dict['Daisy'] = 13
print(dict)

#################################

eklemek_istediğimiz_değer = {'Ahmet':["Turkey", 24]}

dict.update(eklemek_istediğimiz_değer)
print(dict)

#################################

dict.pop('Antonio')
print(dict)

"""VEYA

del dict['Antonio']
print(dict)

"""