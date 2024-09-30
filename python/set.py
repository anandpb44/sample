
# s.difference({6,7,8})
# s.add(10)
# s.update({5,6,7})
# s.pop()
# s.remove(9)
# s.discard(9)
# s.intersection({4,6,1})
# s.intersection_update({4,5,6})
# s.isdisjoint({1,2,3,4})
# s.issubset({1,3,4,5})
# s.issuperset({1,2,8})
# s={1,2,5,7,3,8}
#s.symmetric_difference({1,3,8})
#s.union({1,2,5,7,8,9})
# print(s)
# l=[1,2,3,5,1,2,3,55,45,45,55]
# s=set(l)
# l=list(s)
# print(l)
# l=[1,2,4,{10,11}]

# print(l[3])
# l[3].add(12)
# print(l)
l=[1,2,[10,{5,6}],4]
print(l[2])
l[2][1].add(7)
print(l)