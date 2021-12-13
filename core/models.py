from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=256)

    def __repr__(self):
        return f"<Project: {self.name}>"

class Employee(models.Model):
    name = models.CharField(max_length=256)

    def __repr__(self):
        return f"<Employee: {self.name}>"


class Equipment(models.Model):
    name = models.CharField(max_length=256)

    def __repr__(self):
        return f"<Equipment: {self.name}>"


class EmployeeEquipment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now_add=True)
