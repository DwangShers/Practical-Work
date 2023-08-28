Temp_Convo = "Converting Temperature Calculator."
print(Temp_Convo)

Temp = (input("Convert (C)elsius to Farenheit, (F)arenheit to Celsius, (E)xit."))
print('Choose C or F or E')

if Temp == 'C':
    cel = float(input("Enter temperature in Celsius:"))
    result = (cel*9/5)+32
    print(result)

elif Temp == "F":
    fah = float(input("Enter temperature in Farenheit:"))
    Result = (fah-32)*5/9
    print(Result)

elif Temp == "E":
    print("Bye bye.")

else:
    print()