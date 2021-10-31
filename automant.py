
#################   THIS CODE REMAINS UNTESTED ################

import os, sys, subprocess
import time
from threading import Timer
from subprocess import Popen

#process = subprocess.Popen("yes '$(seq 1 10)' | while read n; do  echo $n; sleep 2; done", stdin=subprocess.PIPE)
#process = subprocess.Popen('watch -n 2 ls -l', stdin=subprocess.PIPE, shell=True)
#cat automant.py | pv --quiet --line-mode --rate-limit 1
process = subprocess.Popen('cat file_random.txt | pv --quiet --line-mode --rate-limit 1', stdin=subprocess.PIPE, shell=True)
process.communicate()
if process.poll() is None:
    print("Still working")
else:
    print("Finished")
rc = process.poll()
print(rc)

#######
timeout = 3
with subprocess.Popen('cat automant.py | pv --quiet --line-mode --rate-limit 1', stdin=subprocess.PIPE, shell=True, stdout=subprocess.PIPE) as process:
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except TimeoutExpired:
        process.kill()
        print("renew?")
        stdout, stderr = process.communicate()
        raise TimeoutExpired(process.args, timeout, output=stdout, stderr=stderr)
