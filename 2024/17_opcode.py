inFile=open("17_test.txt",'r')

for line in inFile:
    line=line.strip()
    
#If register C contains 9, the program 2,6 would set register B to 1.
A,B,C=0,0,9
program=[2,6]
#If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
A,B,C=10,0,0
program=[5,0,5,1,5,4]
#If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
A,B,C=2024,0,0
program=[0,1,5,4,3,0]
#If register B contains 29, the program 1,7 would set register B to 26.
#If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354

A=729
B=0
C=0
program=[ 0,1,5,4,3,0]

A=66245665
B=0
C=0

program=[2,4,1,7,7,5,1,7,4,6,0,3,5,5,3,0]
def doOpcode(opcode,combo,A,B,C,i):
    jump=i+2
    if 0<=combo<=3:
        combo=combo
    elif combo==4:
        combo=A
    elif combo==5:
        combo=B
    elif combo==6:
        combo=C
    #else:
    #    print("error 7!")
    if opcode==0:#div
        A=A//(2**combo)
    elif opcode==1:#xor
        B=B^combo
    elif opcode==2:#mod 8
        B=combo%8
    elif opcode==3:#jnz
        if A!=0:
            jump=combo
    elif opcode==4:#xor
        B=B^C
    elif opcode==5:#out
        print(combo%8,end=',')
    elif opcode==6:#bdiv
        B=A//(2**combo)
    elif opcode==7:
        C=A//(2**combo)
    return jump,A,B,C

i=0
while i<len(program)-1:
    opcode=program[i]
    combo=program[i+1]
    jump,A,B,C=doOpcode(opcode,combo,A,B,C,i)
    i=jump
#print(A,B,C)
        
        
    
