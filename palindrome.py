word = input("Enter a word: ")

# reverse the word
reverse_word = word[::-1]

if word.lower() == reverse_word.lower():
    print("It is a palindrome")
else:
    print("It is not a palindrome")
