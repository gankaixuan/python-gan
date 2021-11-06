for i in range(101,201):
    gan=0
    for j in range(2,i-1):
        if i%j==0:
            gan=1
            break
    if gan==0:
        print(i)