import os
import csv
import random

# Creating empty lists
adjective = []
noun=[]
verb=[]
sentence = []
madlib_lib = []
madlib_order = []


def load_csv_to_list(path_to_file):
        read_csv_list = []
        if os.path.isfile(path_to_file) and path_to_file.endswith('.csv'):  # Validate Path to file exists
            with open(path_to_file, 'r') as f:
                csv_file_reader = csv.reader(f)  # Read the csv file
                for row in csv_file_reader:
                    if row:
                        read_csv_list.append(row[0])  # Append the rows of the file to the list
                    else:
                        continue
                return read_csv_list

def shuffle(sequence):
    tshuffled_list = list(sequence)  # List that will be returned
    array_len = len(tshuffled_list)
    assert array_len > 1, 'Array is too short to shuffle!'
    # Shuffling logic
    for index in range(array_len):
        swap = random.randrange(array_len - 1)
        swap += swap >= index
        tshuffled_list[index], tshuffled_list[swap] = tshuffled_list[swap], tshuffled_list[index]
    return tshuffled_list

def load_mad_lib_resource(path):
    tshuffled_list = []
    global noun, verb, adjective, sentence
    # Call load_csv_to_list
    verb = load_csv_to_list(os.path.join(path,'verbs.csv'))
    noun = load_csv_to_list(os.path.join(path,'nouns.csv'))
    adjective = load_csv_to_list(os.path.join(path,'adjectives.csv'))
    sentence = load_csv_to_list(os.path.join(path,'sentences.csv'))

    #SHUFFLING THE DATA
    verb = shuffle(verb)
    noun = shuffle(noun)
    adjective = shuffle(adjective)
    sentence = shuffle(sentence)
    print (verb)
    # Append the list to the tuple
    tshuffled_list.append(verb)
    tshuffled_list.append(noun)
    tshuffled_list.append(adjective)
    tshuffled_list.append(sentence)

    return tshuffled_list  # Return a tuple of the shuffled list
def play_game(user_sentences,lower_bound, upper_bound):
    global username,madlib_lib, verb, noun, sentence, adjective, min_val, max_val

    is_keep_playing = None
    while is_keep_playing != 'n': # To keep asking the user if he wants to play again
        user_inp = input("Please provide a number between {} and {}".format(lower_bound, upper_bound))

        try:
            user_number = int(user_inp.strip().lower())
        except:
            print("Sorry the value provided is not an integer.") # Input validation
            user_number = None

        if user_number is not None: # Input validation
            if user_number < min_val:
                print("Sorry the number provided is too small (lower than {})".format(min_val))
            elif user_number > max_val:
                print("Sorry the number provided is too big (greater than {})".format(max_val))
            else:
                sent_idx = random.randint(user_number, max_val) % len(sentence)
                nounn_idx = random.randint(user_number, max_val) % len(noun)
                verbb_idx = random.randint(user_number, max_val) % len(verb)
                adjectivee_idx = random.randint(user_number, max_val) % len(adjective)

                # generate the mad lib sentence
                sent = sentence[sent_idx].format(nounn=noun[nounn_idx],verbb=verb[verbb_idx],adjectivee=adjective[adjectivee_idx])

                #GENERATE THE SENTENCES AND WRITE TO THE FILE IF NOT ALREADY SAVED
                print("The sentence you have created is: ")
                print(sent)
                #PRINT ALL OF THE SENTENCES FOR THE USER THUS FAR
                if madlib_lib is []:
                    csv_file_path = os.path.join(username,username+'.csv')
                    f = open(csv_file_path,'a')
                    writer = csv.writer(f, lineterminator='\n')
                    writer.writerow([sent])
                    f.close()
                else:
                    csv_file_path = os.path.join(username,username+'.csv')
                    f = open(csv_file_path,'r')
                    reader = csv.reader(f)
                    for row in reader:
                        user_sentence.append(row[0])
                    f.close()
                    if sent in user_sentence: # Checking if sentence already exists in the madlib library
                        print("Your sentence already exists in the madlib")
                    else: # Append the sentence to the csv file for the user
                        sentence_length = []
                        csv_file_path = os.path.join(username,username+'.csv')
                        f = open(csv_file_path,'r')
                        reader = csv.reader(f)
                        for row in reader:
                            sentence_length.append(row[0])
                        size_of_sentences = len(sentence_length) + 1
                        csv_file_path = os.path.join(username,username+'.csv')
                        f = open(csv_file_path,'a')
                        writer = csv.writer(f)
                        writer.writerow([sent,size_of_sentences])
                        f.close()

        # PRINT ALL OF THE SENTENCES FOR THE USER THUS FAR
        print("Your madlib so far:")
        csv_file_path = os.path.join(username,username+'.csv')
        f = open(csv_file_path,'r')
        reader = csv.reader(f)
        madlib_lib = []
        for row in reader:
            madlib_lib.append(row[0])
        print(madlib_lib)


        is_keep_playing = None  # reset

        while 'y' != is_keep_playing and 'n' != is_keep_playing:
            is_keep_playing = input("Do you want to keep playing? y / n")
            try:
                is_keep_playing = is_keep_playing.strip().lower()
            except:
                is_keep_playing = None

            if 'y' != is_keep_playing and 'n' != is_keep_playing:
                print("Sorry, I did not get that.")
print("Enter username")
username = input()

# VERIFY THE A USER NAME WAS ENTERED ELSE EXIT THE PROGRAM
if not username:
    exit()
else:
    if os.path.isdir(username): # Checking if user exists
        print("Existing User")
        print("Checking if user's game exists")
        path_to_user = os.path.join(username,username+'.csv')
        if os.path.isfile(path_to_user):
            print("Your game exists. Loading your game") # Load the game for the existing user
            user_file = open(path_to_user, 'r')
            csv_reader = csv.reader(user_file)
            for data in csv_reader:
                madlib_lib.append(data[0])
                madlib_order.append(data[1])
            user_file.close()
            print("madlib Library:")
            print(madlib_lib)
        else:
            print("No game exists. Creating your game")  # Create a new csv for the user
            path_to_user = os.path.join(username, username+'.csv')
            user_file = open(path_to_user, 'w')
            user_file.close()
    else:
        print("New User") # Creating a csv for the new user
        print("Creating user")
        os.makedirs(username)
        print("Create your game")
        path_to_user= os.path.join(username, username+'.csv')
        user_file = open(path_to_user, 'w')
        user_file.close()
user_sentence = madlib_lib
# boundaries
min_val = 0
max_val = max(
        len(sentence),
        len(noun),
        len(verb),
        len(adjective),)

play_game(user_sentence, min_val, max_val)
print("Bye!")
