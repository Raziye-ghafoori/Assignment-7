import random 
girls=['fateme','zahara','raziye','nafas','bahar']
boys=['ali','sina','arvin','shahab','sadjad','amir','reza','mohamad']

marrid=[]
size=len(boys)

for i in range(size):
    if len(girls)==0:
        break
    per1=random.choice(boys)
    per2=random.choice(girls)
    girls.remove(per2)
    boys.remove(per1)
    family=[per1,per2]
    marrid.append(family)


print(marrid)