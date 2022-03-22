#!/usr/bin/env python
# coding: utf-8

# In[1]:


class RomanNumeral():

    def __init__(self, roman):
        self.roman = roman
        
    def convert_to_number(self):
        roman_dict = {'I': 1,'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_value = 0
        r = self.roman
        for i in range(len(r)):
            if i > 0 and roman_dict[r[i]] > roman_dict[r[i - 1]]:
                integer_value += roman_dict[r[i]] - 2*roman_dict[r[i-1]]
            else:
                integer_value += roman_dict[r[i]]
        return integer_value

##print the integer_value
