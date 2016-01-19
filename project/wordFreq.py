"""
Author: Paul Zenie
File: wordFreq.py
date: 11/30/14
"""

from wordData import *
from simplePlot import *

def wordFrequencies(words):
    """
    Calculates the frequency of each word in words and stores them in a list
    of WordCount objects
    :param words: A dictionary mapping words to a list of YearCount objects
    :return: A list of WordCount objects in decreasing order from most to least frequent
    """
    lst = []
    for word in words:
        count = totalOccurrences(word, words)
        lst.append(WordCount(word, count))
    lst.sort(key=lambda x: x.count, reverse = True)
    return lst

def main():
    """
    Prompts for filename and rank (between 1 and the length of the list)
    creates a dictionary words with the filename and a lst using the dictionary
    prints the object at the specified rank
    calls wordFreqPlot to plot the list
    :return:
    """
    filename = input("Enter file name: ")
    words = readWordFile(filename)
    lst = wordFrequencies(words)
    rank = input("Enter rank (1-" + str(len(lst)) + "): ")
    indx = int(rank) - 1
    print("Rank " + rank + ": " + str(lst[indx]))
    wordFreqPlot(lst)
    
if __name__ == '__main__':
    main()
