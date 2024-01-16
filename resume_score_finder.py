import json
from sentence_similarity import fast_text_similarity_finder

#Flutter
#Front-end Developer
#PHP
technology = 'PHP' #Choose from above any one

with open('resume_skills.json','r') as json_obj:
    resume_skills = json.load(json_obj)

with open('JD_Info.json','r') as json_obj:
    jd_requirement = json.load(json_obj)

required_tech_stack = jd_requirement[technology]

final_score = dict()
score_list = list()
for candidate,candidate_skills in resume_skills.items():
    score = fast_text_similarity_finder(required_tech_stack, candidate_skills)
    final_score[score] = candidate
    score_list.append(score)
    
score_list = sorted(score_list, reverse=True)
print(score_list)
print('----------------------------------------------------------------------------')
print("Below are the top 3 candidates based on skills mentioned in Job Description for {}".format(technology))
print('----------------------------------------------------------------------------')
for i in range(0,3):
    print("{} has score of {}".format(final_score[score_list[i]], score_list[i])) 
    print('*'*10)
