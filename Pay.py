hour = input('Please enter working hours：')
rate: float = 10
pay: float = 0
try :
    hour = int(hour)
    if hour <= 40 :
        pay = hour * 10
    else :
        m: int = hour - 40
        pay1: float = 1.5 * 10
        pay = pay1 * m + 40 * 10
    print(pay)
except :
    print('Illegal input')