# -*- coding: utf-8 -*-
import requests
import re

url = 'https://adventofcode.com/2020/day/1/input'
session_id = 'YOUR SESSION ID'
x = requests.get(url, cookies = {'session':session_id})

y = x.content.decode()
y = y.split('\n')

my_str_list = [e for e in y if e]
my_int_list = []

for value in my_str_list:
    my_int_list.append(int(value))

for val_1 in my_int_list:
    rem_1 = 2020 - val_1
    val_1_index = my_int_list.index(val_1)
    for val_2 in my_int_list[val_1_index+1:]:
        rem_2 = rem_1 - val_2
        val_2_index = my_int_list.index(val_2)
        if rem_2 in my_int_list[val_2_index+1:]:
            val_3 = rem_2
            print(val_1*val_2*val_3)