#------------------------------PALINDROME CHECKER------------------------------

word=input("\nEnter a word to check if it is a palindrome: ")
word=word.replace(" ", "").lower()
if word==word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")