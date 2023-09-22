def input_data ():
    x = float(input("Input X : "))
    return x
def cal(x):
    y = (( 2 * ( x ** 2 )) + ( 2 * x ) + 1 )
    return y
def showx ( x, y ) :
    print(f'y = ( 2  * ( {x:.0f} ** 2 )) + ( 2 * {x:.0f} ) + 1')
    print (f"แก้สมการได้ : {y:.0f}")

print ("***------------------***")
x = input_data()
print ("***------------------***")
y = cal(x)
showx ( x, y )
print ("***-------END--------***")