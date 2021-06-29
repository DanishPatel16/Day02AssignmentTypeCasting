# # Typecasting Trials

a = "10"
b = 20

a=int(a)

c = a+b

print(a)

print (a,type(a))

#  Output:
#         10
#         10 <class 'int'>

x=input("ENTER THE NUMBER YOU WANT ADD : ")
print(x,type(x))
x=int(x)
print(x,type(x))
y=10

z=x+y
print(z,type(z))

# Output:
#         ENTER THE NUMBER YOU WANT ADD : 25
#         25 <class 'str'>
#         25 <class 'int'>
#         35 <class 'int'>


# trial off all 4 functions

p = "1000"
print(p,type(p))
p=int(p)
print(p,type(p))

#     Output:
#             1000 <class 'str'>
#             1000 <class 'int'>

q = 1000
print(q,type(q))
q=float(q)
print(q,type(q))


q = "1000"
print(q,type(q))
q=float(q)
print(q,type(q))

# Output:
#         1000 <class 'int'>
#         1000.0 <class 'float'>
#         1000 <class 'str'>
#         1000.0 <class 'float'>

q = 1000.50
print(q,type(q))
q=int(q)
print(q,type(q))

s= 1000.78
print(s,type(s))
s=int(s)
print(s,type(s))

    # Output:
    #         1000.5 <class 'float'>
    #         1000 <class 'int'>
    #         1000.78 <class 'float'>
    #         1000 <class 'int'>

