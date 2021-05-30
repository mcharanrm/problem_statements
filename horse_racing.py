#!/usr/bin/env python3


#It is a stright forward thing because logic is not mine

#link to original problem statement
#https://www.youtube.com/watch?v=i-xqRDwpilM


import time
import concurrent.futures


def start_racing(horse_number):
    #not the horse racing but doing the similar thing
    #race among threads to print 100 natural numbers with sleep 1 sec

    start_time = time.time()
    for number in range(1,10):
        print(number,end='')
        time.sleep(1)
    end_time = time.time()
    tmp_list.append({ horse_number: end_time - start_time })

def sort_race_timings():

#I read this logic long time ago and it is super easy to implement it
#>>> A
#[5, 4, 3, 2, 1]
#>>>
#>>> A=[1,2,3,4,5]
#>>> for i in range(len(A)):
#...     tmp_i = A[i];counter = 0
#...     for j in range(i,len(A)):
#...         if A[j] < tmp_i:
#...             tmp_i = A[j]
#...             tmp_j_index = j
#...             counter += 1
#...     if counter > 0:
#...         tmp_i = A[i]
#...         A[i] = A[tmp_j_index]
#...         A[tmp_j_index] = tmp_i
#...
#>>> A
#[1, 2, 3, 4, 5]
#>>>
#>>>
#>>> A=[5,4,3,2,1]
#>>> for i in range(len(A)):
#...     tmp_i = A[i];counter = 0
#...     for j in range(i,len(A)):
#...         if A[j] < tmp_i:
#...             tmp_i = A[j]
#...             tmp_j_index = j
#...             counter += 1
#...     if counter > 0:
#...         tmp_i = A[i]
#...         A[i] = A[tmp_j_index]
#...         A[tmp_j_index] = tmp_i
#...
#>>> A
#[1, 2, 3, 4, 5]
#>>>
#>>>
#>>> A=[2,3,5,4,1]
#>>> for i in range(len(A)):
#...     tmp_i = A[i];counter = 0
#...     for j in range(i,len(A)):
#...         if A[j] < tmp_i:
#...             tmp_i = A[j]
#...             tmp_j_index = j
#...             counter += 1
#...     if counter > 0:
#...         tmp_i = A[i]
#...         A[i] = A[tmp_j_index]
#...         A[tmp_j_index] = tmp_i
#...
#>>> A
#[1, 2, 3, 4, 5]

#...
#>>> A
#[1, 2, 3, 4, 5]
    race_value = []
    for item in race_time:
        for h_number, h_time in item.items():
            race_value.append(h_time)

    for i in range(len(race_value)):
        tmp_i = race_value[i];counter = 0
        for j in range(i,len(race_value)):
            #print('reading values - i: {}  j:{}'.format(race_value[i],race_value[j]))
            if race_value[j] < tmp_i:
                #print('Lowest values {}, j_index - {}'.format(race_value[j],j))
                #time.sleep(1)
                tmp_i = race_value[j]
                tmp_j_index = j
                counter += 1
        if counter > 0:
            tmp_i = race_time[i]
            tmp_rv_i = race_value[i]
            #print('swapping .... {} --- {} ---- index -- {}'.format(a[i], a[tmp_j_index],tmp_j_index))
            race_time[i] = race_time[tmp_j_index]
            race_value[i] = race_value[tmp_j_index]
            race_time[tmp_j_index] = tmp_i
            race_value[tmp_j_index] = tmp_rv_i

if globals()['__name__'] == '__main__':
    #get the race horse names or numbers
    race_horse_numbers = [ 'H' + str(item) for item in range(1,26) ]
    race_time = list()
    #only 5 horses can race on the track at any particular moment
    #split the total available horse list into smaller groups and
    #each group should have 5 horses

    i = 0; j = 5; k = 25
    while j <= k:
        #start the racing
        tmp_list = list()
        print('start horse racing of {}'.format(race_horse_numbers[i:j:1]))
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(start_racing, race_horse_numbers[i:j:1])

        i += 5; j += 5
        race_time.append(tmp_list)
        print('\n\n')

    #perform sorting on the race timings
    race_time = [ item for race in race_time for item in race ]
    sort_race_timings()

    print('###Final result {}'.format(race_time))
    print()

    print('+++ Score board: Top 3 horses are listed below')
    for i in range(1,4):
        print('{}'.format(race_time[-i]))
