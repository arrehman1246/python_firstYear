"""Problem Statement: Consider a permutation of numbers from 1 to N written on a paper. Let’s denote the product of its
 element as ‘prod’ and the sum of its elements as ‘sum’. Given a positive integer N, your task is to determine whether
‘prod’ is divisible by ‘sum’ or not."""

"""Input Format: First input will be an integer T.  It depicts a number of test cases. Followed by value for each 
test case. Each test case will contain an integer N (1<= N <=10^9). It is nothing but the length of the permutation."""

"""Output Format: For each test case, print “YEAH” if ‘prod’ is divisible by ‘sum’, otherwise print “NAH”."""

testSize = int(input("Enter test size: "))
nArr=[]
for i in range(testSize):
    nArr.append(int(input("Enter integer: ")))

for n in nArr:
    if 1 <= n <= (10 ** 9):
        prod = 1
        sums = 0
        for i in range(1, n+1):
            prod = prod * i
            sums += i
        if prod % sums == 0:
            print("YEAH")
        else:
            print("NAH")