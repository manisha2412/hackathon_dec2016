
"""Write a function which accepts 2 params - a string and a word and computes the following:

A. Count occurrences of the word in the string
B. Remove that word from string
C. Append same word equal to number of occurrences in string.
"""


def main():
    mystr = raw_input("Enter a strings")
    word = raw_input("Enter a word you want to count")
    a=[]
    a = mystr.split()
    t=a.count(word)
    print t
    for f in a:
        if f == word:
            a.remove(f)
    m=0
    while (m<t):
        a.append(word)
        m+=1
    print ' '.join(a)
main()