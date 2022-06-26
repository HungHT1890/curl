from re import sub
import re
import subprocess
while True:
    command = 'curl https://combolist.org/generate'
    result = subprocess.check_output(command)
    print(result)
    with open('what_is_this.txt','a',encoding='utf-8') as saveresults:
        saveresults.write(str(result))