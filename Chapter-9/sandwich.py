import pyinputplus as pyip 
wheat_price="20"
white_price="10"
sourdough_price="18"
Amount=0

chicken_price="70"
turkey_price="120"
ham_price="65"
tofu_price="80"
while True :
	print("Choose bread type")
	bread=pyip.inputMenu['wheat','white','sourdough']

	if bread == 'wheat':
    	Amount += wheat_price
	elif bread == 'white':
    	Amount += white_price
	elif bread == 'sourdough'
   	 Amount += sourdough_price
    
	print("Choose bread filler menu ")
	material=pyip.inputMenu['chicken','turkey','ham','tofu']

	if material == chicken:
   	 Amount += chicken_price
	elif material == turkey:
    	Amount += turkey_price
	elif material == ham :
    	Amount+= ham
	elif material == tofu :
    	Amount += tofu_price
        
        prompt=input("Do you want another sandwich ?")
       	order=pyip.YesNo(prompt)
        if order=='no'
        break

print("Price of sandwich will be " + str(Amount))
