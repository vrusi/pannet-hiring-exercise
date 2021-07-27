# Usage

To run the script:

```
python scanner.py [HOST_IP_RANGE_START] [HOST_IP_RANGE_END] [SCAN_UDP]
```
where:
* HOST_IP_RANGE_START is required. If it is the only provided argument then it is the only IP that will be scanned.
* HOST_IP_RANGE_END is optional. If it is provided, the given range of IP addresses will be scanned.
* SCAN_UDP is optional, expects 1 or 0. If 1 is provided, the scanner will scan for open UDP ports (as opposed to only scanning for open TCP ports).

To run with docker: 
```
docker run --rm vrusi/pannet-hiring-exercise [HOST_IP_RANGE_START] [HOST_IP_RANGE_END] [SCAN_UDP]
```