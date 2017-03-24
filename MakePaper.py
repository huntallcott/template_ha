'''
#-------------------------------------------

PURPOSE

This script produces the entire project, from 
initial data to compiling the paper pdf

#------------------------------------------

REQUIREMENTS

Python 2.7.x
Python Library: Pip
Stata
LyX 2.2
R 3.x

#----------------------------------------

IMPORTANT

1) The main package that runs all of the files is gslab_scons. To download
this package, you must have installed pip. 

In the event that you pip is installed and the installation still doesn't work
you must download gslab_scons manually. This can be done by going to:
https://github.com/gslab-econ/gslab_python

2) To run this script, you must ensure that all of the required programs
are installed and in your PATH Environment. 
How to add programs depends on your operating system. 

For UNIX-based system:
open either ~/.bash_profile or ~/.bash_rc using a text editor
(Look up to see which one you should use on your computer)

and add the following command:
export PATH=$PATH:(Location of Your Stata Directory)
e.g. export PATH=$PATH:/usr/local/stata14

For Windows-based system:
Go to the System Control Panel applet, select the advanced tab, 
click the Environment Variables Button, select PATH and then click edit.
Then add the following directories to the PATH:

C:\Program Files\R\R-3.3.2\bin\x64
C:\Program Files (x86)\LyX 2.2\bin
C:\Program Files (x86)\Stata14

#--------------------------------------------

USEFUL COMMENTS 

1) To run a program in this script, we use the build_program() function 
in gslab_scons, where program is a specific program you wish to run, i.e. 
R, stata, lyx, etc. To see the full list of programs available, see:
https://github.com/gslab-econ/gslab_python/tree/master/gslab_scons/builders

2) The basic structure of gs.build_program(source, target, env) is:
source = "Location of file you want program to run relative to location of this file"
target = "Location and name of file you want program to send output to"
env = Dictionary of any command-line arguments you want to pass to function 

3) gs.build_r(): The code in gs.build_r() doesn't use the "target" 
argument to move the outputs of gs.build_r() to the 
target directory. Instead, the 'target' is where the sconscript.log file 
gets sent. If you want the outputs of the code to also go to the target
directory, you must do one of two things:

	i) In the R script, save whatever outputs you want to the output directory 
		relative to where THIS FILE (MakePaper.py) is saved. 
	ii) Pass the target directory as a command line argument that the R script
		reads. See /Code/Analysis/script.R for an example of method ii)

4) gs.build_stata(): The env{} argument must be nonempty and specify the 
type of stata used, i.e. stata, stata-mp, or stata-se. 
Passing None will have gs.build_stata() look for stata on your computer
but if you want, you can specify your flavor instead.

'''
#---------------------------------------

#Import packages 

import os
import shutil

try:
	import gslab_scons as gs #Note: This is an uncommon library.
except ImportError: 
	try: 
		import pip
	except ImportError:
		print("Error: You must download the Python library 'pip'")
		print("Exiting...")
		exit()
	
	pip.main(['install', 'git+https://git@github.com/gslab-econ/gslab_python.git'])
	try: 
		import gslab_scons as gs
	except ImportError:
		print('Error: Unable to install the required library gslab_scons')
		print('Download the required library: https://github.com/gslab-econ/gslab_python')
		print('Exiting...')
		exit()

#-------------------------------------------------

#Create the output directory. Delete it if it already exists
OutDir = 'Output/'

if os.path.isdir(OutDir):
	shutil.rmtree(OutDir)
os.mkdir(OutDir)

#Create output subdirectories
os.mkdir(OutDir + 'Analysis/') 
os.mkdir(OutDir + 'Lyx/')

#-------------------------------------------

# Build the Paper

# Run Stata Code
try:
	gs.build_stata(source = 'Code/Analysis/MasterFile.do', 
		target = OutDir + 'Analysis/', 
		env = {'user_flavor': None} 
		)
except UnboundLocalError:
	print('Error: You must include Stata in your PATH Environment')
	print('See "IMPORTANT NOTE #2" in this script for details')
	print('Exiting...')
	exit()

# Run R Code
# See Comment 3 for exhaustive discussion of this function
gs.build_r(source = 'Code/Analysis/script.R',
    target = OutDir + 'Analysis/',
    env = {'CL_ARG': OutDir + 'Analysis/table.txt'}
    )

#Compile the Paper
gs.build_lyx(source = 'Code/Lyx/Template.lyx', 
	target = OutDir + 'Lyx/Template.pdf', 
	env = {}
	)

#Compile the Slides
gs.build_lyx(source = 'Code/Lyx/Template_Slides.lyx', 
	target = OutDir + 'Lyx/Template_Slides.pdf', 
	env = {}
	)

