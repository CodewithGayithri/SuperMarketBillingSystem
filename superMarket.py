from datetime import datetime
name = input("Enter The Name: ")

lists='''
Rice Rs 50/Kg
Maggie 15
Sugar Rs 42/Kg
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

items = {"Rice":50,
"Maggie": 15,
"Sugar":42}
option=int(input("for list of items press 1:"))
if(option==1):
    print(lists)
for i in range(len(items)):
    inp = int(input("If You Want to Buy Press 1 OR To Exit Press 2"))
    if inp == 2:
        break
    if inp == 1:
        item = input("Enter Item Name: ")
        quantity = int(input("Enter The Quantity: "))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalAmount = gst + totalprice
        else:
            print("Sorry Item is Not Available")
    else:
        print("You Entered Wrong Number")
    inp1 = input("Doy Want Bill yes OR no")
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
                print(i,10*" ",ilist[i],12*" ",
                      qlist[i],8*" ",plist[i])
            print(75*"-")
            print(45*" ","TotalAmount: ","Rs",totalprice)
            print(45*" ","GSTAmount: ","Rs",gst)
            print(75*"-")
            print(50*" ","FinalAmount: ","Rs",finalAmount)
            print(75*"-")
            print("Thank You")
    



    

    
