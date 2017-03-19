************************************
/* Example_CreateFigure.do

Description: This creates an example figure.
*/
************************************


use $dropbox/Intermediate/DatabyID.dta, replace
gen N=1

graph bar (percent) N,  over(LikeWithoutNorms) ///
	graphregion(color(white)) ytitle("Percent of respondents") ///
	title("How would you like Reports without neighbor comparisons?")

graph export Output/Analysis/LikeWithoutNorms.pdf, as(pdf) replace
