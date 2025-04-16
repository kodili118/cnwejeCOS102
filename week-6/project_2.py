def check_admission(candidates):
    admitted = []
    not_admitted = []

    for candidate in candidates:
        name = candidate["name"]
        dept = candidate["department"].lower()
        jamb_score = candidate["jamb_score"]
        credits = candidate["credits"]
        interview_passed = candidate["interview_passed"]

        # Admission criteria 
        if dept == "computer science":
            if jamb_score >= 250 and credits >= 5 and interview_passed:
                admitted.append(name)
            else:
                not_admitted.append(name)
        elif dept == "mass communication":
            if jamb_score >= 230 and credits >= 5 and interview_passed:
                admitted.append(name)
            else:
                not_admitted.append(name)
        else:
            print(f"Unknown depertment for candidate {name}")

    return admitted, not_admitted 

# Candidates example:
candidates = [
    {"name": "Janice", "department": "Computer Science", "jamb_score": 270, "credits": 6, "interview_passed": True},
    {"name": "Alexis", "department": "Computer Science", "jamb_score": 305, "credits": 7, "interview_passed": True},   
    {"name": "Esther", "department": "Mass Communication", "jamb_score": 180, "credits": 5, "interview_passed": False},
    {"name": "Ebube", "department": "Mass Communication", "jamb_score": 310, "credits": 7, "interview_passed": True},
    {"name": "Emeka", "department": "Computer Science", "jamb_score": 300, "credits": 4, "interview_passed": False},
]

admitted, not_admitted = check_admission(candidates)
print("Admitted:", admitted)
print("Not Admitted:", not_admitted)