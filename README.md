# Python IPv4 list generator

This script takes three arguments: starting and ending IPs, and number of batches.
It generates files with one IP per line where the starting and ending IPs are the ones given.

## Usage:

#### Batches: 

Number of files that this script should generate. Each batch has the normal IP range (0.0.0.0 - 255.255.255.255)
and will require the input of starting and ending IPs.

#### Starting IP and mask:
Starting IP and what the network mask should be (NOT the host mask). 
Format is 'xxx.xxx.xxx.xxx/xx'

#### Include unuseable hosts
Includes or excludes default gateway and broadcasts addressses. (EG: 192.168.0.0 and 192.168.0.255)
	
	
## Example:

	IP Address Target File Creator
	Ver: 0.2
	Number of Batches to create:

1

	Batch 1
	Starting IP and mask (xxx.xxx.xxx.xxx/xx): 

127.0.0.0/25

	Include unuseable hosts? (Y/N):

Y

	Done. IP list(s) in script directory under name "Batch_XX.txt"
