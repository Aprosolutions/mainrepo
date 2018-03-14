#!/bin/bash
echo "enter a choice"
echo "1.sum of digits"
echo "2.palindrome "
echo "3.exit"
read c
switch (c)
case : 1
echo " sum of digits "
echo " echo enter 5 number "
for (i=0;i<5;i++)
read n
d=$((n%10))
s=$((s+n))
n=$((n/10))
done 
echo "sum of digits"
case : 2

