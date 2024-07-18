n1 = int(input("Enter the number1 :"))
n2 = int(input("Enter the number2 :"))
n3 = int(input("Enter the number3 :"))

if n1 > n2:
    #either n1 or n2 is greatest
    if n1 > n3:
        print(n1, "is the greatest no")
    else:
        print(n3, "is greatest no")

else:
    #either n2 or n3 is greatest
    if n2> n3:
        print(n2,"is the greatest no")
    
    else:
        print(n3,"is the greatest no")