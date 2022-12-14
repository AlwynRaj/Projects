# -*- coding: utf-8 -*-
"""SSCD Ex 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YH3GxmgtngJpSNM17FFHKhKs22Ccx96U
"""

# Variables needed for the program 
l = []
linecount = 0
dtype ='-'
Datatype = []
Identifier = []
Value = []
ReturnType = []
Arguments = []
flag = False
FunReturnType =[]
FunIdentifier =[]
FunArguments=[]

# Get Program from the user.
while True:
  try:
    l.append(input())
  except:
    break

# l= ['int x , y = 10 ; ', "char c = 'z' ;", 'int func (int,int) ;']

# Tokenizer Function 
def tokizer(x):
  Token = []
  for i in x:
    Temp = i.split()
    for j in Temp:
      Token.append(j)
  return Token

# Appender Function
def appender(dtype,identi,value):
  Datatype.append(dtype)
  Identifier.append(identi)
  Value.append(value)

# Printer function to Print the Table 
def printer():
  from prettytable import PrettyTable # To Tabulate the data 
  mytable = PrettyTable(["Data Type","Return Type", "Identifier", "Value","Arguments "])
  for i in range(len(Datatype)):
    mytable.add_row([Datatype[i],'---',Identifier[i],Value[i],'---'])
  for i in range(len(FunReturnType)):
    mytable.add_row(['---',FunReturnType[i],FunIdentifier[i],'---',FunArguments[i]])
  print(mytable)

# The Loop That Divides and appends the data to appropriate lists
Token = tokizer(l)
for i in Token :
  if i in ['int','float','double','char']: # when we encounter a Dtype store in dtype var
    dtype = i
    continue
  elif i.startswith("'") and i.endswith("'") or i.startswith('(') and i.endswith(')'): # when the token has '' or () mark it with a flag 
      tempstring = i
      flag = True
      continue
  elif i.isidentifier(): # uses isidentifier func to check
    id = i
  elif i in [',']:
    if id in Identifier: 
         continue
    else:
      appender(dtype,id,0) # append using function, 0 because we encounted , in line example int x , y = 10 here x = 0 and y = 10 
    continue
  elif i in ['=']:   # ignore equal to Should change this logic to work differently this should be smarter 
    continue        
  elif i.isnumeric():  # checking for constants to append to the correct id 
     value = i
     continue
  elif i in [';']: # ';' denotes the end of the line and hence all the values that need to be scanned are done . so we can append and move on to next line
     linecount+=1 
     if (flag):
       if id in Identifier: 
         continue
       else:
         appender(dtype,id,tempstring)
     else:
       if id in Identifier: 
          continue
       else:
          appender(dtype,id,value)
  else:   # line counter to print the line number in case of errors
    print('Error in line',linecount,'in',i)

for i in range(len(Value)) : # initially the values were appened to the Datatype, Identifier and value list we need to distinguish b/w func and variable 
  if str(Value[i]).startswith('(') and Value[i].endswith(')'):
    if str(Identifier[i]) in FunIdentifier: 
         continue
    else:
      FunArguments.append(Value.pop(i))
      FunIdentifier.append(Identifier.pop(i))
      FunReturnType.append(Datatype.pop(i))

printer()

"""# Sample Input
int x , y = 10 ; <br>
char c = 'z' ; <br>
int func (int,int) ; <br>

# Sample Output
![Screenshot_20230108_035008.png](data:image/png;base64,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)
"""