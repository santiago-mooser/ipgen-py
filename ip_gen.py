import ipaddress
import argparse

def ipLister(range, unusuable_hosts):
    ip_range=ipaddress.ip_network(range, strict=False)
    ip_list =""

    if unusuable_hosts == True:
        if ip_range.version == 4:
            ip_list = ipaddress.IPv4Network(ip_range)
        else:
            ip_list = ipaddress.IPv6Network(ip_range)
    else:
        ip_list=list(ipaddress.ip_network(ip_range).hosts())

    return ip_list

def generateList(ranges, unusable_hosts, noOutput):
    print("-----\nIPv4 Address Target-File Creator\nVer: 0.3\n-----\n")
    ipListArray = {}
    failed_ranges = {}
    successful_ranges= {}
    

    for ip_range in ranges:
        try:
            ip_list = ipLister(ip_range, unusable_hosts)
            try:
                temp = []
                filename = "batch_"+str(ranges.index(ip_range))+".txt"
                f = open(filename, "w+")
                for line in ip_list:
                    if noOutput == False:
                        f.write(str(line)+"\n")
                    temp.append(line)
                f.close()
                ipListArray.update( { ipaddress.ip_network(ip_range, strict=False): temp })
                print("Wrote "+str(ip_range)+" in "+str(filename))
                successful_ranges.update( {"Ip range":ip_range})
            except:
                print(str(ip_range)+"\tUnable to open file for writing. Continuing to next iteration")
                failed_ranges.update( {"range":{"range":ip_range, "error":"Failed to write file"} })
                continue
        except:
            print(str(ip_range)+"\tIncorrect syntax. Continuing to next argument")
            failed_ranges.update({"range":{"range:":ip_range,"error":"incorrect syntax"} } )
            continue
            
    if __name__ == "__main__":
        exit(0)
    else:
        return ipListArray, failed_ranges

def argument_parser():
    description = "ip_gen.py generates lists of IP addresses to use with nmap. It supports IPv4 and IPv6 addresses"
    usage= "\t\tip_gen.py -r [ip range] <[...]> <-u>\nexample:\tip_gen.py -r 192.168.1.0/30 2620:0:2d0:200::7/124 -u"
    parser = argparse.ArgumentParser(description=description, usage=usage)

    parser.add_argument('-no', help='Prevent script from printing results to file. Useful if used as a module.', action='store_true', default=False)
    parser.add_argument('-r', nargs="+",help='IP ranges to generate', default="", required=True)
    parser.add_argument('-u', help='Include unusable hosts (Gateway and broadcast addresses)', action='store_true', default=False)
    args = parser.parse_args()
    print(args.r)
    if __name__ == "__main__" and args.no:
        print("No output is only supported if script is run as a module")
        exit(1)

    return args.r, args.u, args.no

if __name__ == "__main__":
    ranges, unusable_hosts, noOutput = argument_parser()
    generateList(ranges, unusable_hosts, noOutput)
