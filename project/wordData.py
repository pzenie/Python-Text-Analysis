'''
Author: Paul Zenie
File: wordData.py
Date: 11/30/14
'''

from rit_object import rit_object

class YearCount(rit_object):
    """
    yearCount class which holds the count and year
    """
    __slots__ = ('count', 'year')
    _types = (int, int)

class WordCount(rit_object):
    """
    wordCount class which holds the word and the count of that word
    """
    __slots__ = ('word', 'count')
    _types = (str, int)

def readWordFile(filename):
    """
    Opens the filename and stores the value of the file into a dictionary
    using a for loop
    :param filename: A string giving the name of a unigram csv file
    :return: A dictionary mapping words to lists of YearCount objects.
    """
    file = open("data/" + filename)
    words = dict()
    for line in file:
        currentLine = line.strip().split(",")
        word = currentLine[0]
        year = int(currentLine[1])
        count = int(currentLine[2])
        if word in words:
            lst.append(YearCount(count, year))
            words[word] = lst
        else:
            lst = [YearCount(count, year)]
            words[word] = lst
    return words

def totalOccurrences(word, words):
    """
    Chekcs to see if the word is in the dictionary, if not returns 0
    else adds up the count for each YearCount object for that word
    :param word: The word for which to calculate the count.
    :param words: A dictionary mapping words to lists of YearCount objects
    :return: The total number of times that a word has appeared in a book in the entire dataset
    """
    if word in words:
        total = 0
        for i in words[word]:
            total += i.count
        return total
    else:
        return 0

