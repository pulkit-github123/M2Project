from urllib import request
from xml.sax.saxutils import prepare_input_source
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import csv


# 1 FIND A FACTORIAL OF ANY GIVEN NUMBER USING POST METHOD
@api_view(['POST'])
def FindFactorial(request):
    number = int(request.POST.get('number'))
    factorial = 1
    for x in range(1, number+1):
        factorial = factorial * x
    return Response(factorial)

# 2 GET USERNAMES AND PASSWORDS FROM A FILE AND DISPLAY IT IN JSON FORMAT
@api_view(['GET'])
def GetData(request):
    file = open('M2App/M2Project.csv')
    csvreader = csv.reader(file, delimiter = ",")
    header = []
    header = next(csvreader)
    print("\n")
    print("CSV FILE HEADER IS AS BELOW:")
    print(header)
    print("\n")

    csv_data = []
    for x in csvreader:
        csv_data.append(x)
    print ("CSV FILE DATA IS AS BELOW:")
    print(csv_data)
    print("\n")

    json_data = json.dumps(csv_data)
    print ("SAME DATA IN JSON FORMAT IS AS BELOW:")
    file.close
    return Response(json_data)


# 3 CHECK THE FORMAT OF THE PASSWORD STRING:
@api_view(['POST'])
def checkStringFormat(request):
    string = request.POST.get('string')
    status = 'Invalid String'
    l, u, p, d = 0, 0, 0, 0
    if (len(string) >= 8):
        for letter in string:
            if (letter.islower()):
                l+=1
            if (letter.isupper()):
                u+=1
            if (letter.isdigit()):
                d+=1
            if (letter=="@" or letter=="$" or letter=="_"):
                p+=1
            print(l,u,p,d)
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(string)):
                print("Valid String")
                status = "Valid String"
            else:
                print("Invalid String")
                status = "Invalid String"
    return Response(status)


# 4 CHECK WHETHER THE GIVEN STRING EXIST IN THE FILE
@api_view(['GET'])
def checkString(request):
    input_string = request.GET.get('input_string')
    myfile = open('M2App/M2file.txt', 'a+')
    status = 'String does not exist'
    with open('M2App/M2file.txt') as myfile:
        if input_string in myfile.read():
            status = "The given string exists in the file"
        myfile.close()
    return Response(status)


# 5 DISSPLAY FACTORS OF GIVEN NUMBER
@api_view(['POST'])
def getFactors(request):
    number = int(request.POST.get('number'))
    factors = 1
    factor_list = []
    output_string = ''
    for x in range(1, number+1):
        y = number%x
        if y == 0:
            factor_list.append(x)
        else:
            continue
    output_string = ', '.join(str(x) for x in factor_list)
    return Response(output_string)

# 6 DISPLAY VOWELS IN A GIVEN STRING
@api_view(['POST'])
def displayVowels(request):
    input_string = request.POST.get('input_string')
    output_string = ''
    vowels = ["a", "e", "i", "o", "u", " "] #list of vowels AND a space
    temp_list = []

    for x in input_string:
        if (x in vowels):
            temp_list.append(x) #if a vowel OR a space is found then appending in the list as it is
        else:
            temp_list.append("_") #for everything else _ will be added in the list

    output_string = ' '.join(str(x) for x in temp_list) #converting the temp list into a string
    output_string = output_string.upper() #making everything as upper so that vowels are highlighted
    return Response(output_string)

"""
# 7 REMOVE THE REPEATING CHARACTER IN THE GIVEN STRING
@api_view(['POST'])
def removerepeatedchar(request):
    input_string = request.POST.get('input_string')
    input_string_lower = input_string.lower()
    final_list = []
    temp_list = []
    output_string = ''

    for x in input_string_lower:
        temp_list.append(x) #converitng the string into a list

    len_temp_list = len(temp_list)
    i = 0

    while i+1 < (len_temp_list): #running the checking loop uptill second last characters
        if temp_list[i] == temp_list[i+1]: #checking if two consecutive characters are same or not
            final_list.append("") #if yes then appending a null into a final list
        else:
            final_list.append(temp_list[i]) #else appending the character as-is into the final list
            i = i + 1

    final_list.append(temp_list[len_temp_list-1]) 
    #as the previous loop was only until second last character, appending the last character

    output_string = ''.join(str(x) for x in final_list) #converting the final list into a string
    output_string = output_string.capitalize() #just making the first letter of the string in Upper case
    return Response(output_string) #printing the output
"""

# 8 CONVERT THE DECIMAL NUMBER INTO BINARY
@api_view(['POST'])
def decimaltobinary(request):
    Number = int(request.POST.get('Number'))
    Quotient = Number//2 #First lets calculate the quotient
    FirstBit = Number%2 #Then calculate the Modulus 2, this will give the first bit
    BinaryList = [FirstBit,] #Define a list and put the firstbit as its first element
    BinaryString = '' # Define an emtpy string

    while Quotient >=1: #Entering into a loop
        bit = Quotient%2 #To keep on dividing the quotient mod 2 until it becomes >=1
        BinaryList.append(bit) #Append the result of quotient%2 into the list
        Quotient = Quotient//2 #Then again divide the quotient by 2 and repeat the mod 2 step

    BinaryListReverse = BinaryList[::-1] #Reversing the list, as the first element must be the last one when seen in binary form
    BinaryString = ' '.join(str(x) for x in BinaryListReverse) #Converting the list into string
    return Response(BinaryString)



# 9 CONVERT THE DECIMAL NUMBER INTO OCTA
@api_view(['POST'])
def decimaltoocta(request):
    Number = int(request.POST.get('Number'))
    Quotient = Number//8 #First lets calculate the quotient
    FirstBit = Number%8 #Then calculate the Modulus 8, this will give the first bit
    OctalList = [FirstBit,] #Define a list and put the firstbit as its first element
    OctalString = '' # Define an emtpy string

    while Quotient >= 1: #Entering into a loop
        oct = Quotient%8 #To keep on dividing the quotient mod 8 until it becomes >=1
        OctalList.append(oct) #Append the result of quotient%8 into the list
        Quotient = Quotient//8 #Then again divide the quotient by 8 and repeat the mod 8 step

    OctalListReverse = OctalList[::-1] 
    #Reversing the list, as the first element must be the last one when seen in binary form
    OctalString = ' '.join(str(x) for x in OctalListReverse) #Converting the list into string
    return Response(OctalString)



# 10 CONVERT THE DECIMAL NUMBER INTO HEXA
@api_view(['POST'])
def decimaltohexa(request):
    Number = int(request.POST.get('Number'))
    Quotient = Number//16 #First lets calculate the quotient
    FirstBit = Number%16 #Then calculate the Modulus 16, this will give the first bit
    HexaList = [FirstBit,] #Define a list and put the firstbit as its first element
    HexaString = '' # Define an emtpy string

    while Quotient >= 1: #Entering into a loop
        hex = Quotient%16 #To keep on dividing the quotient mod 16 until it becomes <1
        HexaList.append(hex) #Append the result of quotient%16 into the list
        Quotient = Quotient//16 #Then again divide the quotient by 16 and repeat the mod 8 step

    HexaListReverse = HexaList[::-1] 
    #Reversing the list, as the first element must be the last one when seen in binary form
    HexaString = ' '.join(str(x) for x in HexaListReverse) #Converting the list into string
    return Response(HexaString)  


# 7 REMOVE THE REPEATING CHARACTER IN THE GIVEN STRING
@api_view(['POST'])
def removerepeatedchar(request):
    input_string = request.POST.get('input_string')
    input_string = input_string.lower()
    output_list = []
    x = 0
    len = 0

    for char in input_string:
        output_list.append(char)
        len = len + 1

    while x <(len-1):
        if output_list[x] == output_list [x+1]:
            output_list[x] = ""
        x = x + 1

    output_string = ''.join(str(i) for i in output_list)
    output_string = output_string.capitalize()
    
    return Response(output_string)
    
