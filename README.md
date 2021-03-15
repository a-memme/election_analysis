# Election_Analysis 

## Project Overview 
Colorado Board of Elections employee giving the following tasks to analyze the election results of a recent local congressional election and perform an audit. This audit was to provide information on

- the total number of votes cast 
- the complete list of candidates who received votes, how many votes each candidate received, and what percentage of the total vote each candidate received 
- the voter turnout for each county 
- the percentage of votes and total votes cast in each county 
- the county with the largest voter turnout 
- which candidate received the most votes and consequently, won the election

## Resources 
- Data Source: election_results.csv
- Software: Python, Visual Studio Code 

## Summary 
Analysis of election shows that 
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

- The winner of the election was:
  - Diana DeGette who receieved 73.8% of the vote and 272,892 total votes
