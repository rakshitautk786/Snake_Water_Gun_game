import random
def swg_game(comp,user):
    if user==comp:
        return None
    elif comp=='s':
        if user=='w':
            return False
        elif user=='g':
            return True
    elif comp=='w':
        if user=='g':
            return False
        elif user=='s':
            return True
    elif comp=='g':
        if user=='w':
            return True
        elif user=='s':
            return False


        
print("comp Turn snake(s),water(w),gun(g)?")        
comp=random.randint(1,3)
if comp==1:
    comp='s'
elif comp==2:
    comp='w'
elif comp==3:
    comp='g'

user=input("your turn: snake(s),water(w),gun(g)?")

result=swg_game(comp,user)
print(f"computer choice {comp}")
print(f"user choice {user} ")
if result==None:
    print("Tie")
elif result==True:
    print("You win")
elif result==False:
    print("You Lose")
    