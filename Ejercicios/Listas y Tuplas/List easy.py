
subjects = input("Enter the subjects of the curse(separate them with a ','): ")
separate_subjects = subjects.split(", ")
list_subjects = list(separate_subjects)

scores = []
failed = []
for subjects1 in list_subjects:
    score = input(f"What was your grade in {subjects1}: ")
    if score.isnumeric():
        score = int(score)
        scores.append(score)
    else:
        print("Not valid")
    if score<10:
        failed.append(subjects1)
for scores1 in range(len(scores)):
    print(f"You have {scores[scores1]} in {list_subjects[scores1 ]}")
    
    
#for subjects1 in range(len(failed)):
#   print(f"You have to re-study {failed[subjects1]})
print(f"You have to re-study {failed}")
