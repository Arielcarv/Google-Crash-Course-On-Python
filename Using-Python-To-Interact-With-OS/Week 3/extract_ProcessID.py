import re 

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
pattern = r"\[(\d+)\]"
result = re.search(pattern, log)
print(result[1])

result2 = re.search(pattern, "A completely different string that also has numbers [67890]")
print(result2[1])

# result3 = re.search(pattern, "99 elephants in a [cage]")
# print(result3[1])

def extract_PID(line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, line)
    if result is None:
        return ""
    return result[1]

print(extract_PID(log))
print(extract_PID("99 elephants in a [cage]"))


def extract_pid(log_line):
    regex = r"\[(\d+)\].*\s([A-Z]+)\s"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
