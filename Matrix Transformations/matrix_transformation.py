from turtle import *
import numpy as np
#Decide whether you want to stretch or rotate the plane
S=input("If you want to stretch the plane,type S and If you want to rotate the plain,type R:")
if S=="R":
    I=int(input("Enter angle in degrees"))
    transmatrix=[[np.cos(I*(np.pi/180)),np.sin(I*(np.pi/180))],[np.cos(I*(np.pi/180)+(np.pi/2)),np.sin(I*(np.pi/180)+(np.pi/2))]]
elif S=="S":
    a=int(input("Enter x coordinate of new location of i cap"))
    b=int(input("Enter y coordinate of new location of i cap"))
    c=int(input("Enter x coordinate of new location of j cap"))
    d=int(input("Enter y coordinate of new location of j cap"))
    transmatrix=[[a,b],[c,d]]
    
screensize(1000,1000)
#matrix multiplication operator
def matMult(a,b):
    screensize(1000,1000)
    n=[]
    for i_1 in range(len(a)):    
        n.append([])
        for j_1 in range(2):
            n[i_1].append((a[i_1][0]*b[0][j_1])+(a[i_1][1]*b[1][j_1]))
    return n
#find the determinant of a 2x2 matrix 
det=transmatrix[0][0]*transmatrix[1][1]-transmatrix[0][1]*transmatrix[1][0]
c=matMult([[1,0]],transmatrix)
k=matMult([[0,1]],transmatrix)
colormode(255)
#create gridlines of final space
def gridlines():
    screensize(1000,1000)
    hideturtle()
    #if determinant of matrix is not zero then transformation is valid
    #Space will not collapse into singularity
    if det!=0:
        speed(0)
        color(0,25,200)
        for i in range(40):
            pu()
            goto(g_1[0][0]-i*k[0][0],g_1[0][1]-i*k[0][1])
            pd()
            goto(g_2[0][0]-i*k[0][0],g_2[0][1]-i*k[0][1])
            pu()
        for i in range(40):
            pu()
            goto(g_1[0][0]+i*k[0][0],g_1[0][1]+i*k[0][1])
            pd()
            goto(g_2[0][0]+i*k[0][0],g_2[0][1]+i*k[0][1])
            pu()    
        for j in range(40):
            pu()
            goto(f_1[0][0]-j*c[0][0],f_1[0][1]-j*c[0][1])
            pd()
            goto(f_2[0][0]-j*c[0][0],f_2[0][1]-j*c[0][1])
            pu()
        for j in range(40):
            pu()
            goto(f_1[0][0]+j*c[0][0],f_1[0][1]+j*c[0][1])
            pd()
            goto(f_2[0][0]+j*c[0][0],f_2[0][1]+j*c[0][1])
            pu()
    #if determinant of matrix is zero then transformation is not valid
    #Space will collapse into singularity        
    else:
        color(0,200,200)
        for i in range(1):
            pu()
            goto(g_1[0][0],g_1[0][1])
            pd()
            goto(g_2[0][0],g_2[0][1])
            pu()
        for j in range(1):
            pu()
            goto(f_1[0][0],f_1[0][1])
            pd()
            goto(f_2[0][0],f_2[0][1])
            pu()
#create gridlines of initial space
def bluelines():
    screensize(1000,1000)
    hideturtle()
    speed(-1)
    color(0,255,255)
    for i in range(31):
        pu()
        goto(-15+i,-15)
        pd()
        goto(-15+i,15)
        pu()
    for j in range(31):
        pu()
        goto(-15,-15+j)
        pd()
        goto(15,-15+j)
        pu()
#create axes
def setup():
    screensize(1000,1000)
    p=1
    hideturtle()
    speed(-1)
    setworldcoordinates(-7,-7,7,7)
    setpos(0,0)
    clear()
    bluelines()
    setpos(0,0)
    setheading(0)
    pd()
    color('black')
    for i in range(15):
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        p=p+1
#coordinates of shape to be transformed        
fmatrix=[[0,0],[2,6],[4,6],[6,0],[5,0],[3,5],[1,0],[0,0]]
#initial shape drawing operator
def draw(matA):
    screensize(1000,1000)
    hideturtle()
    pu()
    speed(10)
    goto(0,0)
    pd()
    for point in matA:
        goto(point[0],point[1])
setup()
#matrices for defining size of space
g1=[[-155,0]]
g2=[[155,0]]
f1=[[0,-155]]
f2=[[0,155]]
#matrices for defining size of transformed space
g_1=matMult(g1,transmatrix)
g_2=matMult(g2,transmatrix)
f_1=matMult(f1,transmatrix)
f_2=matMult(f2,transmatrix)
#matrix defining transformed shape
newmat=matMult(fmatrix,transmatrix)
gridlines()
pensize(2)
color('black')
#drawing shape
draw(fmatrix)
pensize(2)
color('red')
#drawing transformed shape
draw(newmat)
done()

