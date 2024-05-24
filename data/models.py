from django.db import models

# Create your models here.
class Student(models.Model):
    Student_Id = models.IntegerField()
    Student_Name = models.CharField(max_length=30)
    Student_DOB = models.DateField()
    Student_DOJ = models.DateField()

    def __str__(self):
        return self.Student_Name
    class Meta:
        db_table = 'studentcrud'
