import ipaddress
import os

def preferences(): #Sets user preferences
    batches = int(input("Number of Batches to create: "))
    if batches == 0:
        print("Hahaha. Very funny...")
        input()
        exit()
    for x in range(batches):
        os.system('cls' if os.name == 'nt' else 'clear')
        while 1:
            ip_start=[]
            print("Batch",x+1,"STARTING IP: \t", end="")
            ip_start.append(str(input()))
            if len(ip_start[x].split('.')) == 4:
                break
            else:
                print("Invalid format!\n")
                continue
                
        while 1:
            ip_end=[]
            print("Batch",x+1,"ENDING IP: \t", end="")
            ip_end.append(str(input()))
            if len(ip_end[x].split('.')) == 4:
                break
            else:    
                print("Invalid format!\n")
                continue
    return ip_start, ip_end

def listMaker(ip_start, ip_end):
    start = ipaddress.IPv4Address(ip_start)
    end = ipaddress.IPv4Address(ip_end)

    ip_startaddress_list = [start]
    temp = start

    while temp != end:
        temp += 1
        ip_startaddress_list.append(temp)

    return ip_startaddress_list

def main():
    print("IP Address Target File Creator\nVer: 0.1")
    
    ip_start, ip_end = preferences() #set starting and ending IP
    
    for y in range(len(ip_start)):
        ip_list=[]
        ip_list = listMaker(ip_start[y], ip_end[y])
        file_name = "batch_"+str(y)+".txt"
        f=open(file_name, 'w+')
        for g in ip_list:
            f.write(str(g)+"\n")
        f.close() 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Done. IP list(s) in script directory under name \"Batch_XX.txt\"")
    input()
main()
