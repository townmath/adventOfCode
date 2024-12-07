import math

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
        sums=[val[0]]*(3**len(val))
        for i,num in enumerate(val[1:]):
            plus=0
            for j in range(len(sums)):
                if plus==0:
                    sums[j]+=num
                elif plus==1:
                    sums[j]*=num
                else:#plus=2
                    #print(sums[j], num)
                    sums[j]=int(str(sums[j])+str(num))
                    #print(sums[j])
                if (j+1)%opsCnt==0:
                    plus+=1
                    plus%=3
            opsCnt*=3
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
                strSol=str(sol)
                strVal=str(vals[i])
                #print(strSol,strVal)
                if strSol.endswith(strVal):
                    #print("worked?", int(strSol[:len(strSol)-len(strVal)]))
                    if len(strSol[:len(strSol)-len(strVal)])>0:
                        newSolSet.append(int(strSol[:len(strSol)-len(strVal)]))
            solSet=newSolSet.copy()
        #print(vals[0],solSet)
        if len(solSet)>0 and vals[0] in solSet:
            total+=oldKey
    print(total)
            
#longWay(valsDict)
shortWay(valsDict)
            
#part a: 66343330034722
#part b: 637696070419031
#012012012012
#000111222000
#000000000111
