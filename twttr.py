def main():

    sentence = input("Input something: ")
    for i in sentence:
        if i.upper() in ["A", "E", "I", "O", "U"]:
            print("", end="")
        else:
            print(i, end="")

    print()




main()
