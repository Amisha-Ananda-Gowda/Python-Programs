sentence=input("Enter a sentence:")
digit=0
upper=0
lower=0
word=sentence.split()
words=len(word)
for i in sentence:
    if i.isdigit():
        digit+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("Number of words : ",words)
print("Number of digits : ",digit)
print("Number of uppercase letters : ",upper)
print("Number of lowercase letters : ",lower)