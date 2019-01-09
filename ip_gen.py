import ipaddress
import os
import getopt
import sys

def ipLister(t):
    os.system('cls' if os.name == 'nt' else 'clear')

    while 1:
        try:
            print("Batch", t+1)
            start_ip=ipaddress.ip_network(input("Starting IP and mask (xxx.xxx.xxx.xxx/xx): "))
            break
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid format or network", "red")
            continue

    while 1:
        ip_list=[]
        choice=str(input("Include unuseable hosts? (Y/N): "))
        
        if choice.lower() == "y":
            for addr in ipaddress.IPv4Network(start_ip):
                ip_list.append(addr)
            break
        elif choice.lower() =="n":
            ip_list=list(ipaddress.ip_network(start_ip).hosts())
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input")
            continue

    return ip_list

def main():
    
    print("IPv4 Address Target-File Creator\nVer: 0.2\n")
    print("***WARNING: IS SLOW WITH LARGE (500+) LISTS***\n")
    
    while 1:
        try:
            batches=int(input("Number of batches to create: "))
            break
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input")
            continue
            
    for t in range(batches):
    
        ip_list=ipLister(t)
        
        for y in range(len(ip_list)):        #print to file
            file_name = "batch_"+str(t)+".txt"
            f=open(file_name, 'w+')
            for g in ip_list:
                f.write(str(g)+"\n")
            f.close()
            
        os.system('cls' if os.name == 'nt' else 'clear')
        
    print("Done. IP list(s) in script directory under name \"Batch_XX.txt\"")
    input()

main()