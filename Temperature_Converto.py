Temp_Convo = "Converting Temperature Calculator."
print(Temp_Convo)

while True:
    Temp= (input("Convert (C)elsius to Farenheit, (F)arenheit to Celsius, (E)xit. Choose one:")).upper()

    if Temp == 'C':
        cel = float(input("Enter temperature in Celsius:"))
        result = (cel*9/5)+32
        print(f"The {cel} Celsius is {result} Farenheit.")

    elif Temp == "F":
        fah = float(input("Enter temperature in Farenheit:"))
        Result = (fah-32)*5/9
        print(f"The {fah} Farenheit is {Result} Celsius")

    elif Temp == "E":
        print("Bye bye.")
        break

    else:
        print("Invalid input, please choose C,F or E:")
        
    