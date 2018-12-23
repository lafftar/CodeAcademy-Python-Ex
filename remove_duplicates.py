def remove_duplicates(dupes):
    deduped = []
    for number in dupes:
        if number not in deduped:
            deduped.append(number)
    return deduped
