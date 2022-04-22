def computepay(h, r):
    if h > 40 :
        pay = 1.5 * r * (h - 40) + (40 * r)
    else:
        pay = h * r
    return pay
    
hr = float(input('Insert your Hours: '))
rt = float(input('Insert your Rate: '))

pay = computepay(hr, rt)
print("Pay", pay)
