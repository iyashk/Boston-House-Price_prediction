import os
from random import randint

for j in range(0, randint(1, 10)):
    d = str(j) + 'days ago'
    # with open('file. txt', 'a') as file:
    #     file.write(d)
    # os.system('git add .')
    print('git commit --date=-"' + d+'"-m"commit"')
# os. system('git push -u origin main')
