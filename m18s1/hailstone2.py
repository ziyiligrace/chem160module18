import sys
if not 'N' in locals():
	print("Variable N not defined")
	sys.exit()
while N!=1:
     print(N)
     steps+=1
     if N%2==0:
        	N=N//2
     else: 
	        N=3*N+1
print("steps=", steps)
