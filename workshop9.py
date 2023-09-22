def input_data():
    id_user = int(input("กรอกรหัสพนักงาน : "))
    name_user = input("กรอกชื่อพนักงาน : ")
    price_product = int(input("กรอกยอดที่ขายของได้ : "))
    return id_user , name_user , price_product
def cal( price_product ):
    if price_product < 1000 :
        commission = 0.0
        text_commission = 0.0
    elif price_product <= 2000 :
        commission = 0.01
        text_commission = 1
    elif price_product <= 3000 :
        commission = 0.03
        text_commission = 3
    else :
        commission = 0.05
        text_commission = 5
    have_production = price_product * commission
    have_production_all = ( price_product * commission ) + price_product
    return commission , have_production , have_production_all , text_commission
def show( id_user , name_user , price_product , text_commission , have_production , have_production_all):
    print (f"| รหัสพนักงาน : {id_user} | ชื่อพนักงาน : {name_user} | ยอดที่ขายของได้ : {price_product} บาท |")
    print (f"| เปอร์เซ็นต์ที่ได้จากคอมมิชชั่น : {text_commission} % | ได้ค่าคอมมิชชั่นเป็นจำนวนเงิน : {have_production:.2f} บาท |")
    print (f"| ได้รับเงินเป็นจำนวน : {have_production_all:.2f} บาท |")
print ("***---------------------------***")
id_user , name_user , price_product = input_data()
print ("***---------------------------***")
cal( price_product )
commission , have_production , have_production_all , text_commission = cal( price_product )
show( id_user , name_user , price_product , text_commission , have_production , have_production_all)
print ("***---------------------------***")