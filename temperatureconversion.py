print("Tell me to which one you want to convert to")
print("1.Celsius\n2.Farenheit")
choice = int(input())
if(choice == 1):
    print("Please give the input in Farenheit:")
    inp = float(input())
    print(f"Celcius:{round((inp - 32) * (5/9),1)}")
elif(choice == 2):
    print("Please give the input in Celsius:")
    inp = float(input())
    print(f"Farenheit:{round((inp * (9/5)) + 32,1)}")