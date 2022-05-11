import xlwt
from xlwt import Workbook

import random
from random import seed, randint

import time

# Sets seed
seed(42)


# Basic Recursion
def binCoeffRecursion(n, k):
    
    # Base Cases
    if k==0 or k==n:
        return 1
    
    return binCoeffRecursion(n-1, k) + binCoeffRecursion(n-1, k-1)


# Dynamic Bottom-Top 
def binCoeffDynamic(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):

            # Base Cases
            if j==0 or j==i:
                C[i][j]=1
            
            C[i][j] = C[i-1][j-1]+C[i-1][j]
    
    return C[n][k]


# Both functions below use Top-Bottom Memoization approach
def binCoeffMemoTable(n, k, dupe):
    
    # Checks if value is in look up table
    # If so, return that value
    if dupe[n][k] != -1:
        return dupe[n][k]
    
    # Base Cases
    if k==0 or k==n:
        dupe[n][k]=1
        return dupe[n][k]

    # Else, put new value in table
    dupe[n][k] = binCoeffMemoTable(n-1,k-1, dupe) + binCoeffMemoTable(n-1, k, dupe)

    return dupe[n][k]


def binCoeffMemo(n,k):
    dupe = [[-1 for i in range(k+1)] for j in range(n+1)]
    return binCoeffMemoTable(n,k,dupe)


# Generates a list of 500 pairings of n and k where n<25
def nkVals():

    # Declare variables
    lst = []
    nk = [0,0]

    # Get two random numbers from 2 to 25
    # Put them in the nk list and add that list to the end of lst
    # Repeat until 500 data points
    for i in range(500):
        vals = randint(2,25), randint(2,25)
        nk[0] = max(vals)
        nk[1] = min(vals)
        print(nk)

        lst.append(nk[:])
    print(lst)
        
    
    return lst
            


# The below three functions all compute the time it takes for each binomial call
def recurTime(wb, lst):
    
    counter = 0
    # Creates Excell Sheets
    sheet1.write(1, 1, "Recursion Times (s)")

    # Calculates the time it takes for each function call and adds them to the data sheet
    for i in range(len(lst)):

        t0 = time.perf_counter()
        binCoeffRecursion(lst[i][0],lst[i][1])
        t1 = time.perf_counter()

        counter += 1

        timeTaken = t1 - t0
        sheet1.write(counter+1, 1, timeTaken)

def dynamTime(wb, lst):
    
    counter = 0 
    # Creates Excel Sheets
    sheet1.write(1,2,"Dynamic Times (s)")

    # Calculates the time it takes for each function call and adds them to the data sheet
    for i in range(len(lst)):

        t0 = time.perf_counter()
        binCoeffDynamic(lst[i][0],lst[i][1])
        t1 = time.perf_counter()

        counter += 1

        timeTaken = t1 - t0
        sheet1.write(counter+1, 2, timeTaken)

def memoTime(wb, lst):

    counter = 0
    # Creates Excel Sheets
    sheet1.write(1,3, "Memoization Times (s)")
    # Calculates the time it takes for each function call and adds them to the data sheet
    for i in range(len(lst)):

        t0 = time.perf_counter()
        binCoeffDynamic(lst[i][0],lst[i][1])
        t1 = time.perf_counter()

        counter += 1

        timeTaken = t1 - t0
        sheet1.write(counter+1, 3, timeTaken)

# Driver Code
if __name__ == "__main__":
    
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok= True)


    
    lst = nkVals()

    t0 = time.perf_counter()
    dynamTime(wb, lst)
    t1 = time.perf_counter()
    print("Dynamic done in " + str(t1-t0) + " seconds!")
    t0 = time.perf_counter()
    memoTime(wb, lst)
    t1 = time.perf_counter()
    print("Memo done in " + str(t1-t0) + " seconds!")
    t0 = time.perf_counter()
    recurTime(wb, lst)
    t1 = time.perf_counter()
    print("Recursion done in " + str(t1-t0) + " seconds!")

    wb.save('BinomialData.xls')

