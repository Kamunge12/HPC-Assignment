#!/bin/bash
# calculate the sum of the first ten million intergers
sum=0
for ((i=1;i<=10000000;i++));do
sum=$((sum+i))
done
echo "sum of first ten million intergers:$sum"

chmod +x bash_script.sh

