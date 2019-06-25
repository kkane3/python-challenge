#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os


# In[10]:


#define input and output paths
election_data = os.path.join('election_data.csv')
election_results = os.path.join('ElectionResults.txt')


# In[3]:


#define variables
candidates = [] #list of candidates
candidates_votes = {} #dict to capture candidates with total votes
total_votes = 0


# In[4]:


with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_votes[candidate] = 0
        
        candidates_votes[candidate] = candidates_votes[candidate] + 1
        


# In[5]:


winner_votes = 0
cand_votes = 0
winner = ""
for candidate, cand_votes in candidates_votes.items():
        cand_votes = candidates_votes.get(candidate)
        if cand_votes > winner_votes:
            winner_votes = cand_votes
            winner = candidate


# In[8]:


#Output to terminal
print(f"Elections Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------\n")
#for candidate, cand_votes in candidates_votes.items():
vote_per = 0
for key, value in candidates_votes.items():
    vote_per = (value/total_votes) * 100
    print(f"{key}: {vote_per} {value}")
    #print(f"{candidates_votes[(key)]}")
    #{candidates_votes[int(value)]/total_votes} {candidates_votes[int(value)]}")
print(f"----------------------------------")
print(f"Winner:  {winner}")


# In[13]:


#Output to file
with open(election_results, "w") as output:
    output.write(f"Elections Results")
    output.write("\n")
    output.write(f"--------------------------------")
    output.write("\n")
    output.write(f"Total Votes: {total_votes}")
    output.write("\n")
    output.write(f"----------------------------")
    output.write("\n")
    vote_per = 0
    for key, value in candidates_votes.items():
        vote_per = (value/total_votes) * 100
        output.write(f"{key}: {vote_per} {value}")
        output.write("\n")
    output.write(f"----------------------------------")
    output.write("\n")
    output.write(f"Winner:  {winner}")



# In[ ]:




