import random
from collections import Counter

#Generate 7 random numbers ticket list
gen_numbers = random.sample(range(1, 100), 7)
print('List of seven randomly generated numbers:' + str(gen_numbers))

#Lottery ticket list
lottery_ticket = [20, 79, 50, 6, 18, 95, 64]
print('Lottery ticket list:', lottery_ticket)

# counts and matches the occurrence of each integer in both lists
counts = Counter(gen_numbers)
for value, count in counts.most_common():
   counts = Counter(lottery_ticket)
   for value, count in counts.most_common():
       if counts in gen_numbers and lottery_ticket == 3:
           print('You won £20 for three matching numbers', value, count)
       elif counts in gen_numbers and lottery_ticket == 4:
           print('You won £40 for four matching numbers', value, count)
       elif counts in gen_numbers and lottery_ticket == 5:
           print('You won £100 for five matching numbers', value, count)
       elif counts in gen_numbers and lottery_ticket == 6:
           print('You won £10000 for six matching numbers', value, count)
       elif counts in gen_numbers and lottery_ticket == 7:
           print('You won £1000000 for seven matching numbers', value, count)
       else:
           print('Oops! There are no matching numbers from the lists!')
