import random

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    word_bank = ["join", "love", "smile", "cloud", "head"]
    for _ in range(quantity):
        random_word = random.choice(word_bank)
        words_list.append(random_word)

def main():
    # Create a list of numbers
    numbers = [16.2, 75.1, 52.3]
    
    # Print the initial list of numbers
    print("numbers", numbers)
    
    # Append one number to the numbers list
    append_random_numbers(numbers)
    print("numbers", numbers)
    
    # Append three numbers to the numbers list
    append_random_numbers(numbers, 3)
    print("numbers", numbers)

    # Stretch Challenge: Create a list of words
    words = ["love", "cloud"]
    
    # Print the initial list of words
    print("words", words)
    
    # Append two words to the words list
    append_random_words(words, 2)
    print("words", words)

if __name__ == "__main__":
    main()
