string=input("Enter string : ")
s=input("Enter Letter for count: ")
count=0
for i in string:
    if i in s:
        count+=1
print(count)