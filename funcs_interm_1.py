import random
def randInt(min= "", max= "" ):
    
    # if int(min) > int(max):
    #     holder = min
    #     min = max
    #     max = holder
    # if int(max) < 0:
    #     max = str(-1*int(max))
    
    if min != "" and max != "":
        if int(min) > int(max):
            # holder = min
            # min = max
            # max = holder
            min, max = max, min
        if int(max) < 0:
            max = str(-1*int(max))
            print("max is:", max)
        num = int(random.random()*(int(max) - int(min)) + int(min))
    elif max != "":
        if int(max) < 0:
            max = str(-1*int(max))
            print("max is:", max)
        num = int(random.random()* int(max))
    elif min !="":
        num = int(random.random()*(100-int(min))+ int(min))
    else: 
        num = int(random.random()*100)
    # print(num)
    return num
# print(randInt())
# print(randInt(max = -50))
# print(randInt(min=50)) 
print(randInt(min=50, max=-500)) 