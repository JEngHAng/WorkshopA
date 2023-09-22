def head ():
    print ("|===============================|")
    print ("| Number 1 | Welcome Freshman   |")
    print ("| Number 2 | Welcome Sophomore  |")
    print ("| Number 3 | Welcome Junior     |")
    print ("| Number 4 | Welcome Senior     |")
    print ("|===============================|")
def input_data ():
    number = int(input("กรอกตัวเลข 1 - 4 : "))
    return number 
def ifnumber ( number ):
    if number == 1:
        print ("| Welcome Freshman   |")
    elif number == 2:
        print ("| Welcome Sophomore  |")
    elif number == 3:
        print ("| Welcome Junior     |")
    elif number == 4:
        print ("| Welcome Senior     |")
    else :
        print ("Not number input again")
head()
number = input_data()
print ("|===============================|")
ifnumber ( number )
print ("|===============================|")