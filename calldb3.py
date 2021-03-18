import xmlDBr3 as xmldb

db = xmldb.xmldb()

def display(user):
	name = user['name']
	bg = user['background']				
	print("{} prefers a {} background".format(name,bg))
	
	if 'otherprefs' in user:
		op = user['otherprefs']
		for key, value in op.items():
			print("\t{} = {}".format(key,value))

#opcode = ['quit','load()', 'list()', 'add()', 'edit()', 'save()']
print('Welcome to Our XML-based Database')
print('Options')
print('\t0<- quit')
print('\t1<- load file')
print('\t2<- list users')
print('\t3<- add user')
print('\t4<- save file')
print('\t5<- find user')
while True:

	x = str(input("Select: "))
		
	if x == "0": break  

	elif x == "1": 
		f = input("Filename: ")
		rtn = db.load(f)
		if rtn != "ok" : print(rtn)

	elif x == "2":
		list = db.list()
		for x in list: display(x)
 
	elif x == "3":  #add new user
		name = input("Enter User name: ")
		pref = input("Preference 1 (light) or 2 (dark): ")
	
		theme = "light"   
		newuser= {"name":name,"background":theme}      
		key = db.add(newuser)
		print("User added with key {}".format(key))

	elif x == "4":  #save database       
		filename = input("Enter output filename: ")
		db.save(filename)
		
	elif x == "5": #find user
		key = input("Enter key: ")
		y = db.find(username)
		if type(y) == str:
			print(y)
		else:
			display(y)

       
print("Goodbye")



