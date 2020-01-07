#!/bin/bash

iptables -t nat -A PREROUTING -i $1 -p tcp --dport $2 -j DNAT --to $3:$4