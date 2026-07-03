#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:36:13 2026

@author: jdk
"""

# Esercizi sulle stringhe

my_string = 'Oggi è una bella giornata!!!'

print(my_string)
print(type(my_string))

print(my_string[0])
print(my_string[1])
print(my_string[-1])

print(my_string[3:5])
print(my_string[:-2])

my_string = 'Cu' + my_string[1:]
print(my_string)

print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())

my_string2 = "Oggi è una splendida giornata per studiare NLP"
new_my_string2_list = my_string2.split()
print(new_my_string2_list)
print(type(new_my_string2_list))
list_to_string = " ".join(new_my_string2_list)
print(list_to_string)

sentence = "La penna è sul tavolo. Il gatto è sulla sedia. Il cane è in giardino."
sent_split = sentence.split('.')
print(sent_split)

tot = sentence.count('è')
print(tot)
new_sentence = sentence.replace('. I',' e i')
print(new_sentence)

sentence_without_o = sentence.replace('o', '')
print(sentence_without_o)

print('La parola penna è in posizione: ', sentence.find('penna')) #Restituisce l'incice della prima occorrenza

start_idx = sentence.find('Il')
sentence = sentence[start_idx:]
print(sentence)
end_idx = sentence.find('.')
sentence = sentence[:end_idx]
print(sentence)

#Se find non trova nulla, restituisce -1

s1 = "Tanto va la gatta al lardo che ci lascia lo zampino."
print(s1.find('l'))
print(s1.rfind('l'))

test_strip = "   Questo è un test!  "
print(test_strip.strip())
print(test_strip.lstrip())
print(test_strip.rstrip())









