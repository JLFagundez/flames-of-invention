# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:01:33 2023

@author: jeanl
"""

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_average(numbers)
print("The average is:", result)

# O erro proposital está abaixo, tente identificá-lo!
random_variable = 10
result = calculate_average(random_variable)
print("The average is:", result)