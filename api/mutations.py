from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Student, Assignment, Score

# Student mutation Resolvers
@convert_kwargs_to_snake_case
def resolve_create_student(obj, info, name):
    student = Student(
        name=name
    )
    db.session.add(student)
    db.session.commit()
    payload = {
        "success": True,
        "student": student.to_dict()
    }

    return payload

@convert_kwargs_to_snake_case
def resolve_delete_student(obj, info, student_id):
    try:
        student = Student.query.get(student_id)
        db.session.delete(student)
        db.session.commit()
        payload = {
            "success": True,
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {student_id} not found"]
        }   

    return payload

#Assignment mutation Resolvers
@convert_kwargs_to_snake_case
def resolve_create_assignment(obj, info, teacher, title):
    assignment = Assignment(
        teacher=teacher,
        title=title
    )
    db.session.add(assignment)
    db.session.commit()
    payload = {
        "success": True,
        "assignment": assignment.to_dict()
    }

    return payload

@convert_kwargs_to_snake_case
def resolve_delete_assignment(obj, info, assignment_id):
    try:
        assignment = Assignment.query.get(assignment_id)
        db.session.delete(assignment)
        db.session.commit()
        payload = {
            "success": True,
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Assignment matching id {assignment_id} not found"]
        }   

    return payload

#Score mutation resolvers
@convert_kwargs_to_snake_case
def resolve_create_score(obj, info, student_id, assignment_id, score):
    score = Score(
        student = student_id,
        assignment = assignment_id,
        score = score
    )
    db.session.add(score)
    db.session.commit()
    payload = {
        "success": True,
        "score": score.to_dict()
    }

    return payload

@convert_kwargs_to_snake_case
def resolve_delete_score(obj, info, score_id):
    try:
        score = Score.query.get(score_id)
        db.session.delete(score)
        db.session.commit()
        payload = {
            "success": True,
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Score matching id {score_id} not found"]
        }   

    return payload