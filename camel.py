def main():

    name = input("input: ")

    for i in name:
        if i.isupper() != True:
            print(i, end="")
        if i.isupper() == True:
            print(f"_{i.lower()}", end="")
    print()



main()






