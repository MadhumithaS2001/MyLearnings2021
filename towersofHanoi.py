def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("move disk 1 from rod",source,"to rod",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("move disk",n,"from rod",source,"to rod",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
n = int(input())
TowerOfHanoi(n,'1','3','2')
print("No.of steps: ".format((2**n)-1))
