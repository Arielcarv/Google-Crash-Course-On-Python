#!/bin/bash

line="-------------------------"

echo "Starting at: $(date)"; echo $line

echo -e "\nUPTIME"; uptime; echo $line

echo -e "\nFREE"; free; echo $line

echo -e "\nWHO"; who; echo $line

echo -e "\nFinishing at: $(date)";
