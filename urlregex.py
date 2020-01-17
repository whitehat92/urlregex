#!/usr/bin/python3
#usage: python3 regex.py '<yourexpression_to_be_analyzed>'


import re
import sys

expression = str(sys.argv[1])
#test = re.search(r''"=(.*?)(?:&|$)"'') #values of parameters
regex = '=(.*?)(?:&|$)'
result = re.search(regex,expression)
#return re.sub(r'(?s)<.*?>', '', html)


#match any character and ignore ? and =
#regex1 = '(.??)\w*(?=)'
regex1 = '(.??)\w*(?=)'
result1 = re.search(regex1, expression)

regex2 = '(\?|\&)([^=]+)\=([^&]+)' #other parameter to try
result2 = re.search(regex2, expression)

regex3 = '=[^&]+&*' #other from regex testing for the values only
result3 = re.findall(regex3, expression, re.DOTALL)

#regex4 = '.?.=+&*' # prints the variables or parameters
regex4 = '.?.=+&*'
result4 = re.findall(regex4, expression, re.DOTALL)

regex5 = '[\w]*\=' #match all the variables
result5 = re.findall(regex5, expression, re.DOTALL)

regex6 ='\=[*\w]*' #all values
result6 = re.findall(regex6, expression, re.DOTALL)

#printing parameters present in the url
    print("parameters present in the url: ", result5[0][:-1], result5[1][:-1],result5[2][:-1])
#printing the values present in the url
print("values present in the url: ", result6[0][1:],result6[1][1:],result6[2][1:])

#only equal sign to help identify how many of them are present in the url
equalsign = '='
equalsignex = re.findall(equalsign, expression, re.DOTALL)
print("number of equal signs in the expression is: ", len(equalsignex))
sys.exit()

