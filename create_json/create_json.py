import pandas as pd
import json

filename = "musicsketch_faqs.xlsx"
df = pd.read_excel(filename, header=None, names=['section', 'question', 'answer'])
section_names = df['section'].unique()
json_array = []

for section_name in section_names:
    section_dict = dict()
    section_dict['section_name'] = section_name
    question_array = list()
    for index, row in df[df['section'] == section_name].iterrows():
        question_array.append({'question': row['question'], 'answer': row['answer']})
    section_dict['entries'] = question_array
    json_array.append(section_dict)

json_object = json.dumps(json_array)
jsonFile = open("faqs.json", "w")
jsonFile.write(json_object)
jsonFile.close()
