# restoran sistemasi

menu = {
    "non":  1,
    "osh": 3,
    "shashlik": 1,
    "manti": 0.5,
    "choy": 0.6,
    "coca cola": 1

}

savatcha = {

}
def show_menu():
    count = 1
    for k,v in menu.items():
        print(f"{count}.{k} ----------- ${v}")
        count +=1



def order():
    while True:
        ovqat = input("Ovqatni tanlang:    ")
        p = int(input("portsiyasini kiriting:    "))
        if ovqat.lower() not in  menu.keys():
            # raise ValueError("Uzur oka ovqat yoq menuyda.")
            print("Uzur oka ovqat yoq menuyda.")
        else:
            savatcha[ovqat] = p
        
        answer = input("Davom etasizmi (ha/yoq): ")
        if answer == "yoq":
            break
        else:
            continue


def order_update():
        ovqat = input("Ovqatni tanlang:    ")
        p = int(input("portsiyasini kiriting:    "))
        if ovqat.lower() not in  menu.keys():
            # raise ValueError("Uzur oka ovqat yoq menuyda.")
            print("Uzur oka ovqat yoq menuyda.")
        else:
            savatcha[ovqat] = p
        

def get_bill():
    total = 0
    for k,v in savatcha.items():
        total+=menu[k]
    print(f"Umumiy hisob ${total} boldi")





# show_menu()
# order()
# print(savatcha)
# order_update()
# print(savatcha)
# get_bill()


def main():
    while True:
        choice = int(input("1.Menu\n2.Biyurtma berish\n3.Buyurtma qoshish\n4.Hisob\n5.Exit\nRaqamorqali tanlang:  "))
        if choice == 1:
            show_menu()
        elif choice ==2:
            order()
        elif choice ==3:
            order_update()
        elif choice == 4:
            get_bill()
        