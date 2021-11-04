from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=False,
        auto_now=True
    )

    class Meta:
        managed = True
        abstract = True


class Department(ModelBase):
    description = models.CharField(
        db_column='tx_description',
        null=False,
        max_length=54,
        unique=True
    )

    salalry_limit = models.DecimalField(
        db_column='nb_salary_limit',
        null=False,
        default=0,
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.description


class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=104
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False
    )

    salary = models.DecimalField(
        db_column='nb_salary',
        null=False,
        default=10000.00,
        max_digits=10,
        decimal_places=2,
    )

    courses = models.ManyToManyField(
        to='Course',
        through='EmployeeCourse'
    )

    class Meta:
        db_table = 'Employee'


class Course(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=104,
        unique=True
    )
    employees = models.ManyToManyField(
        to='Employee',
        through='EmployeeCourse'
    )

    class Meta:
        db_table = 'course'


class EmployeeCourse(ModelBase):
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False
    )
    course = models.ForeignKey(
        to='Course',
        on_delete=models.DO_NOTHING,
        db_column='id_course',
        null=False
    )

    class Meta:
        db_table = 'employee_course'
        unique_together = [
            ('employee', 'course')
        ]
