def inputdata():
    product_name = input("กรอกชื่อรายการสินค้า : ")
    product_price = int(input("กรอกราคาสินค้า : "))
    return product_name , product_price
def cal( product_price ):
    vat = product_price * 0.07
    chackout = product_price + vat
    return vat , chackout
def show( product_name , product_price , vat , chackout):
    print (f"ชื่อรายการสินค้า : {product_name}")
    print (f"ราคาสินค้า : {product_price:.2f} | Vat7% : {vat:.2f} | ราคาที่ต้องชำระ {chackout:.2f}")
print ("***------------------***")
product_name , product_price = inputdata()
print ("***------------------***")
vat , chackout = cal( product_price )
show( product_name , product_price , vat , chackout)
print ("***-------END--------***")