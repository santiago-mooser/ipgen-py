# IP list generator

This script takes IP ranges and an "unusable hosts" flag as arguments and generates lists of IPs for each given range.

## Usage:

```
ip_gen.py -r [ip range] <[...]> <-u>
```

## Example:
```
ip_gen.py -r 192.168.1.0/30 2620:0:2d0:200::7/124 -u
```

The previous commandline arguments will restult in two lists (batch_0.txt and batch_1.txt):

batch_0.txt:
```
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
```
batch_1.txt:
```
2620:0:2d0:200::
2620:0:2d0:200::1
2620:0:2d0:200::2
2620:0:2d0:200::3
2620:0:2d0:200::4
2620:0:2d0:200::5
2620:0:2d0:200::6
2620:0:2d0:200::7
2620:0:2d0:200::8
2620:0:2d0:200::9
2620:0:2d0:200::a
2620:0:2d0:200::b
2620:0:2d0:200::c
2620:0:2d0:200::d
2620:0:2d0:200::e
2620:0:2d0:200::f	
```


#### Starting IP and mask:
Starting IP and what the network mask should be (NOT the host mask). 
Format is 'xxx.xxx.xxx.xxx/xx'

#### Include unuseable hosts
Includes or excludes default gateway and broadcasts addressses. (Eg: 192.168.0.0 and 192.168.0.255)
