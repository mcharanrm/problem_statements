#!/usr/bin/env python3

#how did i come to know ??
#sunday, last week, i was asked to solve this puzzle.

#puzzle description ??
#each word has two + two blanks and you need to fill up
#with same pair of letters to form a word

#examples ??
#_ _ I _ _  <------ "ONION" is the right answer


#some background ??
#there is no way am going to solve this puzzle because
#am too weak in vocabulary. So i need to explore my options ??

#problem solving ??
#I can see a pair of blanks for each question
#Prefix == Suffix
#And there are 26 alphabets
#I need to go through a loop of 26 * 26 = 676 Words for each question

#Out of 676 Words, only some are meaningful english words
#We need to findout what are those meaningful words ??

#To findout the meaningful english words, there is only one
#choice left, that is Dictionary Lookup

#So i decided to search for FREE dictionary API's to get
#my task done. And gladly i found this PyDictionary Library, which is
#sufficient enough to solve my problem

from PyDictionary import PyDictionary
import multiprocessing
from time import sleep



def solve_puzzles(seqno='', first_char='', middle_char='', last_char=''):
    dictionary=PyDictionary()
    for prefix in prefix_pairs:
        #print('reading ... {}'.format( first_char + prefix + middle_char + prefix + last_char))
        response = dictionary.meaning(first_char + prefix + middle_char + prefix + last_char,disable_errors=True)
        if response:
            print('{} {}'.format(seqno, first_char + prefix + middle_char + prefix + last_char))
            #break


if globals()['__name__'] == '__main__':
    #Create the required prefix pairs
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    prefix_pairs = list()
    for i in alphabets:
        for j in alphabets:
            prefix_pairs.append(i + j)

    puzzles = [
        { 1: ['', 'i', ''] },
        { 2: ['v', 'lat', 'n'] },
        { 3: ['h', 'dw', 'e'] },
        { 4: ['', 'res', 'e'] },
        { 5: ['p', 'sev', 'e'] },
        { 6: ['s', 'tim', 't'] },
        { 7: ['', 'da', 'ted'] },
        { 8: ['c', 'kb', 'k'] },
        { 9: ['lo','i', ''] },
        { 10: ['d', 'tingu', 'h'] },
        { 11: ['p', 'dl', ''] },
        { 12: ['s', 'ur', 'e'] },
        { 13: ['', 'p', 'zard'] },
        { 14: ['who', 'sa', ''] },
        { 15: ['', 'at', ''] },
        { 16: ['', 'od', 'rk'] },
        { 17: ['','ma',''] },
        { 18: ['', 'y', 'rd'] },
        { 19: ['h', 'rtbr', 'k'] },
        { 20: ['b','evol','t'] },
        { 21: ['c','diti',''] },
        { 22: ['an','cipa','on'] },
        { 23: ['', 'rri', 'lum'] },
        { 24: ['e','agi',''] },
        { 25: ['inc', 'p', 'ate'] }
    ]

    #create parallel process to speed up the work
    process_names = [ 'p' + str(item) for item in range(len(puzzles)) ]

    for item in range(len(puzzles)):
        process_names[item] = multiprocessing.Process(target=solve_puzzles, args=(item+1, puzzles[item][item+1][0], puzzles[item][item+1][1], puzzles[item][item+1][2]) )

    for item in range(len(puzzles)):
        print(process_names[item],end='|>|>|')
        process_names[item].start()
    print()

    elapsed = 0
    for item in range(len(puzzles)):
        while process_names[item].is_alive():
            #print('{} {} {} {}'.format('Total Elapsed time ... ',elapsed,process_names[item]))
            sleep(60)
            elapsed += 60
    print('{} {}'.format('Total elapsed time ... ',elapsed))
#    for item in range(len(puzzles)):
#        process_names[item].join()

#(venv) [cmusali@cmusali private]$ python thinking_caps.py
#<Process(Process-1, initial)>|>|>|<Process(Process-2, initial)>|>|>|<Process(Process-3, initial)>|>|>|
#<Process(Process-4, initial)>|>|>|<Process(Process-5, initial)>|>|>|<Process(Process-6, initial)>|>|>|
#<Process(Process-7, initial)>|>|>|<Process(Process-8, initial)>|>|>|<Process(Process-9, initial)>|>|>|
#<Process(Process-10, initial)>|>|>|<Process(Process-11, initial)>|>|>|<Process(Process-12, initial)>|>|>|
#<Process(Process-13, initial)>|>|>|<Process(Process-14, initial)>|>|>|<Process(Process-#15, initial)>|>|>|
#<Process(Process-16, initial)>|>|>|<Process(Process-17, initial)>|>|>|<Process(Process-18, initial)>|>|>|
#<Process(Process-19, initial)>|>|>|<Process(Process-20, initial)>|>|>|<Process(Process-21, initial)>|>|>|
#<Process(Process-22, initial)>|>|>|<Process(Process-23, initial)>|>|>|<Process(Process-24, initial)>|>|>|
#<Process(Process-25, initial)>|>|>|
#3 hardware
#1 asias
#12 saturate
#23 curriculum
#19 heartbreak
#11 peddled
#20 benevolent
#6 sentiment
#5 persevere
#13 haphazard
#2 violation
#15 isatis
#10 distinguish
#14 wholesale
#24 engaging
#9 longing
#1 onion
#8 cookbook
#15 orator
#25 incorporate
#21 condition
#22 anticipation
#17 tomato
#7 undaunted
#18 wayward
#16 woodwork
#Total elapsed time ...  3600
