# practice

takeoff_checklist = [
    "Put on suit",
    "Seal hatch",
    "Check cabin pressure",
    "Fasten seatbelt"]

spacewalk_checklist = [
    "Put on suit",
    "Check oxygen",
    "Seal helmet",
    "test radio",
    "Open airlock"]

# .append can be used to add to a predefined list
takeoff_checklist.append("Tell mission control checks are complete")

# lists are treated as arrays, and indiviual indexes can
# be called on to print and/or modify
print(takeoff_checklist[1])
del (takeoff_checklist[2])

flight_manual =[takeoff_checklist, spacewalk_checklist]
# flight manual is now an array of arrays, and includes two sep lists

skills_list = takeoff_checklist + spacewalk_checklist
# skills list is now saved as a combination of both takeoff and spacewalk checklists
# and includes all indexes from both as a single list
