from re import sub
import subprocess

# SINTAX: 
# subprocess.get([<command to be executed>, <parameters of that command>])

subprocess.run(["date"])
# CompletedProcess(args=['date'], returncode=0)
subprocess.run(["sleep", "2"])
# CompletedProcess(args=['sleep', '2'], returncode=0)

result = subprocess.run(["ls", "this_file_doesnt_exist"])
print(f"RETURN CODE: {result.returncode}")

output_result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(f"RETURN CODE: {output_result.returncode}")
print(f"OUTPUT: {output_result.stdout}") # Return an array of bytes.
print(f"DECODED OUTPUT: {output_result.stdout.decode().split()}") 

rm_result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(f"RETURN CODE: {rm_result.returncode}")
print(f"OUTPUT: {rm_result.stdout}")
print(f"ERROR: {rm_result.stderr}")
