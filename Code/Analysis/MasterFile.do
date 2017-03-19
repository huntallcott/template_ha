************************************
/* MasterFile.do

Description: This is the Stata master file for the analysis. 
It sets directories and calls other programs that prepare and analyze data.
*/
************************************



************************************
* Setup
************************************
clear all
set more off

** Set directories
* Here set the location of each user's Dropbox/Externals folder.
if "`c(username)'"=="Hunt" {
	global dropbox = "C:/Users/Hunt/Dropbox/template_ha/Externals" 
}

** Set any other locals and globals 




************************************
* Call data prep and analysis files
************************************
include Code/Analysis/Example_CreateFigure.do
