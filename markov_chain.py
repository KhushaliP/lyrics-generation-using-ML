# -*- coding: utf-8 -*-



"""
simple Markov chain function that creates a dictionary:

The keys should be all of the words in the corpus
The values should be a list of the words that follow the keys
"""
def markov_chain(lyrics):
    #lyrics- corpus of strings where each string is a lyric
    #This is a Bigram markov chain. So the prediciton will be
    #based on previous two words.
    chain = {(None, "START"): []} #dict- beginning is None, there are no prev words
    
    for lyric in lyrics:
        lyric_newlines = lyric.replace('\n', '<N>')
        
        last_two = (None, "START")
        for word in lyric_newlines.split():
            chain[last_two].append(word)
            #Shift the current bigram
            last_two = (last_two[1], word)
            if last_two not in chain:
                chain[last_two]=[]
        chain[last_two].append("END")
    return chain
import pickle
lyrics = pickle.load(open("lyrics.pkl", "rb"))

#Training the markov chain over all the lyrics
chain = markov_chain(lyrics)


"""

Predicting the lyrics
Input is the chain (dict of words)
"""
import random
def generate_lyrics(chain):
    words = []
    #generate the first word
    word = random.choice(chain[(None, "START")])
    words.append(word)
    
    last_two = (None, "START")
    while words[-1] != "END":
        #Generate the next word
        word = random.choice(chain[last_two])
        words.append(word)
        #Shift the bigram
        last_two = (last_two[1], words[-1])
    #Join the words together into a string with line breaks
    lyrics= " ".join(words[:-1])
    return "\n".join(lyrics.split("<N>"))

print(generate_lyrics(chain))