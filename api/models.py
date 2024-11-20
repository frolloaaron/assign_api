from main import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String)
    title = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "teacher": self.teacher,
            "title": self.title
        }
    
class Score(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student = db.Column(db.Integer, db.ForeignKey(Student.id, ondelete="CASCADE"))
    assignment = db.Column(db.Integer, db.ForeignKey(Assignment.id, ondelete="CASCADE"))
    score = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "student": Student.query.get(self.student),
            "assignment": Assignment.query.get(self.assignment),
            "score": self.score
        }

