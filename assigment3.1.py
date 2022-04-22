# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# ----Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#-----Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 




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
