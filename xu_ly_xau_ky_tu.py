s1 = input().lower().split()
s2 = input().lower().split()


s = s1[::]
s.extend(s2)
setS = list(set(s))
setS.sort()
print(" ".join(setS))

# Cach 1:
# a = list(set(s1).intersection(s2))
# a.sort()
# print(" ".join(a))

a = [x for x in set(s1) if x in s2]
a.sort()
print(" ".join(a))
