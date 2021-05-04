def checkIfPangram(sentence):
    whole = list('abcdefghijklmnopqrstuvwxyz')
    for w in whole:
        if w not in sentence:
            return False
    return True

print(checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))
print(checkIfPangram('leetcode'))