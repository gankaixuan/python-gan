far=[]
h=100
for i in range(1,11):
    if i==1:
        far.append(h)
    else:
        far.append(h*2)
    h=h/2
print(f'经过的总距离：far={sum(far)}')
print(f'第十次反弹高度为：h={h}')
    