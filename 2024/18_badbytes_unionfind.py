
inFile=open("18_union.txt",'r')
maxDim=6#70#
maxBytes=12#1024#

badBytes=[]

for line in inFile:
    line=line.strip()
    x,y=line.split(',')
    x,y=int(x),int(y)
    badBytes.append((y,x))

#adapted from https://algs4.cs.princeton.edu/15uf/
class UF():
    def __init__(self,n):
        if (n < 0):
            print("n must be >=0")
        self.count = n;
        self.parent = n*[None]
        self.rank = n*[None]
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self,p):
        self.validate(p);
        while (p != self.parent[p]):
            self.parent[p] = self.parent[self.parent[p]]    # path compression by halving
            p = self.parent[p]
        return p
    

    def connected(self,p,q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if (rootP == rootQ): return

        # make root of smaller rank point to root of larger rank
        if  (self.rank[rootP] < self.rank[rootQ]):
            self.parent[rootP] = rootQ
        elif (self.rank[rootP] > self.rank[rootQ]):
            self.parent[rootQ] = rootP
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP]+=1
        self.count-=1


    # validate that p is a valid index
    def validate(self, p):
        n = len(self.parent)
        if (p < 0 or p >= n):
            print("index " + p + " is not between 0 and " + (n-1))

    def __str__(self):
        outStr=""
        for i in range(maxDim+1):
            for j in range(maxDim+1):
                outStr+=str(uf.parent[100*i+j])+','
            outStr+="\n"
        return outStr

def convertPoint(pt):
    i,j=pt
    return (i*100+j)

uf = UF(10000)
dirs=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

#like maxFlow we need dummy nodes
topRight=(maxDim+2,maxDim+2)#something off the grid
ufTopRight=convertPoint(topRight)
bottomLeft=(maxDim+3,maxDim+3)#something else off the grid
ufBottomLeft=convertPoint(bottomLeft)
visited=set()
#print(uf.count)
for byte in badBytes:
    #print(byte)
    visited.add(byte)
    ufByte=convertPoint(byte)
    i,j=byte
    for d in dirs:
        di,dj=d
        if i+di<0 or j+dj>maxDim:      #top right edges go to 
            uf.union(ufByte,ufTopRight)#top right dummy node
        elif i+di>maxDim or j+dj<0:      #bottom left edges go to
            uf.union(ufByte,ufBottomLeft)#bottom left dummy node
        elif (i+di,j+dj) in visited: #else connect neighbors together
            uf.union(convertPoint((i+di,j+dj)),ufByte)
    #print(uf)
    if uf.connected(ufTopRight,ufBottomLeft):#when the connected neighbors
        print("connected by",byte)# connect to both dummy nodes, the path is
        break                     # blocked
