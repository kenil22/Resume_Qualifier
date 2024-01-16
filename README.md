**Resume Qualifier based on Job Description**
-----------------------------
Description  
-----------------------------
Above given source code can find the best resume from the multiple available resume(word document) format based on the keywords present in Job Description.
For instance, if you are looking for the PHP developer for which you will mention some of the skills of this designtion in JD. These keywords will be the keywords considered to find the best CV.

Kindly follow the below mentioned steps to execute this source code:-
1. create conda env with python version = 3.8.10
2. Install all the requirements
3. Install fasttext model using below mentioned steps :-
   1. Open python shell in command prompt and run --->
   2. import fasttext.util
   3. fasttext.util.download_model('en', if_exists='ignore') 
   4. Note :- This will download FastText word embeddings  of 10 GB which is pre-trained.
4. Install spacy pre-trained model using below mentioned command.
   1. pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
5. Once, all the steps has been completed successfully, you're done with setup.
6. Now, place your Job Descriptions in Doc format in **JD_documents** folder.
7. Place you CVs in **resume_doc_folder**.
8. Run **python JD_info_collector.py**.
9. Run **python resume_skills_finder.py**.
10. Finally, run **python resume_score_finder.py**.
11. After following the 10th step, your result will be displayed in the terminal.
12. PFA screenshots for results.
    
    ![result](https://github.com/kenil22/Resume_Qualifier/assets/73990461/cdf72d62-e1e8-4b87-97b1-f554b7868cfc)
