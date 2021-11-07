# An Analysis of Election Data using Python

## Overview of Election Audit
A database containing information on a U.S. congressional election was analyzed. The main purpose of the analysis was to conduct an election audit. To achieve this purpose, a python script was written to:

-  Calculate the total number of votes cast;
-  Get a complete list of candidades who received votes;
-  Get a complete list of counties included in the election;
-  Calculate the total number of votes each candidate received;
-  Calculate the total number of votes each county collected;
-  Calculate the percentage of votes each candidate won;
-  Calculate the percentage of votes each county collected;
-  Identify the county which largest turnout;
-  Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.62.0

## Results
The analysis of the election showed that:
- There were 369,711 votes cast in the election;
- The candidates were:
	- Diana DeGette, who received 73.8% of the votes and 272,892 number of votes;
	- Charles Casper Stockham, who received 23.0% of the votes and 85,213 number of votes;
	- Raymon Anthony Doane, who received 3.1% of the votes and 11,606 number of votes.
- The counties included in the election were:
	- Denver, where 82.8% of the votes and 306,055 number of votes were collected;
	- Jefferson, where 10.5% of the votes and 38,855 number of votes were collected;
	- Arapahoe, where 6.7% of the votes and 24,801 number of votes were collected;
- Therefore:
	- The county with largest turnout was Denver;
	- The winner of the election based on popular vote was Diana DeGette. 

## Summary
Besides serving for the analysis of the present data, the python script created here can be easily adapted for future analysis of election data. The main reason why the script is versatile is because it was developed through the creation of general variables, lists and dictionaries. See for example the beginning of the code, where the path to load and save file (lines 9 and 11, respectively) will need to be adapted in a future analysis but variables, lists and dictionaries in lines 14 to 31 are general and can be used to calculate candidate and county votes in other datasets.


![Screen Shot 2021-11-06 at 8 44 00 PM](https://user-images.githubusercontent.com/89421440/140631995-2661d1d4-cd18-4ace-bd29-b992ce9e6cae.png)


To use the script in any election, the main modification analysts will have to make is to substitute the list indexes to find the candidate names and the county names in the database. In the present database, candidates names and county names can be found in list indexes 2 and 1, respectively (See lines 47 and 50 below). This information will have to be updated for this code to work in other elections.


![Screen Shot 2021-11-06 at 8 56 09 PM](https://user-images.githubusercontent.com/89421440/140631999-641c10f1-9099-49a9-828d-82fc8c1e6d80.png)

