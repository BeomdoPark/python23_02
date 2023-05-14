# menu_stocks = {1:"apple", 2:"mango", 3:"abc", 4:"ace"}
# stocks = {"apple":[20, 1000], "mango":[10, 2000], "abc":[30, 500], "ace":[50, 2000]}

menu_stocks = {}
stocks = {}


def init():
    f = open("origin_stf2.csv", "r")
    f.readline()
    for _ in range(2):
        token = f.readline()
        tokens = token.split(",")
        menu_stocks[int(tokens[0])] = tokens[1]
        stocks[tokens[1]] = [int(tokens[2]), int(tokens[3])]
    pass


def sell(key, count):
    global stocks
    print(f"Sell {key}, amount:{stocks[key][0]}")
    if stocks[key][0] >= count:
        stocks[key][0] = stocks[key][0] - count
        print(f"sell {key}: {stocks[key][1] * count}")
    else:
        print("Cannot sell {key}")


def sell_apple(count):
    global stocks
    print(f"Sell apple, amount:{stocks['apple']}")
    if stocks["apple"] >= count:
        stocks["apple"] = stocks["apple"] - count
        print(f"sell apple: {1000 * count}")
    else:
        print("Cannot sell apple")


def sell_mango(count):
    global mango
    print(f"Sell mango, amount:{count}")
    if mango >= count:
        mango = mango - count
        print(f"sell mango: {2000 * count}")
    else:
        print("Cannot sell mango")


def print_store():
    print("==========STF============")
    for key, item in stocks.items():
        print(f"{key}:{item}")


def print_menu():
    for key, item in menu_stocks.items():
        print(f"{key}. Buy {item}")
    print("99. Bye")
    print("=========================")


init()
for _ in range(0, 5):
    print_store()
    print_menu()

    choice = int(input("Enter Choice:"))

    if choice != 99:
        amount = int(input("Enter amount:"))
        sell(menu_stocks[choice], amount)
        pass
    elif choice == 99:
        break
    else:
        pass
