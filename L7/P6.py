'''
wapp for billing software

'''	

menu = {'idli':30, 'dosa':40, 'vada':20}

amount = 0.0
while True:
	op = int(input("1 add, 2 amount and 3 exit"))
	if op == 1:
		item_name = input("Enter item name orderred ")
		item_price = menu.get(item_name, 0)
		if item_price == 0:
			print("Invalid item name")
		else:
			qty = int(input("enter quantity "))
			amount += item_price * qty
	elif op == 2:
		print("amount = ", amount)
	elif op == 3:
		break
	else:
		print("invalid option ")	
			