inFile=open("7.txt",'r')

valsDict=dict()
for line in inFile:
    line=line.strip()
    pieces=line.split()
    target=int(pieces[0][:-1])
    numArr=[int(x) for x in pieces[1:]]
    valsDict[target]=numArr

def longWay(valsDict):
    total=0
    for key,val in valsDict.items():
        opsCnt=1
        sums=[val[0]]*(2**len(val))
        for i,num in enumerate(val[1:]):
            plus=True
            for j in range(len(sums)):
                if plus:
                    sums[j]+=num
                else:
                    sums[j]*=num
                if (j+1)%opsCnt==0:
                    plus=not plus
            opsCnt*=2
        if key in sums:
            total+=key
    print(total)

def shortWay(valsDict):
    total=0
    for key,vals in valsDict.items():
        oldKey=key
        notGood=False
        solSet=[key]
        for i in range(len(vals)-1,0,-1):
            newSolSet=[]
            for sol in solSet:
                if (sol//vals[i])*vals[i]==sol:
                    newSolSet.append(sol//vals[i])
                if sol-vals[i]>=0:
                    newSolSet.append(sol-vals[i])
            solSet=newSolSet.copy()
            if len(solSet)==0:
                break
        #print(vals[0],solSet)
        if len(solSet)>0 and vals[0] in solSet:
            total+=oldKey
    print(total)
longWay(valsDict)
shortWay(valsDict)
            
        
    
