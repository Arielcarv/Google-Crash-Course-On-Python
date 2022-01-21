import os 
import subprocess
import json

my_env = os.environ.copy()
formatted_my_env = json.dumps(my_env, indent=2)
print(f"ALL ENVIRONMENT VARIABLES: {formatted_my_env}")

my_env["PATH"] = os.pathsep.join(["opt/myapp/", my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env)
print (result)