def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
select = int(input("enter the number for operations\n1.addtion\n2.subtraction\n3.multiplication\n4.divison"))
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number"))
if select==1:
    print(num1 ,"+", num2 , "=" , add(num1,num2) )
if select==2:
    print(num1 ,"-", num2 , "=" , sub(num1,num2) )
if select==3:
    print(num1 ,"*", num2 , "=" , mul(num1,num2) )
if select==4:
    print(num1 ,"/", num2 , "=" , div(num1,num2) )    