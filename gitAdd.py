import os
from random import randint

d = str(1) + 'days ago'
with open('file. txt', 'a') as file:
    file.write(d)
os.system('git add .')
os.system('git commit --date=-"' + d+'"-m"commit"')
os. system('git push -u origin main')
