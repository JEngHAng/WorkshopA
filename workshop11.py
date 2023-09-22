def input_data ():
    phone_number = int(input("กรอกเบอร์โทรศัพท์ : "))
    user_name = input("กรอกชื่อผู้ใช้เบอร์โทรศัพท์ : ")
    time_call = float(input("กรอกจำนวนที่ต้องการใช้โทรศัพท์ : "))
    return phone_number , user_name , time_call
def cal_min_call ( time_call ):
    if time_call <= 15 :
        min = 5 
    elif time_call <= 30 :
        min = 3
    else :
        min = 1.50
    money_time = time_call * min
    return min , money_time
def show ( phone_number , user_name , time_call , money_time ):
    print (f"| ชื่อผู้ใช้เบอร์โทรศัพท์ : {user_name} | เบอร์โทรศัพท์ : {phone_number} |")
    print (f"| จำนวนที่ใช้โทร : {time_call} นาที | ตกนาทีละ : {min} บาท |")
    print (f"| เป็นจำนวนเงิน : {money_time} บาท |")
print ("***-----------------------***")
phone_number , user_name , time_call = input_data ()
print ("***-----------------------***")
min , money_time = cal_min_call ( time_call )
show ( phone_number , user_name , time_call , money_time )
print ("***-----------------------***")