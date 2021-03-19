# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:55:38 2021

@author: Manish Kumar Goswami

"""
from difflib import get_close_matches

import json

data = json.load(open("data.json")) 

def trans(output):
    if output.lower() in data:
        return data[output.lower()]
    
    elif output.title() in data:
        return data[output.title()]
    
    elif output.upper() in data:
        return data[output.upper()]
    
    elif len(get_close_matches(output, data.keys()))> 0:
        
        print("Did you want %s word to search"%get_close_matches(output, data.keys())[0])
        
        decide = input("Press Y for yes N for no")
        
        if decide.lower() == "y":
            
            return data[get_close_matches(output, data.keys())[0]]
        
        elif decide.lower() == "n":
            
            print("This word is not in my dictonery Google it")
            
        else:
            
            print("You have enter wrong input")
            
    else:
        
        print("This word is not in my dictonery Google it")

output = input("Enter any word to search")

word = trans(output)

if type(word) == list:
    
    for item in word:
        
        print(item)

else:
    
    print(word)
    
    
    
    
    



