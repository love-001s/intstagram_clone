import random
n = int(input("Guess Number from 1 to 10 :"))
c = random.randint(1,10)
i = 1

while n!=c:
    print("Your failed, \n Try Again")
    n = int(input("Guess Number from 1 to 10 :"))
    i +=1

print(f"\nYour choose number: {n}")
print(f"You Won The game!, In {i} attempts  ")    