total : float = 0
counts : int = 0
average : float = 0.0
#inputs = input("Please enter :")
while True :#使用while循环
    inputs = input("Please enter :")
    if inputs == 'done' :#如果输入done，则退出当前循环
        break
    try :
        inputs = float(inputs)
    except :
        print("Invalid input")#%inputs
        continue#继续循环
    total += inputs
    counts = counts + 1
    average = total / counts
print('total: %d' %total)
print( 'counts: %d' %counts)
print('average: %s' %average)