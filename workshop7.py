def input_bingo ():
    number_bingo = int(input("กรอกหมายเลข 0 - 25 : "))
    return number_bingo
def random_bingo ():
    import random
    random_number = random.randint( 0 , 25 )
    return random_number
def showbingo ( number_bingo , random_number ):
    if number_bingo == random_number:
        print (f"Your is number : {number_bingo} | Number Bingo is : {random_number} | Correct, You are the win")
    else :
        print (f"Your is number : {number_bingo} | Number Bingo is : {random_number} | Not, Correct!!!")
print ("***---------------------------***")
number_bingo = input_bingo()
print ("***---------------------------***")
random_number = random_bingo ()
showbingo ( number_bingo , random_number )
print ("***---------------------------***")