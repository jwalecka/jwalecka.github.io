import pandas as pd
from collections import defaultdict
import json

filename = "musicsketch_faqs.xlsx"
df = pd.read_excel(filename, header=None, names=['section', 'question', 'answer'])
sections_dict = defaultdict(dict)

for index, row in df.iterrows():
    current_dict = sections_dict[row['section']]
    current_dict[len(current_dict)] = {'question': row['question'], 'answer': row['answer']}
    sections_dict[row['section']] = current_dict

json_object = json.dumps(sections_dict)
jsonFile = open("faqs.json", "w")
jsonFile.write(json_object)
jsonFile.close()