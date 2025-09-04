def frogg(gusto):
    gusto*=3
    gusto-=12
    return (gusto and 1)

for i in range(1,20):
    print(frogg(i))