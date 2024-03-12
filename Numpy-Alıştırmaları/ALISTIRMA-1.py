"""
SORU: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Space yerine virgül koyunuz, kelime kelime ayırınız.

verilen string = "text"
"""

text = "The goal is to turn data into information, and information into insight"
list= [text]
text = list[0].upper()
words = [f'{word}' for word in text.split()]
son = ','.join(words)

print(words)