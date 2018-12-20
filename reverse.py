def reverse(text):

    indo = []
    final = ""
    text = str(text)

    #Finds where the index ends
    for index, n in enumerate(text):
        indo.append(index)

    #Finds the max index, then makes a list of numbers counting backwards from the max index to 0
    indo_m = max(indo)
    rng = range(indo_m, -1, -1)

    #Iterates through the list, adding each item to the final variable >> text[4] to text[1]
    for i in rng:
        final += (text[i])
    return final
print(reverse("Python!"))
