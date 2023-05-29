# menu_stocks = {1:"apple", 2:"mango", 3:"abc", 4:"ace"}
# stocks = {"apple":[20, 1000,total_profit], "mango":[10, 2000,total_profit],}

# 자료구조 선언
menu_stocks = {}  # { key(ID) : value(menu) }
stocks = {}  # { key(menu) : value([amount, value, total_profit]) }

f = open("stf2.csv", "r")
history_file = open("history.csv", "w")  # history.csv 생성 메뉴 값 및 입력 값 저장
sales_file = open("sales.csv", "w")  # history.csv 생성
rows_when_init = len(f.readlines())  # 전체 줄 개수
f.seek(0)  # f.readlines() 이후 seek(0)


def init():
    f.readline()  # 한 줄 날림
    for _ in range(rows_when_init - 1):  # 기존 자료에 있는 menu_stocks, stocks 선언과 초기화
        token = f.readline()
        tokens = token.split(",")  # [2, mango, 10, 2000]
        menu_stocks[int(tokens[0])] = tokens[1]

        # total_profit은 실행 시마다 0으로 초기화
        stocks[tokens[1]] = [int(tokens[2]), int(tokens[3]), 0]

    # 자료구조에 저장 후 "w+"모드로 새로 열기
    global file

    file = open("stf2.csv", "w+")
    file.write("id,name,amount,value,\n")
    f.close()
    sales_file.write("name,value,count,profit\n")


def sell(key, count):
    # global stocks
    print(f"Sell {key}, amount:{stocks[key][0]}")
    stocks[key][2] += stocks[key][1] * count  # stocks[key][2](=total_profit) 증감식
    if stocks[key][0] >= count:
        stocks[key][0] = stocks[key][0] - count
        print(f"sell {key}: {stocks[key][1] * count}")
        sales_file.write(f"{key},{stocks[key][1]},{count},{stocks[key][2]}\n")
    else:
        print(f"Cannot sell {key}")


# 재고출력
def print_store(choice=1):
    if choice == 1:
        print("==========STF============")
    elif choice == 0:
        print("Print Store")
    for key, value in sorted(menu_stocks.items()):
        print(f"{value} : {stocks[value][0:2]}")


# 메뉴 시작화면 출력
def print_menu():
    for key, value in sorted(menu_stocks.items()):
        print(f"{key}. Buy {value}")

    print("97. Insert Item")
    print("98. Remove Item")
    print("99. Bye")
    print("0. Print Stock")
    print("=========================\n")


# 97. 품목 추가 : 품목명, 재고 수, 가격을 입력 받고 품목 ID를 자동으로 부여, 자료구조에 추가.
def add_menu():
    name = input("Enter the menu's [name] : ")
    amount = int(input("Enter [amount] of menu : "))
    value = int(input("Enter the [price] of menu : "))
    history_file.write(f"{name}\n{amount}\n{value}\n")

    for i in range(1, sorted(menu_stocks.keys())[-1] + 2):
        if menu_stocks.get(i) == None:  # id가 자동으로 부여됨
            menu_stocks[i] = name  # menu_stocks dict에 append 기능을 함
            stocks[name] = [amount, value, 0]
            break


# 98. 품목 삭제 : 현재 품목을 보여주고, 사용자가 선택한 품목을 삭제. csv내 해당 품목에 대한 정보삭제.
def delete_menu():
    for key, item in sorted(menu_stocks.items()):
        print(f"[id] {key} : {item}")
    select_id = int(input("Enter the [id] of the item to be deleted : "))
    history_file.write(f"{select_id}\n")
    del stocks[menu_stocks[select_id]], menu_stocks[select_id]


# 99. Bye : stf2.csv에 현재 ID,menu,amount,value 저장
def exit_with_savecsv():
    file.seek(0)
    file.readline()  # 2번째 줄부터 작성됨.
    rows_when_close = len(menu_stocks)  # 닫을 시 stf2.csv에 작성할 줄 개수

    for key in sorted(menu_stocks.keys()):
        menu_name = menu_stocks[key]
        file.write(
            f"{key},{menu_name},{stocks[menu_name][0]},{stocks[menu_name][1]},\n"
        )
    file.close()
    history_file.close()
    sales_file.close()


# 프로그램 동작
init()

while True:
    print_store()
    print_menu()
    choice = int(input("Enter Choice:"))
    history_file.write(f"{choice}\n")
    if menu_stocks.get(choice) is not None:  # menu_stocks에 해당 id가 있으면 실행
        amount = int(input("Enter amount:"))
        history_file.write(f"{amount}\n")
        sell(menu_stocks[choice], amount)
    elif choice == 0:
        print_store(choice)
    elif choice == 97:  # 품목추가
        add_menu()
    elif choice == 98:  # 품목삭제
        delete_menu()
    elif choice == 99:  # Bye
        exit_with_savecsv()
        break
    else:
        print("Please enter valid Choice")
