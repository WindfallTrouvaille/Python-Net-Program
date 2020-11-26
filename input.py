maximum : int = 0
minimum : int = 0
while True :

    inputs = input("Enter a number:")
    num : int = 0

    if inputs == 'done':
        break
    try :
        num = int(inputs)
    except :
        print("Invalid input!")
        continue
    if maximum == 0 or num > maximum :
        maximum = num
    if minimum == 0 or num < minimum :
        minimum = num

print('maximum : %d' %maximum)
print('minimum : %d' %minimum)
