def pig_latin(sentence):
    # Write your solution here!
  #look at the first element, if its a,e,i,o,u return the sentence itself 
    #if not grab the first element and move it at the end 
    # also concatenate with "ay"
    vowels = ['a','e','i','o','u']
    words = sentence.split()       #words = "a", "w", "e", "s", "o", "m, "e"
    new_list = []

    for letters in words:
      if letters[0] in vowels:
        new_list.append(letters)
        # print(new_list)
      else:
          new_sentence = letters[1:] + letters[0] + "ay"
          new_list.append(new_sentence)
          # new_list = letters[1:] + letters[0] + "ay"
    
    return " ".join(new_list)
     
# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")