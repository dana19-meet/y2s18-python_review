class superhero:
	def __init__(self,name,suerpower,strength):
		self.name=name
		self.suerpower=suerpower
		self.strength=strength

def sprint(sname):
	print(sname.name)
	print(sname.strength)

dana=superhero("Dana","read",6)
sprint(dana)

def saving(name,work):
	if (name.strength>work):
		print(name.strength-work)
	elif(name.strength<work):
		print("superhero is not strong enough! :(")

saving(dana,8)