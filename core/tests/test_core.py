from django.contrib.auth.models import User
from core.models import Project, Employee, Equipment, EmployeeEquipment
from unittest import TestCase


class TestProject(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username="testuser")

    def test_add_project(self):
        data = {
            "name": "Project Possible",
        }
        p = Project.objects.create(**data)
        self.assertEqual(
            p.name, data["name"], "Project name fail",
        )


class AssignProject(TestCase):
    def setUp(self) -> None:
        self.user, created = User.objects.get_or_create(username="testuser")
        self.project = Project.objects.create(name="P1")
        self.employee = Employee.objects.create(name="E1")
        self.equipment = Equipment.objects.create(name="Eq1")
 
    def test_create_relation(self):
        rel = EmployeeEquipment.objects.create(
            project=self.project,
            employee=self.employee,
            equipment=self.equipment,
        )

        self.assertEqual(rel.project, self.project, "Project Mismatch",)
        self.assertEqual(rel.employee, self.employee, "Employee Mismatch",)
        self.assertEqual(rel.equipment, self.equipment, "Equipment Mismatch",)
