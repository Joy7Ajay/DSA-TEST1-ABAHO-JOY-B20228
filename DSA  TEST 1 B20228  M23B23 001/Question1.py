# i changed 1st to first because numbers cannot be used at the start of function names.
first = [14,8,-23,4,6,10,-18,5,5,11]
maxSum = first[0]
sumz = 0

for i in range(0, len(first)):
    sumz += first[i]
    
    if sumz<0:
        sumz = 0
    elif maxSum < sumz:
        maxSum = sumz
        
print("Maximum Sub Array Sum =", maxSum)