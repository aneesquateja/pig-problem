def pig_latin(sentence):
   # split the sentence into a list of words
    words = sentence.split()

    # for each new word, use the helper to convert the word
    # into pig latin. Put those words into new_words
    new_words = []
    for word in words:
        new_words.append(pig_latin_single_word(word))

    # Join all the words together with spaces to make the final string
    return " ".join(new_words)

    # Helper that converts a single word to pig latin
def pig_latin_single_word(word):
    # if the first letter is a vowel, don't change anything
    if word[0] in 'aeiou':
        return word

    # otherwise, if it's a consonant
    # start with all but the first letter of the word
    new_word = word[1:]
    # add the first letter to the end of the word
    new_word += word[0]
    # add the suffix
    new_word += "ay"
    return new_word
# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")