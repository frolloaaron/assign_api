from .models import Student, Assignment, Score
from ariadne import convert_kwargs_to_snake_case

#Student query resolvers
def resolve_students(obj, info):
    try:
        students = [student.to_dict() for student in Student.query.all()]
        payload = {
            "success": True,
            "students": students
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_student(obj, info, student_id):
    try:
        student = Student.query.get(student_id)
        payload = {
            "success": True,
            "student": student.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Stuident matching id {student_id} not found"]
        }

    return payload

# Assignment query resolvers
def resolve_assignments(obj, info):
    try:
        assignments = [assignment.to_dict() for assignment in Assignment.query.all()]
        payload = {
            "success": True,
            "assignments": assignments
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_assignment(obj, info, assignment_id):
    try:
        assignment = Assignment.query.get(assignment_id)
        payload = {
            "success": True,
            "assignment": assignment.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Assignment matching id {assignment_id} not found"]
        }

    return payload

# Score query resolvers
def resolve_scores(obj, info):
    try:
        scores = [score.to_dict() for score in Score.query.all()]
        payload = {
            "success": True,
            "scores": scores
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_scores_student(obj, info, student_id):
    try:
        scores = [score.to_dict() for score in Score.query.filter(Score.student == student_id)]
        payload = {
            "success": True,
            "scores": scores
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload