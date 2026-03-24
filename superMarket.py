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
print(price)


    

    
