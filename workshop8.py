def input_water ():
    water_ph = int(input("กรอกค่า PH ของน้ำ : "))
    return water_ph
def compare_ph (water_ph):
    if water_ph<= 8 :
        compare = 0
    else :
        compare = 1
    return compare
def show_ph( compare ):
    if compare == 0:
        print ("Result is Normal")
    else :
        print ("Result is Alkali")

print ("***---------------------------***")
water_ph = input_water()
print ("***---------------------------***")
compare_ph ( water_ph )
show_ph( compare_ph (water_ph) )
print ("***---------------------------***")