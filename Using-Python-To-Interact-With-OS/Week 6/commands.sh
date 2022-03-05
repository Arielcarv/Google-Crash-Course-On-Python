## Original
cat spyder.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

## Improved
cat spyder.txt | tr ' ' '\n' | tr '[:upper:]' '[:lower:]' | sed 's/,//g' | sort | uniq -c | sort -nr

## From the last 20 lines, cut from the 5th space till the end  
tail /var/log/syslog | cut -d' ' -f5- 

## From the whole file cut from the 5th space till the end, and measure which one is the most repeated.
cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head 
