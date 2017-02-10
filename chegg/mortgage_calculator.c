/* 
Intro to c, mortgage calculator
Mortgage formula/annuity formula
Run the scenario for as many months as necessary. For example 2 year ,10 year depending on user inputs
User inputs principle in dollars and cents (total amount of the mortgage). For example $150000
User inputs percent of interest as integer. For example 6% (divide interest by 12 to find monthly interest rate)
User inputs term in years. For example 2, 10, 20, 30 years in integer (divide by 12 to find number of months)
Program uses formula to calculate monthly payment with C math to use exponents
Monthly payment (same every month). For example 6,648.10,  rounded to 2 decimal places, use this number to pay off to zero at the end, but must round up slightly to next higher penny
 
Subtract monthly interest payment from payment towards principle. Subtract payment towards principle from total principle. Interest and principle are then reducing each month.
 
Output the user inputs as results (interest, years, total principle) at top of results in table, first 3 months and last 3 months, last month shows the slight overpayment from rounding up in principle balance.
 
Attached output table shows example output in proper format.

-------------------------------------------------------------------------------------------------------------
-----------------------------------------------	 OUTPUT  ----------------------------------------------------
-------------------------------------------------------------------------------------------------------------

principle	=  150,000.00						rate  = 6% 						0.005
Pay/Mo. 	=  	 6,648.10						Years = 2						24

Month 			Principle			Interest 			$ to Prin 			Prin Balance
1			$150,000.00				$750.00				$5,898.10			$144,101.90
2			$144,101.90				$720.51				$5,927.59			$138,174.31
3			$138,174.31				$690.87				$5,957.23			$132,217.08
.			...						....				....				....
.			...						....				....				....

22			 $19,746.29				 $98.73				$6,549.37			 $13,196.93
23			 $13,196.93				 $65.98				$6,582.12			  $6,614.81
24			  $6,614.81				 $33.07				$6,615.03			      $0.22

------------------------------------------------------------------------------------------------------------
*/ 

#include <stdio.h>
#include <conio.h>
#include <math.h>

int main()
{
	/* code */







	return 0;
}