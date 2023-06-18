def toh(n,source,destination,axulliary):
    if n==1:
        print("move ", source ,"to", destination)
        return

    toh(n-1,source,axulliary,destination)
    print("move ", source, "to", destination)
    toh(n-1,axulliary,destination,source)

#no of disks
n_disks = 4
toh(n_disks,'a','b','c')