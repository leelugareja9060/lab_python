#else..if
age=int(input("enter your age:"))
if age>=18:
    print("yes you are eligible")
else
    print("no you are not eligible")
#0dd or even number
num=int(input("enter number:"))
if num % 2==0:
    print("even number")
else:
    print("odd numbere")

#if...elif...else
num=int(input("enter a number:"))
if num>0:
    print("positive number:")
elif num<0:
    print("negative number:")
else:
    print("zero")
#if...elif...else
marks=int(input("enter your marks"))
if marks >=90:
    print("you will get a grade")
elif marks >=70:
    print("you will get b grade")
else:
    print("you will get c grade")