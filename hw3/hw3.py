# imports for simulation and graph
import random									
import timeit
#import matplotlib.pyplot as plt
import sys 

# 2 different sorting algorithms with different complexity classes
# 1st: Bubble sorting with complexity level O(n**2)

def bubbleSort(alist):							# Bubble sort function taking a list as argument
  for passnum in range(len(alist)-1,0,-1):      # starts sorting the last number in the list
    for i in range(passnum):					# loops through the list 
      if alist[i]>alist[i+1]:                   # compares every two number in the list
        temp = alist[i] 						# following three lines make the swap
        alist[i] = alist[i+1]
        alist[i+1] = temp
  return alist   
        
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]  
# bubbleSort(alist)
# print(alist)

# 2nd: Merge sorting with complexity level O(nlogn)

def mergeSort(alist):                           # Merge sort function taking a list as argument
  if len(alist) > 1:							# splits into halves until there is 1 number in every half 
    mid = len(alist)//2							# the actual split happens
    lefthalf = alist[:mid]						# fist half of the splited list
    righthalf = alist[mid:]						# second half of the splited list
    
    mergeSort(lefthalf)							# recursive call for first half
    mergeSort(righthalf)						# recursive call for second half
    											# goes until there is 1 number in each list
    i = 0					
    j = 0
    k = 0
    while (i < len(lefthalf)) and (j < len(righthalf)):
      if lefthalf[i] < righthalf[j]:			# compares left half to right half of the list with single numbers
        alist[k] = lefthalf[i]					# indexes the smallest number (left half in this case) after comparison
        i = i+1									# move to the next for comparison
      else:										# if right half is smaller
        alist[k] = righthalf[j]					# index that one
        j = j+1									# move to the next for comparison
      k = k+1									# move to next index in the list
      
    while i < len(lefthalf):					# the next two while loops do the same 
      alist[k] = lefthalf[i]					# across right and left halves
      i = i+1
      k = k+1
      
    while j < len(righthalf):
      alist[k] = righthalf[j]
      j = j+1
      k = k+1
  return alist

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# mergeSort(alist)
# print(alist)

def sortingSim(n, sims):
  time_bubble = []
  time_merge = []
  for i in range(sims):
    samp = random.sample(range(n), n)			# generate a random sample of size n
    time1 = timeit.default_timer()				# set the timer to record sorting times
    bubbleSort(samp)							# run the bubble sort
    time2 = timeit.default_timer()				# record sorting time
    mergeSort(samp)								# run the merge sort
    time3 = timeit.default_timer()				# record sorting time
    time_bubble.append(time2 - time1)			# time passed for bubble sort
    time_merge.append(time3 - time2)			# time passed for merge sort
  return sum(time_bubble)/len(time_bubble), sum(time_merge)/len(time_merge) 
  												# mean sorting times
random.seed(12345) 								# for reproducibility

time_bubble = []
time_merge = []
n = 250											# sample size
for i in range(2,n):
  times = sortingSim(i, 10)						# runs 10 sims to give an average
  time_bubble.append(times[0])                  # first mean is bubble sort time
  time_merge.append(times[1])					# second mean is merge sort time

# p.s: I did the plotting in R, because I failed to install matplotlib

  