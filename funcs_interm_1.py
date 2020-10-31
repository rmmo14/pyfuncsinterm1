import random
def randInt(min= "", max= "" ):
    
    if min != "" and max != "":
        num = int(random.random()*(int(max) - int(min)) + int(min))
    elif max != "":
        num = int(random.random()* int(max))
    elif min !="":
        num = int(random.random()*(100-int(min))+ int(min))
    else: 
        num = int(random.random()*100)
    return num
    print(num)
# print(randInt())
# print(randInt(max = 50))
# print(randInt(min=50)) 
print(randInt(min=50, max=500)) 