# Trial-Balance-Formatting
Example notebook for preparing QuickBooks trial balance data for import into CCH Engagement
![](images/tb_transform.png)

## Overview
Formatting trial balance data from quickbooks exports to import into CCH Engagement can be tedious work, especially for clients with multiple subsidiaries. While it is manageable for companies with 3 or 4 subsidiaries to handle this work in excel, what if there are dozens of them!? This project was inspired by a real world application where I was asked to format the trial balances with a company with 75 subsidiaries, and decided it was time to put together a scalable ETL workflow for trial balance data. The notebooks in this project assume some basic knowledge of python inlcuding data types, control flow, and functions, and the pandas library. If you would like to jump straight into the code, check out the [example notebook](tb_formatting_example.ipynb) or the corresponding [etl script](tb_formatting_etl.py) file. If you would like a more step by step guide that lays out how I arrived at the code in those files, check out the tutorial_notebook_tb_formatting.ipynb
