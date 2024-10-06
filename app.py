import os
import pandas as pd

def create_campaign_lists(file_path):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Step 1: Sort by specified SIC codes and filter by industry criteria
        sic_codes_to_sort = [7311, 8721, 8748, 7319, 8742]

        # Extract distinct SIC codes and sort based on the order of sic_codes_to_sort
        data['SIC_CODE'] = data['COMPANY_SIC'].apply(lambda x: [int(code) for code in str(x).split(',') if code.isdigit()])
        data['SIC_CODE_SORT_ORDER'] = data['SIC_CODE'].apply(lambda x: sorted([sic_codes_to_sort.index(code) for code in x if code in sic_codes_to_sort]))
        data.sort_values(by=['SIC_CODE_SORT_ORDER'], inplace=True)

        # Filter by primary industry criteria
        industry_criteria = ['Advertising', 'media', 'marketing', 'consulting', 'tax services', 'financial services', 'wealth plan']
        industry_filter = data['PRIMARY_INDUSTRY'].str.lower().str.contains('|'.join(industry_criteria), na=False)
        category1_data = data[industry_filter]

        # Step 2: Sort and filter based on Seniority Level and Job Type
        seniority_filter = ~data['SENIORITY_LEVEL'].str.lower().str.contains('staff|administration|adminstration', na=False)
        job_type_filter = ~data['JOB_TITLE'].str.lower().str.contains('intern|professor|scientist|engineer|mechanical|mechanics', na=False)

        # Sorting and filtering
        category2_data = data[seniority_filter & job_type_filter]

        # Step 3: Create categories based on Email, Phone Number, and Valid Personal Email
        category1_data = category1_data.drop_duplicates(subset='BUSINESS_EMAIL', keep='first')
        category2_data = category2_data.drop_duplicates(subset='DIRECT_NUMBER', keep='first')
        category3_data = data[data['PERSONAL_EMAIL'].notnull() & ~data['JOB_TITLE'].str.lower().str.contains('intern|professor|scientist|engineer|mechanical|mechanics', na=False)]

        # Save the results to separate CSV files
        category1_file = "Email_Funnel_Campaign_List.csv"
        category2_file = "Conversational_AI_List.csv"
        category3_file = "Social_Media_Campaign_List.csv"

        category1_data.to_csv(category1_file, index=False)
        category2_data.to_csv(category2_file, index=False)
        category3_data.to_csv(category3_file, index=False)

        # Print the number of rows for each category
        print(f"\nNumber of rows in Category 1: {len(category1_data)}")
        print(f"Number of rows in Category 2: {len(category2_data)}")
        print(f"Number of rows in Category 3: {len(category3_data)}")

        print(f"\nCategories created successfully:")
        print(f"- Category 1: {category1_file}")
        print(f"- Category 2: {category2_file}")
        print(f"- Category 3: {category3_file}")

    except Exception as e:
        print(f"Error: {e}")

# Get the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full file path
file_name = "data.csv"
file_path = os.path.join(script_dir, file_name)

# Call the function to create campaign lists
create_campaign_lists(file_path)
