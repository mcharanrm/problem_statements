#!/usr/bin/env python3

from math import floor
import time

# Below code snippet simply display rotated version of a given Matrix
#>>> A=[
#... [1,2,3],
#... [4,5,6],
#... [7,8,9]
#... ]
#>>> for j in range(len(A)):
#...     for i in range(len(A)-1,-1,-1):
#...             print('{}'.format(A[i][j]),end=' ')
#...     print()
#...
#7 4 1
#8 5 2
#9 6 3

#But the above code is not what we are looking for
#We are looking for something like - Rotation of indices

#It took me a while to compute the general solution that
#can help us to rotate the indices of both event length and
#odd lenght square matrix


if globals()['__name__'] == '__main__':
    #Declare the matrix here
    A = [[1,2,3,4,5,6,7,8,9,10],
         [11,12,13,14,15,16,17,18,19,20],
         [21,22,23,24,25,26,27,28,29,30],
         [31,32,33,34,35,36,37,38,39,40],
         [41,42,43,44,45,46,47,48,49,50],
         [51,52,53,54,55,56,57,58,59,60],
         [61,62,63,64,65,66,67,68,69,70],
         [71,72,73,74,75,76,77,78,79,80],
         [81,82,83,84,85,86,87,88,89,90],
         [91,92,93,94,95,96,97,98,99,100]
    ]
    print('+++ Before Matrix Rotation')
    for item in A:
        for inner_item in item:
            print('{}'.format(inner_item),end=' ')
        print()
    #Declare special index variables
    ai = 0; aj = 0
    bi = 0; bj = len(A) - 1
    ci = len(A) - 1; cj = 0
    di = len(A) - 1; dj = len(A) - 1

    #Initialize the required no of loop for matrix rotation
    for i in range(floor(len(A)/2)):
        #We need to preseve the special index variables from being modified
        #So create copy of those variables
        tai = ai; taj = aj
        tbi = bi; tbj = bj
        tci = ci; tcj = cj
        tdi = di; tdj = dj

        #Start the matrix rotation
        for r1 in range(tai,tbj):
            #print('rotating .....',A[tai][taj])
            #time.sleep(5)
            tmp = A[tbi][tbj]
            A[tbi][tbj] = A[tai][taj]
            A[tai][taj] = tmp

            taj+=1
            tbi+=1
        #Restore the original values of tai and taj
        tai = ai; taj = aj
        #print('Rotated ',A)

        #Start more matrix rotation
        for r2 in range(tai,tbj):
            #print('rotating .....',A[tai][taj])
            #time.sleep(5)
            tmp = A[tdi][tdj]
            A[tdi][tdj] = A[tai][taj]
            A[tai][taj] = tmp

            taj+=1
            tdj-=1
        #Restore the original values of tai and taj
        tai = ai; taj = aj
        #print('Rotated ',A)

        #Start more matrix rotation
        for r3 in range(tai,tbj):
            #print('rotating .....',A[tai][taj])
            #time.sleep(5)
            tmp = A[tci][tcj]
            A[tci][tcj] = A[tai][taj]
            A[tai][taj] = tmp

            taj+=1
            tci-=1

        #Do the matrix rotation on different rows and columns
        ai+=1; aj+=1
        bi+=1; bj-=1
        ci-=1; cj+=1
        di-=1; dj-=1
        #print(ai,aj,bi,bj,ci,cj,di,dj)

    print('\n')
    print('+++ After Matrix Rotation')
    for item in A:
        for inner_item in item:
            print('{}'.format(inner_item),end=' ')
        print()


#[cmusali@cmusali honey_told_me_to]$ python3 matrix_rotation_90_degrees.py
#+++ Before Matrix Rotation - [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#+++ After Matrix Rotation - [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
#[cmusali@cmusali honey_told_me_to]$ vi matrix_rotation_90_degrees.py
#[cmusali@cmusali honey_told_me_to]$ python3 matrix_rotation_90_degrees.py
#+++ Before Matrix Rotation - [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#+++ After Matrix Rotation - [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
#[cmusali@cmusali honey_told_me_to]$ python3 matrix_rotation_90_degrees.py
#+++ Before Matrix Rotation - [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
#+++ After Matrix Rotation - [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]

#[cmusali@cmusali private]$ python3 matrix_rotation_90_degrees.py
#+++ Before Matrix Rotation
#1 2 3 4 5 6 7 8 9 10
#11 12 13 14 15 16 17 18 19 20
#21 22 23 24 25 26 27 28 29 30
#31 32 33 34 35 36 37 38 39 40
#41 42 43 44 45 46 47 48 49 50
#51 52 53 54 55 56 57 58 59 60
#61 62 63 64 65 66 67 68 69 70
#71 72 73 74 75 76 77 78 79 80
#81 82 83 84 85 86 87 88 89 90
#91 92 93 94 95 96 97 98 99 100
#
#
#+++ After Matrix Rotation
#91 81 71 61 51 41 31 21 11 1
#92 82 72 62 52 42 32 22 12 2
#93 83 73 63 53 43 33 23 13 3
#94 84 74 64 54 44 34 24 14 4
#95 85 75 65 55 45 35 25 15 5
#96 86 76 66 56 46 36 26 16 6
#97 87 77 67 57 47 37 27 17 7
#98 88 78 68 58 48 38 28 18 8
#99 89 79 69 59 49 39 29 19 9
#100 90 80 70 60 50 40 30 20 10 
