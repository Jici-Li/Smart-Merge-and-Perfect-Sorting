
# File:    smartsort.py
# Author:  John Longley
# Date:    October 2025

# Template file for Inf2-IADS (2025-26) Coursework 1, Part A:
# Implementation of hybrid Merge Sort / Insert Sort,
# with optimization for already sorted segments.


import peekqueue
from peekqueue import PeekQueue

# Global variables

comp = lambda x,y: x<=y       # comparison function used for sorting

insertSortThreshold = 10

sortedRunThreshold = 10


# TODO: Task 1. Hybrid Merge/Insert Sort

# In-place Insert Sort on A[m],...,A[n-1]:

def insertSort(A,m,n):
    """In-place Insert Sort on A[m],..,A[n-1]"""
    if n<=m:
        return
    for i in range(m+1,n):
        key=A[i]
        j=i-1
        while j>=m and not comp(A[j],key):
            A[j+1]=A[j]
            j-=1
        A[j+1]=key


def merge(C,D,m,p,n):
    """Merge C[m],...,C[p-1] and C[p],...,C[n-1] into D[m],...,D[n-1]"""
    i,j,k=m,p,m
    while i<p and j<n:
        if comp(C[i],C[j]):
            D[k]=C[i]
            i+=1
        else:
            D[k]=C[j]
            j+=1
        k+=1
    while i<p:
        D[k]=C[i];i+=1;k+=1
    while j<n:
        D[k]=C[j];j+=1;k+=1

def greenMergeSort(A,B,m,n):
    """Merge Sort A[m],...,A[n-1] using just B[m],...,B[n-1] as workspace.
    Deferr to Insert Sort if length <= insertSortThreshold"""
    if n - m <= insertSortThreshold:
        insertSort(A,m,n)
    else:
        q1=m+(n-m)//4
        q2=m+(n-m)//2
        q3=m+3*(n-m)//4

        greenMergeSort(A,B,m,q1)
        greenMergeSort(A,B,q1,q2)
        greenMergeSort(A,B,q2,q3)
        greenMergeSort(A,B,q3,n)

        merge(A,B,m,q1,q2)
        merge(A,B,q2,q3,n)
        merge(B,A,m,q2,n)

# Provided code:

def greenMergeSortAll(A):
    B = [None]*len(A)
    greenMergeSort(A,B,0,len(A))
    return A


# TODO: Task 2. Detecting already sorted runs.

def allSortedRuns(A):
    """Build and return queue of sorted runs of length >= sortedRunThreshold.
    Queue items should be pairs (i,j) such that A[i],...,A[j-1] is sorted."""
    Q=PeekQueue()
    n=len(A)
    i=0
    while i<n:
        j=i+1
        while j<n and comp(A[j-1],A[j]):
            j+=1
        if j-i>=sortedRunThreshold:
            Q.push((i,j))
        i=j
    return Q

def isWithinRun(Q,i,j):
    """Test whether A[i],...,A[j-1] is sorted according to info in Q."""
    current=Q.head
    while current and current.value is not None:
        a, b=current.value
        if i<a:
            return False
        elif a<=i and j<=b:
            return True
        current=current.next
    return False


def smartMergeSort(A,B,Q,m,n):
    """Improvement on greenMergeSort taking advantage of sorted runs."""
    if isWithinRun(Q,m,n):
        return
 
    if n-m<=insertSortThreshold:
        insertSort(A,m,n)
        return

    q1=m+(n-m)//4
    q2=m+(n-m)//2
    q3=m+3*(n-m)//4

    if not isWithinRun(Q,m,q1):
        smartMergeSort(A,B,Q,m,q1)
    if not isWithinRun(Q,q1,q2):
        smartMergeSort(A,B,Q,q1,q2)
    if not isWithinRun(Q,q2,q3):
        smartMergeSort(A,B,Q,q2,q3)
    if not isWithinRun(Q,q3,n):
        smartMergeSort(A,B,Q,q3,n)
    
    merge(A,B,m,q1,q2)
    merge(A,B,q2,q3,n)
    merge(B,A,m,q2,n)

# Provided code:

def smartMergeSortAll(A):
    B = [None]*len(A)
    Q = allSortedRuns(A)
    smartMergeSort(A,B,Q,0,len(A))
    return A


# TODO: Task 3. Asymptotic analysis of smartMergeSortAll

# 1. Justification of O(n lg n) bound.
#
#
#
#
# (continue as necessary)

# 2. Runtime analysis for nearly-sorted inputs.
#
#
#
#
# (continue as necessary)


# Functions added for automarking purposes - please don't touch these!

def set_comp(f):
    global comp
    comp = f

def set_insertSortThreshold(n):
    global insertSortThreshold
    insertSortThreshold = n

def set_sortedRunThreshold(n):
    global sortedRunThreshold
    sortedRunThreshold = n

def set_insertSort(f):
    global insertSort
    insertSort = f

# End of file
