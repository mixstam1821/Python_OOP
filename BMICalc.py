def main():
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    result = weight / (height ** 2)

    print("Your BMI is", result)

if __name__ == "__main__":
    main()
