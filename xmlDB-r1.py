import xmltodict
import os.path
import random
import dict2xml

print('Welcome to Our XML-based Database')
print('Options')
print('\t0<- quit')
print('\t1<- load file')
print('\t2<- list users')
print('\t3<- add user')
print('\t4<- edit user')
print('\t5<- save file')

opcode = ['quit','load()', 'list()', 'add()', 'edit()', 'save()']

def load():
   x = input("Filename: ")
   if os.path.exists(x):
      print(x + " exists")
      f = open(x)
   else:
      print(x + " doesn't exist. Try again.")   
      
   buf = f.read()
   print(buf)
   f.close()

   dict = xmltodict.parse(buf)
   global listOfUsers
   root = dict.get('root') 
   listOfUsers = root['user']    
        
def list():
   for x in listOfUsers:
     name  = x['name']
     bg    = x['background']
     print("{} prefers a {} background".format(name,bg))
     
def add():   
   name = input("Enter User name: ")
   pref = input("Preference 1 (light) or 2 (dark): ")
   key = random.randrange(1000, 10000000)
   
   theme = "light"
   if pref != 1: theme = "dark"
   newuser= {"name":name,"background":theme,"key":key}  
   listOfUsers.append(newuser)
     
def edit():
   print("edit called")
   
def save():
   x = '<?xml version="1.0" encoding="UTF-8"?>\n'
   x += '<root>\n'

   y = dict2xml.dict2xml(listOfUsers,wrap="user")  #wrap every list element
   
   x += y
   x += '</root>'

   fn = input("Enter output filename: ")
   f = open(fn,"w+")
   f.write(x)
   f.close()
     
# ----------------------------------------------
while True:
   x = int(input("Select: "))
   if x == 0: break  
   if x >= 0 and x<=5:
      eval(opcode[x])

