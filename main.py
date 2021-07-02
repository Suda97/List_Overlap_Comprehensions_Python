import random
a = random.sample(range(0, 100), random.randint(1,25))
b = random.sample(range(0, 100), random.randint(1,25))
x = [aa for aa in a for bb in b if aa == bb]

print(a)
print(b)
print(x)
