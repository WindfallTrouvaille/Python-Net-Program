score = input('Please enter your scores:')
try :
   score = float(score)
   if score >= 0.9 and score < 1 :
       print('Grade is "A"')
   elif score >= 0.8 and score < 0.9 :
       print('Grade is "B"')
   elif score >= 0.7 and score < 0.8 :
       print('Grade is "C"')
   elif score >= 0.6 and score < 0.7 :
       print('Grade is "D"')
   elif score >= 0 and score < 0.6 :
       print('Grade is "F"')
   else :
       print('Bad score!')
except :
    print('Bad score!')
