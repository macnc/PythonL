#! /usr/bin/python
# _*_coding: utf-8


stat_name = ['Alabama', "California", 'Oklahoma', 'Florida']
vowels = list('aeiou')
output = []

for stat in stat_name:
    stat_list = list(stat.lower())

    for vowel in vowels:
        while True:
            try:
                stat_list.remove(vowel)
            except:
                break
    output.append(''.join(stat_list).capitalize())

print(output)
