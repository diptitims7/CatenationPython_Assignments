a=10
b=20
c=30
Avg=((a+b+c)/3)
print("Average",Avg)
if Avg>a and Avg>b and Avg>c:
    print("Aberage is higher than a,,b,c")
if Avg>a and Avg>b:
    print("Average is higher than abc")
elif Avg>a and Avg>c:
    print("Average is higher than a,c")
elif Avg>a:
    print("Average is just higher than a")
elif Avg>b:
    print("Average is just higher than b")
elif Avg>c:
    print("Average is just higher than c")  
