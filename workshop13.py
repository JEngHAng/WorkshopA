def input_data ():
    id_std = int(input("กรอกรหัสนักเรียน : "))
    user_std = input("กรอกชื่อนักเรียน : ")
    point_std = float(input("กรอกเกรดเฉลี่ยของนักเรียน : "))
    return id_std , user_std , point_std
def cal ( point_std ):
    if point_std < 2:
        answer = "ไม่ผ่าน"
    else :
        answer = "ผ่าน"
    return answer
def show ( id_std , user_std , point_std , answer ):
    print (f"| รหัสนักเรียน : {id_std} | ชื่อนักเรียน : {user_std} |")
    print (f"| เกรดเฉลี่ยของนักเรียน : {point_std} | ผลการเรียน : {answer} |")

print ("***----------------***")
id_std , user_std , point_std = input_data ()
print ("***----------------***")
answer = cal ( point_std )
show ( id_std , user_std , point_std , answer )
print ("***----------------***")