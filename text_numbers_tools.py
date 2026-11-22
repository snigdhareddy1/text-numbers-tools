def count_words(sentence):
    words = sentence.split()
    return len(words)

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def reverse_sentence(sentence):
    return sentence[::-1]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main execution
user_sentence = input("Enter a sentence: ")
user_number = int(input("Enter a number: "))

print("Word Count:", count_words(user_sentence))
print("Longest Word:", find_longest_word(user_sentence))
print("Reversed Sentence:", reverse_sentence(user_sentence))

if is_prime(user_number):
    print(str(user_number) + " is a prime number.")
else:
    print(str(user_number) + " is not a prime number.")