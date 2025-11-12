import random
import time

OPEARATORS =["+","-","*",]
MIN_OPERAND =3
MAX_OPERAND =12
TOTAL_PROBLEMS =10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right= random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPEARATORS)

    expr = str(left) +" "+ operator  +" " + str(right)
    #eval function to dynamically cal results
    answer = eval(expr)
    return expr , answer

wrong = 0
input("Press any button to begin...")
print("-----------")

strat_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()
    while True:
        guess= input("Problem # " + str(i+1) + ":" + expr + "= ")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()
total_time = end_time - strat_time

print("-----------")
print("Nice work, you finished in",str(round(total_time, 2)), "seconds")
