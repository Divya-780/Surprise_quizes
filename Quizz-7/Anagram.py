#Anagram
'''
s1=input("enter first string::")
s2=input("enter second string::")
s1=s1.lower()
s2=s2.lower()
sort_s1=sorted(s1)
sort_s2=sorted(s2)
print(sort_s1)
print(sort_s2)
if len(sort_s1)==len(sort_s2):
    if(sort_s1==sort_s2):
        print("true")
    else:
        print("false")
else:
    print("false")'''

#Functions:

def checkAnagram(s1,s2):
    #checking lengths of the two strings equal or not
    if(len(s1)==len(s2)):
        #converting strings into lower case
        s1=s1.lower()       
        s2=s2.lower()
        #arranging letters in alpahabatical order
        sort_s1=sorted(s1)
        sort_s2=sorted(s2)
        #after arraging the words,check equal or not
        if(sort_s1==sort_s2):
            return True
        else:
            return False
    else:
        return False
a=input("enter a first string::")
b=input("enter second string::")
print(checkAnagram(a,b))
