#Swapping two numbers without using 3 rd variable

#Using arethematic
a=32
b=24

a=a+b
b=a-b
a=a-b

print(f"Swapped values are : a={a} , b={b}")

#Using XOR

x=52
y=23

x=x^y
y=x^y 
x=x^y

print(f"Swapped values: x={x} , y={y}")
