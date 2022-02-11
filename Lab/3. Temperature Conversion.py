# Temperature Conversion
# Date 17/11/21
import sys

print("Temperature Conversion from One to another scale")

a = input("Select Default Temperature Scale from Celsius / Fahrenheit / Kelvin: ")
if a not in ["Celsius","celsius","Fahrenheit","fahrenheit","Kelvin" ,"kelvin"]:
    sys.exit("Invalid Input, Recheck !")
    
print("You have selected", a, "as your default temperature measurement scale!")
t = eval(input(" Enter the temperature in Selected Scale : "))

if a == "Celsius" or a == "celsius":
    k = t + 273.16
    f = t*(9/5) + 32
    print(f' The entered temperature {t} converted from {a} to Kelvin is', round(k,2)," and in Fahrenheit is", round(f,2),' !')

elif a == "Fahrenheit" or a == "fahrenheit":
    c = (t - 32) * (5/9)
    k = c + 273.16
    print(f' The entered temperature {t} converted from {a} to Kelvin is', round(k,2)," and in Celsius is", round(c,2),' !') 

elif a == "Kelvin" or a == "kelvin":
    c = t - 273.16
    f = (t - 273.16) * (9/5) + 32
    print(f' The entered temperature {t} converted from {a} to Celsius is', round(c,2)," and in Fahrenheit is", round(f,2),' !')

else:
    print("Invalid Operations, Recheck !")


