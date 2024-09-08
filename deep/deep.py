def main():
    answer = input("The answer to the Great Question of Life, the Universe and Everything is: ").lower().strip()

    if answer in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

main()
