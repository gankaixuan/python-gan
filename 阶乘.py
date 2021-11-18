sum=0
for i in range(1,11):
    t=1
    for j in range(1,i+1):
        t*=j
    sum+=t
print(sum)