numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Bharathi", "nayana", "Di", "Mokshu", "Mia", "Varma"]
words = ["apple", "orange", "banana", "lite", "blueberry", "apricot"]

def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Even numbers using function:", even_numbers)

even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda:", even_numbers_lambda)

names_long = list(filter(lambda name: len(name) >= 3, names))
print("Names with 3+ characters:", names_long)

words_with_a = list(filter(lambda word: "a" in word.lower(), words))
print("Words containing 'a':", words_with_a)
