#making the lists
noun = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
verb = ["pay", "put", "read", "run", "say", "see"]
adjective = ["other", "new", "good", "high", "old"]
sentence= ["All the king’s {adjective} horses and all the king’s dainty {noun} could not {verb} scrambled egg man back together again", "Man {verb} on a {adjective} {noun}.","{noun} {verb} to the {adjective} ground."]
#assigning the values
cond = 'y' or cond =='Y'
word_noun = 0
word_verb = 0
word_adjective = 0
sentence_temp = 0
while cond == "y" or cond =="Y":
    cond = input("Enter y to continue or n to exit the game")
    if cond == "n" or cond == "N":
        print("the game has ended")
        exit()
    elif cond == "Y" or cond =="y":
        inpt = int(input("Please enter an integer greater than 0:"))
        if inpt < 0 or type(inpt) != int:
            print("Oops!Thats not greater than 0 or the number is not valid")
        else:
            word_noun = inpt % len(noun)
            word_verb = inpt % len(verb)
            word_adjective = inpt % len(adjective)
            sentence_temp = inpt % len(sentence)
            print(sentence[sentence_temp].replace('{noun}','{0}').replace('{verb}','{1}').replace('{adjective}','{2}').format(noun[word_noun],verb[word_verb],adjective[word_adjective]))
