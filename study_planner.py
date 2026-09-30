def study_planner():
    study_plan = []
    plans = int(input("number of study plans:"))#users
    for i in range(plans):
        subject = input("subject:")
        topic = input("topic:")
        day = input("day:")
        study_plan.append({"subject":subject,"topic":topic,"day":day})
    print("Your Study Plans:")#output
    for items in study_plan:
        print(items["subject"],items["topic"],items["day"])
