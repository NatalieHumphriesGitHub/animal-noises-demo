from application import db                                  #we need to make a class AND an sql table for the database results

class Results(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.String(10))
    noise = db.Column(db.String(10))
    def __str__(self):
        return f"{self.animal} goes {self.noise}"           #the difference here is that the string function doesn't exist in the sql table