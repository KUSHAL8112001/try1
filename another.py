
resources= { "water":300,
             "milk":200,
             "coffee":100
            }

machine_hold = {"espresso":{"water":100,"milk":100,"coffee":50},"price":50,
                "coffee":{"water":150,"milk":150,"coffee":70},"price":70,
                "lattee":{"water":100,"milk":150,"coffee":30},"price":90
                }

def reports(res):
    Water=res["water"]
    Milk=res["milk"]
    Coffee=res["coffee"]
    return(f"The current resources available are \nWater: {Water} \nMilk: {Milk} \nCoffee: {Coffee} \n ")

def checkresources(item):
    for resource, amount in machine_hold[item].items():
        if resource in resources and resources[resource] < amount:
            print(f"Not enough {resource}")
            return False
    return True


def needmoney(user_item):
    if user_item=="espresso":
        print("The coste of espresso is 50 rupees ")
        ten_rupee=int(input("Enter the number of 10 rupees note "))
        twenty_rupee=int(input("Enter the number of 20 rupees note "))
        user_money=10*ten_rupee+20*twenty_rupee
        if user_money==50:
            print("We have prepared your espresso ")
            resources["water"]=resources["water"]-machine_hold["espresso"]["water"]
            resources["coffee"]=resources["coffee"]-machine_hold["espresso"]["coffee"]
            resources["milk"]=resources["milk"]-machine_hold["espresso"]["milk"]
            print(reports(resources))
        elif user_money>50:
            refund=user_money-50
            print(f"The coffee is prepared, {refund} amount is returned ")
            resources["water"]=resources["water"]-machine_hold["espresso"]["water"]
            resources["coffee"]=resources["coffee"]-machine_hold["espresso"]["coffee"]
            resources["milk"]=resources["milk"]-machine_hold["espresso"]["milk"]
            print(reports(resources))
        else:
            print("Order terminated\n The amount entered is less than 50 ")

    if user_item=="coffee":
        print("The coste of coffee is 70 rupees ")
        ten_rupee=int(input("Enter the number of 10 rupees note "))
        twenty_rupee=int(input("Enter the number of 20 rupees note "))
        user_money=10*ten_rupee+20*twenty_rupee
        if user_money==70:
            print("We have prepared your coffee ")
            resources["water"]=resources["water"]-machine_hold["coffee"]["water"]
            resources["coffee"]=resources["coffee"]-machine_hold["coffee"]["coffee"]
            resources["milk"]=resources["milk"]-machine_hold["coffee"]["milk"]
            print(reports(resources))
        elif user_money>70:
            refund=user_money-70
            print(f"The coffee is prepared, {refund} amount is returned ")
            resources["water"]=resources["water"]-machine_hold["coffee"]["water"]
            resources["coffee"]=resources["coffee"]-machine_hold["coffee"]["coffee"]
            resources["milk"]=resources["milk"]-machine_hold["coffee"]["milk"]
            print(reports(resources))
        else:
            print("Order terminated\n The amount entered is less than 70 ")

    if user_item=="lattee":
        print("The coste of lattee is 90 rupees ")
        ten_rupee=int(input("Enter the number of 10 rupees note "))
        twenty_rupee=int(input("Enter the number of 20 rupees note "))
        user_money=10*ten_rupee+20*twenty_rupee
        if user_money==90:
            print("We have prepared your lattee ")
            resources["water"]=resources["water"]-machine_hold["lattee"]["water"]
            resources["coffee"]=resources["coffee"]-machine_hold["lattee"]["coffee"]
            resources["milk"]=resources["milk"]-machine_hold["lattee"]["milk"]
            print(reports(resources))
        elif user_money>90:
            refund=user_money-90
            print(f"The lattee is prepared, {refund} amount is returned ")
            resources["water"]=resources["water"]-machine_hold["lattee"]["water"]
            resources["coffee"]=resources["coffee"]-machine_hold["lattee"]["coffee"]
            resources["milk"]=resources["milk"]-machine_hold["lattee"]["milk"]
            print(reports(resources))
        else:
            print("Order terminated\n The amount entered is less than 90 ")

is_on=True
while is_on:
    choice=input("Espresso, Coffee, Lattee \n").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(reports(resources))
#after this the main the code starts 
    elif choice=="espresso":
        if checkresources("espresso")==True:
            is_money=needmoney("espresso")
#the code for the coffee
    elif choice=="coffee":
        if checkresources("coffee")==True:
            is_money=needmoney("coffee") 

#the code for lattee         
    elif choice=="lattee":
        if checkresources("lattee")==True:
            is_money=needmoney("lattee")
