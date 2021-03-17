# Election_Analysis 

## Project Overview 
Analyzing the election results of a recent local congressional election and performing an audit. This audit was to provide information on the following:

- the total number of votes cast 
- the complete list of candidates who received votes, how many votes each candidate received, and what percentage of the total vote each candidate received 
- the voter turnout for each county 
- the percentage of votes and total votes cast in each county 
- the county with the largest voter turnout 
- which candidate received the most votes and consequently, won the election

## Resources 
- Data Source: election_results.csv
- Software: Python, Visual Studio Code 

## Audit Results
Analysis of election shows that:
- There were 369,711 votes cast in the election 

*(analyzed using the following code in python):*

<img width="350" alt="1_totalvotes" src="https://user-images.githubusercontent.com/79600550/111091394-2c568680-8509-11eb-93ea-5e9d17eb1601.png">
<img width="466" alt="2_totalvotes" src="https://user-images.githubusercontent.com/79600550/111091396-2e204a00-8509-11eb-9eb2-8643ac28dcf1.png">
<img width="353" alt="3_totalvotes" src="https://user-images.githubusercontent.com/79600550/111091397-2fea0d80-8509-11eb-8460-6683793ac6c6.png">

- electoral candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane 
- candidate results revealed that:
  - Charles Casper Stockham received 85,213 votes or 23% of the total vote 
  - Diana DeGette received 272,892 votes or 73.8% of the total vote
  - Raymon Anthony Doane received 11,606 votes or 3.1% of the total vote

*(analyzed using the following code in python):*

<img width="538" alt="candidate_results" src="https://user-images.githubusercontent.com/79600550/111091510-86574c00-8509-11eb-8be9-5b8b5ac4dcc2.png">

- county-specific results revealed that:
  -  Jefferson county received a total of 38,855 votes or 10.5% of the total vote 
  - Denver county received a total of 306,055 votes or 82.8% of the total vote 
  - Arapahoe county recieved a total 24,801 votes or 6.8% of the total vote

*(analyzed using the following code in python):*

<img width="650" alt="county_results" src="https://user-images.githubusercontent.com/79600550/111091432-44c6a100-8509-11eb-9adb-bff7330e99e7.png">

- The county with the largest voter turnout was Denver.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 total votes

## Audit Summary
The current Python script written for the purpose of this election analysis (reference PyPoll_Challenge.py file) is quite versatile in nature and can be applied over again to get at the information of interest for any election. With election data that is clean and stored within a csv file, the code designed in this script will access the data file, declare a number of different variabes, lists and dictionaries to represent and store the information regarding the above categories of interest, and will loop through the data count and pull out such information - i.e the total number of votes casted; how many candidates there are and name them; how many votes each candidate received and what percentage of the total vote they received; what counties/districts were involved in the election, how many votes came from that area; what percentage of the total vote was casted in this area; etc. Furthermore, it will save and print this data in an organized manner in a seperate, easy-to-read txt file as done so in this analysis (reference the Analysis folder - election_analysis.txt and terminal_print). 

Of course, how the original data file is organized will determine what adjustments need to be made to the code in order to reference the correct physical location of the information. For example, if the candidates names data is stored in the first or second column rather than third (ie column 0 or column 1 instead of column 2 according to Python indexing), areas in the code can be altered to reference these specific areas in the for loop. These changes are quite minor and easy to perform. 
Another example in which the code can be altered to suit data for other elections would be to those that provide a more diverse dataset. If futher data were provided - for example, different voter demographic information - the same structure of code used in this analysis could be used to provide valuable insights on this information as well, presenting even more useful information when analyzing election results. This could simply be done with the use of lists or dictionaries to organize the data, and provide point of reference when looping through the dataset and performing calculations (if necessary). 
