# Import 
import os
import subprocess


## Change directory
# Need to make flexible for other users
os.chdir("C:/Users/Hunt/Documents/GitHub/template_ha/")



## Run programs
# Stata analysis
subprocess.call("StataMP-64.exe","do","/Code/Analysis/MasterFile.do")


# Lyx to compile paper
subprocess.call("lyx.exe")
