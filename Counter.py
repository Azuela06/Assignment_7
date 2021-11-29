
def Counter_wvc():
    vowel_count = 0
    consonant_count = 0
    word_count=0
    vowels = ['a','e','i','o','u']
    word = [" "]
    for sentence in statement:
        if sentence in vowels:
            vowel_count += 1
        elif sentence in word:
            word_count += 1
        else:
            consonant_count += 1
    return vowel_count, consonant_count, word_count + 1
    
def final(Vowels, consonants, words):
    print(f"The total number of vowels are {Vowels}, The number of consonants are {consonants}, and the number of words are {words}.")

print("Hi, this is a counter of vowels, consonants, and words in your statement and even essays")

statement = input("Give any statement or sentence: ")

Vowels, consonants, words = Counter_wvc()

final(Vowels, consonants, words)