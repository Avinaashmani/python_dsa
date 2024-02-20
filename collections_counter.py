from collections import Counter
import random

list_ex = []
str_ex = ('Learning a little each day adds up. Research shows that students who make learning a habit are more likely '
          'to reach their goals. Set time aside to learn and get reminders using your learning scheduler.')
for i in range(25):
    list_ex.append(random.randint(20, 45))

counter = Counter(list_ex)
counter_str = Counter(str_ex)
print(list_ex)
print(counter)
print(counter_str.most_common(18))
