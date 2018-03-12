path="../../logs/0.05/"

results = {}

for r in range(256):
    f = open(path+str(r)+".out","r")
    for line in f:
        if line[0] != 'a':
            data = line.split(" ")
            r1 = int(data[1].replace(',', ''))
            r2 = int(data[2].replace(',', ''))
            sr = float(data[7].replace(',', ''))
            try:
                results[(r1,r2)].append(sr)
            except:
                results[(r1,r2)] = [sr]

            try:
                results[(r2,r1)].append(sr)
            except:
                results[(r2,r1)] = [sr]
    

for r in range(256):
    for r2 in range(256):
        try:
            print(r,r2,sum(results[(r,r2)])/8.0)
        except:
            print(r,r2,1.0)
    print("")
