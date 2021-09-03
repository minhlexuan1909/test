a, k, n = [int(num) for num in input().split()]

numList = []
upperLimit = int(n/k)
numList = [str(multiply*k-a) for multiply in range (1, upperLimit+1) if multiply*k > a]
print({True: ' '.join(numList), False: "-1"}[len(numList) > 0])