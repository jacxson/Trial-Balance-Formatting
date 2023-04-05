import pandas as pd
import os




def new_col_from_split(df, split_col, delim, index = -1):
    return [x[index] for x in df[split_col].astype(str).str.split(delim)]


def create_entity_dict(df, entity_column, suffix_column, data_folder='./quickbooks_data/'):
    file_list = os.listdir(data_folder)
    return {x + '.xlsx': '.' + y for x, y in zip(df[entity_column], df[suffix_column]) if x + '.xlsx' in file_list}


def format_tbs(entities, data_folder='./quickbooks_data/'):
    
    if 'ready_for_tb_import' not in os.listdir():
        os.mkdir('./ready_for_import/')
        
    if 'processed_quickbooks_files' not in os.listdir():
        os.mkdir('./processed_quickbooks_files/')
        
    for entity, suffix in entities.items():
        
        # Print statement to help with debugging if one of the QuickBooks files is formatted differently
        print(f'formatting {entity}')
        
        # Create a dataframe from the QuickBooks export file
        df = pd.read_excel(f'{data_folder}{entity}', sheet_name='Sheet1', skiprows=4)
        
        # Drop the unneeded Total row
        if 'total' in df.iloc[len(df) - 1, 0].lower():
            df.drop(index=len(df) - 1, inplace=True)
            
        # Replace nan values with 0 
        df.fillna(0, inplace=True)
        
        # Split combined name and account coloumn into separate name and account column, adding the suffix to the end of the account numbers.
        df['_col'] = new_col_from_split(df, 'Unnamed: 1', ':')
        df['account_number'] = [account + suffix for account  in new_col_from_split(df, '_col', ' · ', index=0)]
        df['account_name'] = new_col_from_split(df, '_col', ' · ')
        
        # Combine debit and credit columns into a single balance column
        df['balance'] = df['Debit'] - df['Credit']
        
        # Export account number, account name, and balance columns to a new excel file in ready_for_import folder
        df[['account_number', 'account_name', 'balance']].to_excel(f'./ready_for_tb_import/formatted_tb_{entity}', index=False)
        
        # Move QuickBooks excel file to import_file_created folder
        os.rename(f'./{data_folder}/{entity}', f'./processed_quickbooks_files/{entity}')
        
        # Print statement confirming successful formatting to help with debugging
        print(f'formatted_tb_{entity} successfully created')
        
        
if __name__ == 'main':
    
    df_keys = pd.read_excel('account_keys.xlsx')
    entity_dict = create_entity_dict(df_keys, entity_column='Entity', suffix_column='Acronym')
    format_tbs(entity_dict)