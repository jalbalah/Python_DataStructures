def quicksort(A):
    r_quicksort(A, 0, len(A)-1)
def r_quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        r_quicksort(A, lo, p - 1)
        r_quicksort(A, p + 1, hi)
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            swap(A, i, j)
            i += 1
    swap(A, i, hi)
    print(str(A)[1:-1].replace(",",""))
    return i
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
#input()
#l = [int(x) for x in input().split(" ")]
l=[1, 3, 9, 8, 2, 7, 5]
print("Sort:",str(l)[1:-1].replace(",",""))
quicksort(l)
