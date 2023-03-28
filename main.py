def main(book):
    print("--- Begin report of books/frankenstein.txt ---")
    count_words(book)
    count_letters(book)
    print("--- End report ---")

book = None

with open('./books/frankenstein.txt') as f:
    book = f.read()
    

def count_words(text):
    return print(len(text.split()))

def count_letters(text):
    count = {}    
    for letter in text.lower():
        if letter.isalpha():
            if letter not in count:
                count[letter] = 1
            else: count[letter] += 1

    new_list = list(count.items())
    new_list.sort()
    
    for letter in new_list:
        print(f"The {letter[0]} character was found {letter[1]} times")  

    
main(book)