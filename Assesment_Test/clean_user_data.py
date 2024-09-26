import csv
import re
from collections import OrderedDict

 
def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

 
def clean_user_data(input_file, output_file):
    unique_users = OrderedDict()   

 
    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['user_id']
            email = row['email']

            
            if user_id not in unique_users and is_valid_email(email):
                unique_users[user_id] = row

    
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['user_id', 'email', 'name',  ]   
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()   
        for user in unique_users.values():
            writer.writerow(user)

 
if __name__ == "__main__":
    input_csv = 'users.csv'           
    output_csv = 'cleaned_users.csv'   
    
    clean_user_data(input_csv, output_csv)
    print(f"Data cleaned and written to {output_csv}")
