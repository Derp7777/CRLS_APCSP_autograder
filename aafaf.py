import os
import re
import subprocess
import delegator

filename = '/tmp/2018_luismartinez_1.04.py'
cmd = "grep 'input' " + filename + "| wc -l  "
print(cmd)
#cmd = "ls -al|wc -l"
c = delegator.run(cmd)
print(c.out)
print(c.err)