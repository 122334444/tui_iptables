#!/bin/bash

date

echo
iptables -L PREROUTING --line-numbers -v -n -t nat
#iptables -t nat -L --line-numbers

#echo
#iptables --list --line-numbers