def anti_vowel(text):
    result = ""
    vowels = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")
    for i in text:
        if i not in vowels:
            result += i
        else:
            pass
    return result
print(anti_vowel("Hello"))
