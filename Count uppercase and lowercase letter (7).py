def count_case_letters(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

 
text = input("Enter a string: ")
upper_count, lower_count = count_case_letters(text)
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
