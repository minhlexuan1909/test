import collections

t = int(input())

for i in range(1,t+1):
    s1 = input()
    s2 = input()
    # __________Cach 1___________
    # freqs1 = [0]*124
    # freqs2 = [0]*124
    # for letter in s1:
    #     freqs1[ord(letter)]+=1
    # for letter in s2:
    #     freqs2[ord(letter)]+=1
    # print(f'Test {i}:',{True: 'YES', False: 'NO'}[freqs1 == freqs2])
    # __________Cach 2___________
    # s1 = collections.Counter(s1)
    # s2 = collections.Counter(s2)
    # print(f'Test {i}: ', {True: 'YES', False: 'NO'}[s1==s2])