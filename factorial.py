#Write a Python program that finds the factorial of a number using recursion and returns the result.
def fact(num):
    if(num==1):
        return num
    else:
        return num*fact(num-1)
input1=int(input("enter a  number :"))  
if (input1<0):
    print("please enter a postive number")
elif(input1==0): 
    print("the factorial 1")
else:
    print(f"the factorial of {input1}",fact(input1)) 