"""
Created on Wed Nov 17 23:29:51 2021

@author: Burak Alanyalıoğlu (@felsefesinde on GitHub)
"""

def word_reverser(phrase):
    list_of_words = phrase.split(" ")
    
    """if you want to see how our list 
    looks like just run also the line commented
    below:
    print(list_of_words)
    """
    new_phrase = ""
    for i in range (0, len(list_of_words)):
        word = list_of_words[i]
        new_phrase = word + " " + new_phrase
    #Let's remove the extra space " " at the end of our string
    new_phrase = new_phrase.strip()
    return new_phrase

print(word_reverser('Codecademy rules apply here'))