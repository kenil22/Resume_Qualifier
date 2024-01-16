from pyresparser import ResumeParser
from docx2pdf import convert
import os 
import json



if 'JD_Info.json' not in os.listdir():
    jd_dict = dict()
else:
    with open('JD_Info.json','r') as json_obj:
        jd_dict = json.load(json_obj)

doc_folder = 'JD_document'
pdf_folder = 'JD_pdf'
for doc_file in os.listdir(doc_folder):
    if doc_file.endswith('.docx'):
        convert(input_path=os.path.join(doc_folder,doc_file),output_path=os.path.join(pdf_folder,doc_file.split('.')[0]+'.pdf'))
        os.remove(os.path.join(doc_folder,doc_file))
        data = ResumeParser(os.path.join(pdf_folder,doc_file.split('.')[0]+'.pdf')).get_extracted_data()

        skills = ''
        if data['skills'] is not None:
            skills = ', '.join(data['skills'])

        experience = ''
        if data['experience'] is not None:
            experience = ', '.join(data['experience'])

        if experience != '':
            final_jd_info = skills + ', '+experience
        else:
            final_jd_info = skills

        jd_dict[doc_file.split('.')[0]] = final_jd_info

with open('JD_Info.json','w') as json_file:
    json.dump(jd_dict, json_file)