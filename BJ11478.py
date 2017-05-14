s=set([]);i=input();l=len(i)
for j in range(l):[s.add(i[j:k]) for k in range(j+1,l+1)]
print(len(s))