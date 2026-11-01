from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent /"grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.
    """

    weight_final_list = []  # to put calculate number inside
    try:
        with open (GRADES_FILE) as infile:  # open file, with to auto close
                next(infile)  # read next line
                for line in infile:
                    score = process_row(line)
                    weight_final_list.append(score)

    except FileNotFoundError:
        print("Error: grades.csv not found.")
        return None
   
    except Exception as err:
        print(f"Error: {err} ")
        return None

    analyze_grade(weight_final_list)
    


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""

    row = row.strip()  # takeout /n
    parts = row.split(',')  # follow commad cut, get list

    # number of index number -> change to int then put in list
    tests = [int(x) for x in parts [2:6]]  # test [90, 85, 91, 82,], 
    exams = [int(x) for x in parts [6:8]]  # exam [85, 88]
    discussions = [int(x) for x in parts [8:10]]  # discussion [90, 92]
    project_score = int(parts [10])  # project [95]

    test_avg = average_subject(tests)  # compute the average of tests
    exam_avg = average_subject(exams)  # compute the average of exams
    discussion_avg = average_subject(discussions)  # compute the average of discussions, project just one score.
    

    final_grade = weight_final(test_avg, exam_avg, discussion_avg, project_score)  
    # compute the final grade with weight

    return final_grade


def average_subject(subject_list):
    # Return the average of the scores in subject_list.
    if not subject_list:  # if nothing in the list, just return 0, because it not get any number
        return 0
    return sum(subject_list) / len(subject_list)  # sum together, then / how many number
    



def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""

    final_score = (test_avg * TEST_WEIGHT +
                    exam_avg * EXAM_WEIGHT +
                    discussion_avg * DISCUSSION_WEIGHT +
                    project_score * PROJECT_WEIGHT)
    return final_score



def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    
    # ready 5 count
    count_90 = 0
    count_80 = 0
    count_70 = 0
    count_60 = 0
    count_below = 0

    # index the list
    for score in weight_final_list:
        if score >= 90:
            count_90 += 1
        elif score >= 80:
            count_80 += 1
        elif score >= 70:
            count_70 += 1
        elif score >= 60:
            count_60 += 1
        else:
            count_below += 1

    # print output
    print(f"Number of student with final grade 90 or above: {count_90} ")
    print(f"Number of student with final grade 80-89:   {count_80} ")
    print(f"Number of student with final grade 70-79:   {count_70} ")
    print(f"Number of student with final grade 60-69:   {count_60} ")
    print(f"Number of student with final grade below 60:   {count_below} ")


if __name__ == "__main__":
    main()
