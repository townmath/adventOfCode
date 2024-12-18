program=[2,4,1,7,7,5,1,7,4,6,0,3,5,5,3,0]

bestI=0
def do_one_simplified_similarity(A,program,debug=False):
    global bestI
    B=0
    C=0
    #newProgram=[]
    i=0
    oldA=A
    #if debug: print("A=",oct(A)[2:])
    while True:
        #2,4,
        B=A%8
        #if debug: print("B=",oct(B)[2:])
        #1,7,
        #B=B^7 #same as 7-B?
        #if debug: print("B=",oct(B)[2:])
        #7,5,
        C=A>>(B^7)
        #if debug: print("C=",oct(C)[2:])
        #1,7,
        #B=B^7
        #if debug: print("B=",oct(B)[2:])
        #4,6,
        B=B^C
        #if debug: print("B=",oct(B)[2:])
        #0,3,
        A=A>>3
        #if debug: print("A=",oct(A)[2:])
        #5,5,
        #print(B%8,end=",")
        if i>=len(program):
            return 0
        elif program[i]!=B%8:
            return i
        elif i>=bestI:
            bestI=i
            #print(i,oct(oldA)[2:])

        #if debug: print("B%8=",B%8)
        #3,0
        i+=1
        if A==0:
            return i

answerSet=set()
def buildUp4(octNums):
    global answerSet
    maxSim=0
    outSet=set()
    #print(len(program))
    for octNum in octNums:
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    for l in range(8):
                        topPart=str(i)+str(j)+str(k)+str(l)
                        A=int(topPart+octNum,8)
                        sim=do_one_simplified_similarity(A,program)
                        if sim==16:
                            #print(topPart+octNum)
                            #print("=========^")
                            #print("loook")
                            answerSet.add(int(topPart+octNum,8))
                        if sim>=len(octNum):
                            outSet.add(str(l)+octNum)
    return outSet
infLoopCnt=0
while infLoopCnt<20:
    octNums=[""]
    while infLoopCnt<20:
        octNums=buildUp4(octNums)
        infLoopCnt+=1
#print(answerSet)
print(sorted(list(answerSet)))
