#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------
# Modify the program so that the most_frequent function works.
#----------------------------------------------------------------------------

import string

def sentence_to_words(sentence):
    sentence = sentence.lower()
    reduced_sentence = ""
    for character in sentence:
        if character in string.ascii_lowercase or character == " ":
            reduced_sentence += character
    return reduced_sentence

def update(dictionary, words):
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

def most_frequent(dictionary):
    if len(dictionary) == 0:
        print("Emtpy dictionary. No word occur more frequently than others.\n")
    else:
        most_common_word = ""
        highest_frequency = 0
        for key, value in dictionary.items():
            if value > highest_frequency:
                most_common_word = key
                highest_frequency = value
        print(most_common_word, "occurs", highest_frequency, "times.\n")

def main():
    proceed = "yes"
    word_dictionary = {}
    while proceed == "yes" or proceed == "y":
        sentence = input("Please enter a sentence: ")
        words = sentence_to_words(sentence)
        word_list = words.split()
        update(word_dictionary, word_list)
        print(word_dictionary)
        most_frequent(word_dictionary)
        proceed = input("Woud you like to continue? ")
        proceed = proceed.lower()

main()
