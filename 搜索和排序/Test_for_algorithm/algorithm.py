from profiler import Profiler
def selectSort(lst,Profiler):
    i = 0
    while i < len(lst)-1:
        minindex = i
        j=i+1
        while j<len(lst):
            Profiler.comparison()
            if lst[j] < lst[minindex]:
                minindex = j
            j = j+1

        if minindex != i:
            swap(lst, minindex, i, Profiler)

        i += 1


def swap(lst, i, j,Profiler):
    Profiler.exchange()
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

