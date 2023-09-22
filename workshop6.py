def head ():
    print ("***-------โปรแกรมการคำนวณดอกเบี้ย-------***")
def input_money():
    money = float(input("จำนวนเงินที่กู้ : "))
    return money
def interest (money):
    if money > 1000:
        money_interest = ( money * 0.025 ) + money
        print (f"กู้เงินมากกว่า 1000 บาท คิดดอกเบี้ย ร้อยละ '2.5' บาท รวมทั้งหมดเป็น : {money_interest} บาท")
    else :
        money_interest = ( money * 0.055 ) + money
        print (f"กู้เงินน้อยกว่า 1000 บาท คิดดอกเบี้ย ร้อยละ '5.5' บาท รวมทั้งหมดเป็น : {money_interest} บาท")
    return money_interest

print ("***------------------------------------***")
head()
print ("***------------------------------------***")
money = input_money()
print ("***------------------------------------***")
interest (money)
print ("***------------------------------------***")