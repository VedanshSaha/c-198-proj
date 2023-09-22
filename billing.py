while True:
    total=0
    customerName=input("Name of the customer")
    while True:
        print("enter cost of items and quantity")
        cost= float(input("item Cost :"))
        quantity= int(input("quantity :"))
        total += cost*quantity
        repeat=input("do you want to add more items")
        if repeat=="n" or repeat=="N" :
            break
    print("name : ", customerName)
    print("total bill cost: ", total)
    new_customer = input("go to next person")
    if new_customer == "n" or new_customer=="N":
        break
