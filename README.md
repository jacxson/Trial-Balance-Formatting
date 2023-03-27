# Trial-Balance-Formatting
Example notebook for preparing QuickBooks trial balance data for import into CCH Engagement

## CCH Engagement Trial Balance Imports:

### What is CCH Engagement?
CCH Engagement is a powerful accounting software suite that facilitates collaboration and review of work through binders. Each engagement that the firm has with a given client in a given year has its own binder where all of the workpapers for that engagement are stored. At the center of each binder is a trial balance that serves as a single source of truth for all testing that is done in the various workbooks.

### Trial Balance Imports in CCH Engagement
CCH Engagement makes importing trial balances as simple as copying and pasting the entire table for an Excel spreadsheet *as long as the data is in the correct format*. In order to use the Paste TB Import functionality in CCH Engagement, the trial balance must be formatted into 3 columns: "Account Number", "Account Description", and "Balance". The most time and labor intensive aspect of importing trial balances is reformatting client data from various sources (this notebook will use data that emulates a QuickBooks export).

### 