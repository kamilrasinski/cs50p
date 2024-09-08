def main():
    time = convert(input("What time is it? ").strip())

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(x):
    x = x.split(":")
    return float(x[0]) + (float(x[1]) / 60)

if __name__ == "__main__":
    main()
