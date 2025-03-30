
# Count the number of words and letters in a given sentence.
# •	Skills Used: Strings, loops, dictionaries
# •	Bonus: Count how many times each word appears.

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
letter_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
    for l in w:
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1

print("Word count:", word_count)
print("Letter count:", letter_count)