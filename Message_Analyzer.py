Sentence=input("Enter a sentence: ")
if Sentence.endswith('.'):
    print("It is a sentence")
elif Sentence.endswith('?'):
    print("It is a quetion")
elif Sentence.endswith('!'):
    print("It is an exclamation")
else:
    print("It is an Unknown type of message")