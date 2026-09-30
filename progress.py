def subject_progress_tracker():
    sub_prog = {}
    num_subs = int(input("Enter number of subjects:"))#for the users
    for i in range(num_subs):
        subjects = input("name of subject:")
        progress = int(input("progress of subject:"))
        sub_prog[subjects]= progress
    print("Your Subject Progress:")
    for output in sub_prog:
        print(output,":",sub_prog[output])#print in form of key and value
    return sub_prog
