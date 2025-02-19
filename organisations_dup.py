import pandas as pd
from fuzzywuzzy import fuzz

def check_similarity(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    return fuzz.ratio(string1, string2)

def mark_duplicates(input_file, output_file, log_file):
    df = pd.read_csv(input_file)
    df['similar_name_to_row'] = None

    with open(log_file, "w") as log:  # Open log file in write mode
        for i, row1 in df.iterrows():
            for j in range(i + 1, len(df)):
                if i != j:
                    # Comparing column organisation_name only
                    ith_organisation_name = str(row1['organisation_name'])
                    jth_organisation_name = str(df.at[j, 'organisation_name'])  # Fixed `j` index

                    if not ith_organisation_name or not jth_organisation_name:
                        log.write(f"One of the rows is empty... (Row {i} or {j})\n")
                        continue

                    if ith_organisation_name[0] != jth_organisation_name[0]:
                        continue

                    similarity_score = check_similarity(ith_organisation_name, jth_organisation_name)

                    if similarity_score > 80:
                        log.write(f"These two names are similar:\n")
                        log.write(f"{i}th row's name: {df.at[i, 'organisation_name']}\n")
                        log.write(f"{j}th row's name: {df.at[j, 'organisation_name']}\n\n")

                        if pd.notna(df.at[i, 'similar_name_to_row']):
                            df.at[i, 'similar_name_to_row'] += f",{j+2}"
                        else:
                            df.at[i, 'similar_name_to_row'] = str(j+2)
        # df.to_csv(output_file)
        print("Loop has ended....\n")

input_file = 'global_organisations_first_500_ASC.csv'
output_file = 'merged_first_500.csv'
log_file = "duplicates_log.txt"

mark_duplicates(input_file, output_file, log_file)

                        
                        

