def censor(text, word):
    #This turns our phrase into a list so we can iterate through it word by word.
    text = text.split()
    
    #This finds the word that equals our 'word', and then replaces it with '*' equal to the length of the word.
    for index, i in enumerate(text):
        if i == word:
            i = i.replace(i, ("*" * len(i)))
            text[index] = i
        else:
            pass
    
    #This turns the list back into a phrase.
    text = " ".join(text)
    return text
    
text = "this bitch is tripping damn bitch"
word = "bitch"
print(censor(text, word))
