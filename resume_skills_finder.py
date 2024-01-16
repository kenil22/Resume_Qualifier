from pyresparser import ResumeParser
from docx2pdf import convert
import os 
import json

if 'resume_skills.json' not in os.listdir():
    resume_dict = dict()
else:
    with open('resume_skills.json','r') as json_obj:
        resume_dict = json.load(json_obj)

doc_folder = 'resume_doc_folder'
pdf_folder = 'resume_pdf_folder'
for doc_file in os.listdir(doc_folder):
    if doc_file.endswith('.docx'):
        convert(input_path=os.path.join(doc_folder,doc_file),output_path=os.path.join(pdf_folder,doc_file.split('.')[0]+'.pdf'))
        os.remove(os.path.join(doc_folder,doc_file))
        data = ResumeParser(os.path.join(pdf_folder,doc_file.split('.')[0]+'.pdf')).get_extracted_data()
        skills = ', '.join(data['skills'])
        resume_dict[doc_file] = skills

with open('resume_skills.json','w+') as json_obj:
    json.dump(resume_dict, json_obj)