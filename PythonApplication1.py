
petrol = {"AI92": 1, "AI95": 2, "DIZEL": 0.8}
food = {"HotDog": 2.2, "Sprite": 1.5, "HamBurger": 3.7}


def addPetrol():
    choise = input("Do you want add petrol: ")
    if choise == "Yes" or choise == "yes":
        addpetrol = input("Which petrol do you want to add : ")
        price = float(input("Enter price: "))
        petrol.update({addpetrol: price})
        print(petrol)
        FoodList()


def addFood():
    choise = input("Do you want add Food: ")
    if choise == "Yes" or choise == "yes":
        addfood = input("Which food do you want to add : ")
        price = float(input("Enter price: "))
        food.update({addfood: price})
        print(food)


def FoodList():
    print(food)
    choise = input("Do you want delete food: ")
    if choise == "Yes" or choise == "yes":
        delete = input("Which food do you want to delete: ")
        if delete in food:
            del food[delete]
            print(food)
            addFood()
        else:
            print("The food with this name isn't in food list: ")
    elif choise == "No" or choise == "no":
        pass


def PetrolList():
    print(petrol)
    choise = input("Do you want delete petrol: ")
    if choise == "Yes" or choise == "yes":
        delete = input("Which petrol do you want to delete: ")
        if delete in petrol:
            del petrol[delete]
            print(petrol)
            addPetrol()
        else:
            print("The petrol with this name isn't in petrol list: ")
    elif choise == "No" or choise == "no":
        choise = input("""Do you want see food list or add petrol
                        1)AddPetrol
                        2)Food
                        : """)
        if choise == "1":
            addPetrol()
        elif choise == "2":
            FoodList()
        else:
            pass


choise = int(input("""
Hi user ! Welcome to the system
1) Admin panel
2) Guest panel 
SELECT :

"""))

food = {"HotDog": 2.2, "Sprite": 1.5, "HamBurger": 3.7}
total=0
def buy_Food():
    global total
    print(f"Select food with you want to buy: {food}")
    select1=input("Select food: ")
    if select1=="HotDog" or select1=="Sprite" or select1=="HamBurger":
        count1=int(input(f"How many {select1} you want: "))
        if select1=="HotDog":
            total += count1 * 2.2
            print(f"You should pay {total}")
        elif select1=="Sprite":
            total += count1 * 1.5
            print(f"You should pay {total}")
        elif select1=="HamBurger":
            total += count1*3.7
            print(f"You should pay {total}")
        choise=input("Do you want buy anything else: ")
        if choise=="Yes" or choise=="yes":
            select1 = input("Select food: ")
            if select1 == "HotDog" or select1 == "Sprite" or select1 == "HamBurger":
                count1 = int(input(f"How much {select1} you want: "))
                if select1 == "HotDog":
                    total += count1 * 2.2
                    print(f"You should pay {total}")
                elif select1 == "Sprite":
                    total += count1 * 1.5
                    print(f"You should pay {total}")
                elif select1 == "HamBurger":
                    total += count1 * 3.7
                    print(f"You should pay {total}")
                else:print("We dont have this food")
                choise = input("Do you want buy anything else: ")
                if choise == "Yes" or choise == "yes":
                    select1 = input("Select food: ")
                    if select1 == "HotDog" or select1 == "Sprite" or select1 == "HamBurger":
                        count1 = int(input(f"How much {select1} you want: "))
                        if select1 == "HotDog":
                            total += count1 * 2.2
                            print(f"You should pay {total}")
                        elif select1 == "Sprite":
                            total += count1 * 1.5
                            print(f"You should pay {total}")
                        elif select1 == "HamBurger":
                            total += count1 * 3.7
                            print(f"You should pay {total}")
                        else:
                            print("We dont have this food")
        print(f"Thanks for comming to our petrol shop this is you bill : {total}")
    else:print("We dont have this food")

admin_password_login = "admin"
if choise == 1:
    password = input("Enter password : ")
    if password == admin_password_login:
        print(f"Welcome {admin_password_login} ! ")
        PetrolList()
elif choise == 2:
    print(f"What do you want buy this is our menu of fast food and petrols{petrol},{food}")
    choise = input(f"First you should select petrol: {petrol}: ")
    if choise == "AI92":
        choise = input("LITER OR PRICE: ")
        if choise == "LITER" or choise == "Liter":
            liter = float(input("How much liter you want: "))
            liter_price_sum = liter * 1
            print(f"Sum: {liter_price_sum}")
        elif choise == "PRICE" or choise == "Price":
            price = float(input("Enter price: "))
            liter_price_sum = price / 1
            print(f"You shold pay for petrol: {liter_price_sum}")
    elif choise == "AI95":
        choise = input("LITER OR PRICE: ")
        if choise == "LITER" or choise == "Liter":
            liter = float(input("How much liter you want: "))
            liter_price_sum = liter * 2
            print(f"Sum: {liter_price_sum}")
        elif choise == "PRICE" or choise == "Price":
            price = float(input("Enter price: "))
            liter_price_sum = price / 2
            print(f"You shold pay for petrol: {liter_price_sum}")
    elif choise == "DIZEL":
        choise = input("LITER OR PRICE: ")
        if choise == "LITER" or choise == "Liter":
            liter = float(input("How much liter you want: "))
            liter_price_sum = liter * 0.8
            print(f"You shold pay for petrol: {liter_price_sum}")
        elif choise == "PRICE" or choise == "Price":
            price = float(input("Enter price: "))
            liter_price_sum = price / 0.8
            print(f"You shold pay for petrol: {liter_price_sum}")
    choise = input("Do you want buy food? ")
    if choise == "Yes" or choise == "yes":
        buy_Food()
    elif choise == "No" or choise == "no":
        print("Thanks for comming our petrol pls come again we will be happy")