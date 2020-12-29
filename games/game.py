import random

digits = [1,2,3,4,5,6,7,8,9]

random.shuffle(digits)

sequence = digits[:3]

#print(sequence)

print("The numbers have been generated")

x = sequence[0]

y = sequence[1]
z = sequence[2]



#functions

def check(num1,num2,num3):

    if (num1 == x) or (num2 ==y) or (num3 ==z):

        output_1 = "Match"

        return output_1

    elif (num1 in sequence) or (num2 in sequence) or (num3 in sequence):

        output_2 = "Close"

        return output_2

    else:

        output_3 = "Nope"

        return output_3



def win(num1,num2,num3):

    if (num1==x) and (num2==y) and (num3==z):

        return True

    else:

        return False



#Game logic



while True:

    input_string = input("Enter a list numbers or elements separated by space: ")

    #userlist = input_string.split()

    user_x = int(input_string[0])

    user_y = int(input_string[1])

    user_z = int(input_string[2])

   

    print(check(user_x,user_y,user_z))


    if win(user_x,user_y,user_z)==True:
        print("You guessed the correct order")
        print("Congratz, you win")
        break