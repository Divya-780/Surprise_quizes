#Write a program to read lines from a text file and print the words which are less than 5 characters.

s=input("enter any string:")
c=0
s1=list(s)
for i in s1:
    if i==" ":
        continue
    for char in i:
            c=c+1
    if(c<=5):
        print(char)
    
