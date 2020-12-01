# -*- coding: utf-8 -*-
import requests
import re


url = 'https://adventofcode.com/2020/day/1/input'
session_id = '53616c7465645f5fadff3dc6e4805c0dfcd534a83a396b4e2dbed0de878fc22c8df962a5c45769bbbf5c00a289ac7720'
x = requests.get(url, cookies = {'session':session_id})

y = x.content.decode()
y = y.split('\n')

my_str_list = [e for e in y if e]
my_int_list = []
my_remainders_list = []
my_solution_list = []

for value in my_str_list:
    my_int_list.append(int(value))
    

for val1 in my_int_list:
    remainder = 2020 - val1
    my_remainders_list.append(remainder)
    
    if remainder in my_int_list:
        my_solution_list.append(my_int_list[my_int_list.index(remainder)])
        print(my_int_list.index(remainder))
        
answer = my_solution_list[0] * my_solution_list[1]
print(answer)