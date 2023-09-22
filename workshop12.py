def input_data () :
    group_leader = input("กรอกชื่อหัวหน้ากรุ๊ปทัวร์ : ")
    number_leader = int(input("กรอกเบอร์ติดต่อกลับภายหลัง : "))
    people = int(input("กรอกจำนวนคนที่จะไปเที่ยวกับกรุ๊ปทัวร์ : "))
    return group_leader , number_leader , people
def cal_people ( people ) :
    if people <= 2 :
        pay = 300
    elif people <= 5 :
        pay = 250
    elif people <= 10 :
        pay = 210
    else :
        pay = 150
    return pay
def show ( group_leader , number_leader , people , pay ) :
    print (f"| ชื่อหัวหน้ากรุ๊ปทัวร์ : {group_leader} | เบอร์ติดต่อกลับภายหลัง : {number_leader} |")
    print (f"| จำนวนคนที่จะไปเที่ยวกับกรุ๊ปทัวร์ : {people} | ตกคนละ {pay} บาท |")
    print (f"ยอดรวมทั้งหมดที่ต้องชำระ {people * pay}")

print ("***------------------------***")
group_leader , number_leader , people = input_data ()
print ("***------------------------***")
pay = cal_people ( people )
show ( group_leader , number_leader , people , pay )
print ("***------------------------***")