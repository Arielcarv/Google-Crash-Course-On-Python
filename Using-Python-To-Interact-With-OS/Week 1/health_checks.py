#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    '''Returns True if the disk usage is less than 80%'''
    disk_usage = shutil.disk_usage(disk)
    free_space = (disk_usage.free / disk_usage.total) * 100
    print(f"Disk Usage: {disk_usage}.")
    return free_space > 20

def check_cpu_usage():
    '''Returns True if CPU usage is less than 75%'''
    cpu_usage = psutil.cpu_percent(1)
    print(f"CPU Usage: {cpu_usage}")
    return cpu_usage < 75 

if check_disk_usage("/") or check_cpu_usage():
    print("Everything is OK!") 
else:
    print("ERROR")
    