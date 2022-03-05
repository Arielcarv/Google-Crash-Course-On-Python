## Original
cat spyder.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

## Improved
cat spyder.txt | tr ' ' '\n' | tr '[:upper:]' '[:lower:]' | sed 's/,//g' | sort | uniq -c | sort -nr

