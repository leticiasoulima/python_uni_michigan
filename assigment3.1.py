hr = input('Enter Hours: ')
try :
    h = int (hr)
except :
    print('Not a number')
rate = input('Enter Rate: ')
try :
    rt = float (rate)
except :     
    print('Not a number')
    
if h <= 40 :
	payment = float(h) * float(rt)
    	print(payament)
else :
    payment = float(40 * rt  + ( h - 40) * 1.5 * rt)
print(payment)
