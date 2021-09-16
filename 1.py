#Given two words, print out a new word made up of the first, middle and last characters of each word.

#Ex:first_word = “America” second_word = “Japan” Expected output: AJrpan

s1=input("Enter 1st string:") 
s2=input("enter second string:")
s1_list=list(s1)
s2_list=list(s2)
#print(s1_list)
#print(s2_list)
#print(len(s1_list))
len_s1=round(len(s1_list)/2) #if it even length string then it will make round else it will take middile element from the given srings
len_s2=round(len(s2_list)/2)
new_word_list=list(s1_list[0]+s2_list[0]+s1_list[len_s1-1]+s2_list[len_s2]+s1_list[-1]+s2_list[-1])
new_word_str=''.join(str(e) for e in new_word_list)
print(new_word_str)





