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
    

    
