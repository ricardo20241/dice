def random():
    num = int(input("Enter any number between 1 to 6 : "))
    import random
    random1 = random.randrange(1, 6)
    print("Number at the face of dice is:", random1)
    point=0
    if num == random1:
        a = random.randrange(40, 50)
        print("^^^^^^^^^^^^^^^^^^  YOU WON THE ROUND  ^^^^^^^^^^^^^^^^^^^")
        print("Total point gained this round", a)
        point = a
    elif num>0 and num <= 6:
        print("You lost the round ")
    else:
        print("You entered the wrong input")
    return point

total_point = 0
random()
while True:
    n = input("Press yes to continue |||||||   Press no to exit : ")
    if n == "yes":
        point = random()
        total_point = total_point + point
    elif n == "no":
        break
    else:
        print("restart")
print("*********************   ROUND OVER   **********************")
print("Total Point Won -->",total_point)
