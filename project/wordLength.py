"""
Author: Paul Zenie
File: wordLength.py
date: 11/30/14
"""
from wordData import *
from simplePlot import *

def occurrencesInYear(word, year, words):
    """
    Calculates the total number of occurrences of a word in a specific year
    :param word: The word in question passed in as a str
    :param year: The year in question (int)
    :param words: A dictionary mapping words to a list of YearCount objects
    :return: The number of occurrences of the word in the year (int)
    """
    if word in words:
        total = 0
        for i in words[word]:
            if i.year == year:
                total = i.count
        return total
    else:
        return 0
def averageWordLength(year, words):
    """
    Calculates the average word length in a specified year
    :param year: The year in question (int)
    :param words: A dictionary mapping words to a list of YearCount objects
    :return: The average word length of the year in question
    """
    total = 0
    i = 0
    x = 0
    for word in words:
        total = len(word)
        total *= occurrencesInYear(word, year, words)
        x += total
        i += occurrencesInYear(word, year, words)
    if i == 0:
        return 0
    else:
        average = x / i
        return average

def averageWordLengthYears(startYear, endYear, words):
    """
    Calculates the average word length in the specified range of years
    :param startYear: The start year (int)
    :param endYear: The end year (int)
    :param words: A dictionary mapping words to a list of YearCount objects
    :return: A list of float's that contains the average word lengths by year in the increasing order for years between startYear and endYear
    """
    i = startYear
    lst = []
    while i <= endYear:
        lst.append(averageWordLength(i, words))
        i += 1
    return lst

def main():
    """
    prompts for filename, word, year, year2, start year, and end year
    prints the number of occurences in a year of the word in the specified year
    prints the average word length for the year of second year
    creates a list of float's which are the average word lengths by year
    calls averageWordLengthPlot to plot the list
    """
    filename = input("Enter file name: ")
    words = readWordFile(filename)
    word = input("Enter a word: ")
    year = int(input("Enter a year: "))
    print("The word " + word + " occurred " + str(occurrencesInYear(word, year, words)) + " times in the year " + str(year))
    year2 = int(input("Enter a year: "))
    print("The average word length for the year " + str(year2) + " is " + str(averageWordLength(year2, words)) + " letters")
    startYear = int(input("Enter a start year: "))
    endYear = int(input("Enter an end year: "))
    lst = averageWordLengthYears(startYear, endYear, words)
    averageWordLengthPlot(startYear, endYear, lst)
    
if __name__ == '__main__':
    main()
