name = input("Enter your name : ").strip()  
age = input("Enter your age : ").strip()
subject = input("Enter your favorite subject : ").strip()
quote = input("Enter your favorite quote : ").strip()

name = name.capitalize()

paragraph = f"""
Student Information:
Name: {name}
Age: {age}
Favorite Subject: {subject}
Favorite Quote: "{quote}"
"""
print(paragraph)

letters = list(name)
if len(letters) >= 1:
    print("First letter of the list:", letters[0])
    print("Last letter of the list:", letters[-1])
else:
    print("No letters in the list!")