import os

##returns boolean values that the files are in the folder
submissions_directory="./submissions/"
file_specifications= ["checkpoint.docx","data.sql","documentation.pdf","index.html"]
submission_names= os.listdir(submissions_directory)
print("BEGINNING FILE CHECKING...")
for student_submission in submission_names:
    print(100*"-")
    if '.DS_Store' == student_submission:
        continue
    else:
        try:
            for filename in file_specifications:
                file_exists = os.path.exists(submissions_directory+student_submission+"/"+filename)
                ## checks to see if there is a missing file and gives back error
                if file_exists==False:
                    raise Exception()
            print (student_submission+" Is clear for further analysis")
        except:
            print (student_submission+" Has an incorrect submission,where a following error has occured :")
            print ("Missing File or File Name is Incorrect")
print(100*"-")
print("FINISHED FILE CHECKING...")

    
        

