"""
Author: Paul Zenie
File: letterFreq.py
Date: 11/30/14
"""

from wordData import *
from letterHist import *

def letterFreq(words):
    """
    Iterates through words to add up the number of times each letter occurs
    then divides that number the total number of letters and stores it in a list
    :param words: A dictionary mapping words to lists of YearCount objects
    :return: A list containing the relative Frequency of letters scaled by the total letter count in alphabetical order
    """
    totalLetters = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0   
    for word in words:
        count = totalOccurrences(word, words)
        letters = len(word)
        totalLetters = totalLetters + (count * letters)
        a += (word.count("a") * count)
        b += (word.count("b") * count)
        c += (word.count("c") * count)
        d += (word.count("d") * count)
        e += (word.count("e") * count)
        f += (word.count("f") * count)
        g += (word.count("g") * count)
        h += (word.count("h") * count)
        i += (word.count("i") * count)
        j += (word.count("j") * count)
        k += (word.count("k") * count)
        l += (word.count("l") * count)
        m += (word.count("m") * count)
        n += (word.count("n") * count)
        o += (word.count("o") * count)
        p += (word.count("p") * count)
        q += (word.count("q") * count)
        r += (word.count("r") * count)
        s += (word.count("s") * count)
        t += (word.count("t") * count) 
        u += (word.count("u") * count)
        v += (word.count("v") * count)
        w += (word.count("w") * count) 
        x += (word.count("x") * count)
        y += (word.count("y") * count)
        z += (word.count("z") * count)
    freqList = [(a/totalLetters),(b/totalLetters), (c/totalLetters), (d/totalLetters), (e/totalLetters), (f/totalLetters), (g/totalLetters), (h/totalLetters), (i/totalLetters), (j/totalLetters), (k/totalLetters), (l/totalLetters), (m/totalLetters), (n/totalLetters), (o/totalLetters), (p/totalLetters), (q/totalLetters), (r/totalLetters), (s/totalLetters), (t/totalLetters), (u/totalLetters), (v/totalLetters), (w/totalLetters), (x/totalLetters), (y/totalLetters), (z/totalLetters)]    
    return freqList
def main():
    """
    Prompts for filename and word, creates dictionary words using filename,
    prints total occurances of word, prints letter frequencies, and calls
    letterFreqPlot to plot the letter frequencies.
    :return: None
    """
    filename = input("Enter Filename: ")
    word = input("Enter word: ")
    words = readWordFile(filename)
    print("Total occurrences of " + word + ": " + str(totalOccurrences(word, words)))
    freqList = letterFreq(words)
    print("Letter frequencies: " + str(freqList))
    letterFreqPlot(freqList)

if __name__ == '__main__':
    main()
