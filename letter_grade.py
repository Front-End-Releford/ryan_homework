from random import randint

score = randint(60, 200)
grade = None

if score <= 69:
    grade = 'F'
elif score <= 74:
    grade = 'D'
elif score <= 79:
    grade = 'C'
elif score <= 89:
    grade = 'B'
else:
    grade = 'A'

print(str(score) + '% is a ' + grade + '!')

