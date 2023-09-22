def input_data():
    id_std = int(input("กรอกรหัสนักเรียน : "))
    name_std = input("กรอกชื่อนักเรียน : ")
    score_00 = float(input("กรอกคะแนนนักเรียนรอบที่ 1 : "))
    score_01 = float(input("กรอกคะแนนนักเรียนรอบที่ 2 : "))
    score_02 = float(input("กรอกคะแนนนักเรียนรอบที่ 3 : "))
    return id_std , name_std , score_00 , score_01 , score_02
def calandshow (id_std , name_std , score_00 , score_01 , score_02):
    score_all = (score_00 + score_01 + score_02) / 3
    print (f"รหัสนักเรียน : {id_std}")
    print (f"ชื่อนักเรียน : {name_std}")
    print (f"คะแนนลำดับที่ 1 : {score_00} | คะแนนลำดับที่ 2 : {score_01} | คะแนนลำดับที่ 3 : {score_02}")
    print (f"เฉลี่ยทั้ง 3 คะแนนได้ : {score_all:.2f}")
    return score_all
print ("***------------------***")
id_std , name_std , score_00 , score_01 , score_02 = input_data()
print ("***------------------***")
calandshow (id_std , name_std , score_00 , score_01 , score_02)
print ("***-------END--------***")