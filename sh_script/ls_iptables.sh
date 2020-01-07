#!/bin/bash

date

echo
iptables -t nat -L --line-numbers

echo
iptables --list --line-numbers