name=input('What is your goodname Sir \n')
l=list(name)
name=name.lower()
print(*name, sep='\t')
for i in range(len(name)):
    print(name[i])
matrix = [['a','s','s','f','a','c','e'],['b','e','h','e','n','c','h','o','d'],['c','h','u','t','i','y','a'],['d','o','n','k','e','y'],['e','t','a','t','t','i'],['f','a','r','t','f','a','c','e'],['g','A','a','n','D','u'],['h','a','r','a','m','i'],['i','m','l','i','l','u','n','d'],['j','h','a','a','t','u'],['k','u','t','t','e'],['l','u','n','d','f','a','k','i','r'],['m','a','d','a','r','c','h','o','d'],['n','a','h','i','d','e','g','i'],['o','_','c','h','u','t','i','y','e'],['p','o','t','t','y','f','a','c','e',':','P'],['q','h','a','i','t','u','z','i','n','d','a'],['r','a','n','d','i'],['s','a','a','l','a'],['t','e','n','c','h','o','d'],['u','c','h','u','t','i','y','a'],['v','i','r','g','i','n','s','a','a','l','a'],['w','h','o','r','e'],['x','h','u','t','i','y','a'],['y','U','a','l','i','v','e'],['z','a','d','a','r','c','h','o','d']]
for r in matrix:
    for c in r:
        print(c, end = "")
    print()
for i in range(len(name)):  
    for r in matrix:
        c = r[0]
        if name[i]==c:
            print(name[i])
            for c in r:
                print(c,end="")
            print('\n')
            break
