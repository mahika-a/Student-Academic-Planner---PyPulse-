def performance_insights(subject_progress):

    if not subject_progress:
        print("Wait, you haven't entered any subject progress yet! Run option 1 first.")
        return
    for subject in subject_progress:
        score = subject_progress[subject]
        if 0<=score<20:
            print(subject, ": needs critical attention")
        elif 20<=score<50:
            print(subject, ": needs attention")
        elif 50<=score<90:
            print(subject, ": working fine")
        elif 90<=score<100:
            print(subject, ": almost completed")
        else:
            print(subject, ": completed successfully")