# Student Performance Analytics System
# Requirement: FR-002 - Identify At-Risk Students

def analyze_student_performance(student_list):
    """
    This function analyzes student performance data to calculate 
    average scores and classify students into performance categories.
    
    Categories:
    - At Risk: Average < 50%
    - Satisfactory: Average 50% to 69%
    - Good Performer: Average >= 70%
    """
    
    # Initialize counters
    at_risk_count = 0
    satisfactory_count = 0
    good_performer_count = 0
    
    # Process each student (LOOP STRUCTURE)
    for student in student_list:
        total_score = 0
        module_count = 0
        
        # Calculate total of all scores (NESTED LOOP)
        for score in student['scores']:
            total_score = total_score + score
            module_count = module_count + 1
        
        # Calculate average (IF-ELSE STRUCTURE)
        if module_count > 0:
            average_score = total_score / module_count
        else:
            average_score = 0
        
        # Classify student based on average (IF-ELSE STRUCTURE)
        if average_score < 45:  # Changed threshold from 50 to 45
            student['status'] = "At Risk"
            student['average'] = average_score
            at_risk_count = at_risk_count + 1
        elif average_score >= 45 and average_score < 70:  # Adjusted threshold
            student['status'] = "Satisfactory"
            student['average'] = average_score
            satisfactory_count = satisfactory_count + 1
        else:
            student['status'] = "Good Performer"
            student['average'] = average_score
            good_performer_count = good_performer_count + 1
    
    # Display results
    print("\n===== STUDENT PERFORMANCE REPORT =====\n")
    
    for student in student_list:
        print(f"Student: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Average: {student['average']:.2f}%")
        print(f"Status: {student['status']}")
        print("-" * 40)
    
    print("\n===== SUMMARY =====")
    print(f"At Risk Students: {at_risk_count}")
    print(f"Satisfactory Students: {satisfactory_count}")
    print(f"Good Performers: {good_performer_count}")
    print(f"Total Students: {len(student_list)}")
    
    return {
        'at_risk': at_risk_count,
        'satisfactory': satisfactory_count,
        'good_performer': good_performer_count
    }


# Test the function with sample data
if __name__ == "__main__":
    # Sample student data
    students = [
        {'name': 'Ahmed', 'scores': [85, 90, 78, 92]},
        {'name': 'Sara', 'scores': [45, 38, 42, 35]},
        {'name': 'Mohammed', 'scores': [55, 62, 58, 65]},
        {'name': 'Fatima', 'scores': [72, 85, 68, 75]},
        {'name': 'Ali', 'scores': [48, 52, 45, 55, 60]},  # Added one more score
        {'name': 'Maryam', 'scores': []}
    ]
    
    # Run analysis

    results = analyze_student_performance(students)

