# Trial-Balance-Formatting
Example notebook for preparing QuickBooks trial balance data for import into CCH Engagement
---
![](images/tb_transform.png)
#### *** while this project was inspired by a real-world scenario, all data in this project is purely fictitious ***
---
## Overview
Formatting trial balance data from quickbooks exports to import into CCH Engagement can be tedious work, especially for clients with multiple related entities. While it is manageable  to handle this work in excel for companies with 3 or 4 subsidiaries, what if there are dozens? And what if each entity has hundreds of accounts?

This repository was inspired by a real world scenario working in an audit and assurance practice where I was asked to format the trial balances for a company with almost 100 subsidiaries. I decided it was time to put together a scalable ETL workflow for trial balance data using python to automate process from start to finish. The notebooks in this project assume some basic knowledge of python inlcuding data types, control flow, functions, and the pandas library. If you would like to jump straight into the code, check out the [example notebook](example_notebook_tb_formatting.ipynb) or the corresponding [etl script](trial_balance_etl.py) (the two are essentially identical). If you would like a more step by step guide that lays out the thought processes behind each step, check out the [tutorial notebook](tutorial_notebook_tb_formatting.ipynb). 

If you're new to python but curious to learn more about pythonic approaches to accounting workflows, feel free to reach out on [LinkedIn](linkedin.com/in/jacxson). I'd love to chat!

## Methodology
The reformatting of QuickBooks outputs requires three primary steps: 
#### 1. Extract account numbers and descriptive names from strings of nested accounts and subaccounts
The account description column of excel outputs is usually formatted with nested account names and numbers that make it easy for a human reader to understand the structure of accounts at different levels of grouping. The goal of this step is to extract only the lowest level sub-account and its corresponding name. While this may seem like a major challenge, it becomes easier when you begin to recognize patterns in the formatting that exist to make it more readable. In the examples provided, I exploit the existence of delimiters separating account names and numbers and the different account subgroup levels and derive a set of rules that, when applied, will always return the relevant account name and number in separate columns. Since these patterns were the same for all of the related entities, this processing could be automatically applied to every trial balance. 
#### 2. Append 3 character account suffixes to the account numbers to differentiate identical account numbners belonging to different subsidiaries for the consolidated trial balance
Account numbering across related entities is often standardized to facilitate the review of financial information across the entities. This poses a problem when it comes time for consolidation, as accounts from the different entities become indistinguishable. A simple solution is the addition of suffixes to the account numbers (e.g. "1000" becomes "1001.ABC") that serve as keys, mapping the accounts to their respective entities. While this would be a simple task in excel, it still requires you to treat the entities one by one. I suggest a more efficient approach. Since my firm already had an excel table mapping the suffixes to their respective entities, used this table to automatically assign the suffixes to every entity's trial balance.
#### 3. Combine credit and debit columns into a single net balance column
This step is fairly straight forward, a simple question of addition/subtraction that can easily be automated with Python.

## Results
While this certainly required a little bit of strategizing and development work on the front end, it transformed a task that previously took an Auditor several hours into a single script that runs in a matter of seconds. Adapting this workflow to a new set of related entities only requires slight tweaks according to the pattern of account delimiters and a new mapping of entities and account suffixes.



