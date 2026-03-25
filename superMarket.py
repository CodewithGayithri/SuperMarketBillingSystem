from datetime import datetime
name = input("Enter The Name: ")

lists='''
Rice   Rs 50/kg
Maggie Rs 15
Sugar  Rs 42/kg
Atta   Rs 30/kg
Coffee Rs 10
Chilli Rs 15/Kg
Onion  Rs 50/kg
'''

#Declaration
price = 0
pricelist = []
totalprice = 0
finalPrice = 0
ilist=[]
iprice = []
qlist = []
plist = []
finalAmount=0

items = {"Rice":50,
"Maggie": 15,
"Sugar":42,
"Atta":30,
"Coffee":10,
"Chilli":15,
"Onion":50}

while(True):
    option=int(input("1. List ofItems\n2. Buy Items\n3. Exit\nChoose The Option: "))
    if(option==1):
        print(lists)
    elif option == 3:
        break
    elif option == 2:
         item = input("Enter Item Name: ")
         quantity = int(input("Enter The Quantity: "))
         if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item,quantity,items[item],price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalAmount = gst + totalprice
         else:
            print("Sorry Item is Not Available")
    else:
          print("Please Choose Valid Option!")
inp1 = input("Doy Want Bill yes OR no: ")
if inp1 == 'yes':
    pass
    if finalAmount!=0:
        print(25*"=","Super Market",25*"=")
        print(28*" ","Banglore")
        print("Name:",name,30*" ","Date: ",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ","Quantity",3*" "
                  ,"Price",)
        for i in range(len(pricelist)):
            print(i+1,10*" ",ilist[i],12*" ",
                      qlist[i],8*" ",plist[i])
        print(75*"-")
        print(42*" ","TotalAmount: ","Rs",totalprice)
        print(42*" ","GSTAmount: ","Rs",gst)
        print(75*"-")
        print(42*" ","FinalAmount: ","Rs",finalAmount)
        print(75*"-")
        print(30*" ","Thank You")
    



    

    
