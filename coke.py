def main():

    cost = 50

    while cost > 0:
        print(f"Amount Due: {cost}")
        coin = int(input("Insert Coin: "))
        if coin == 25 and cost > 0:
            cost = cost - coin
        elif coin == 10 and cost > 0:
            cost = cost - coin
        elif coin == 5 and cost > 0:
            cost = cost - coin
    if coin == 25 or coin == 10 or coin == 5 and cost < 0:
            print (f"Change Owed: {-cost}")

main()
