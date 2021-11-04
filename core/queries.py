from django.db.models import ExpressionWrapper, FloatField, Sum
from django.db.models.functions import Upper, Lower
from django.db.models.functions import LPad, Cast
from django.db.models import Value as V, CharField, F

from core import models


def test():
    courses = models.Course.objects.all()
    for course in courses:
        print(course.name)


def query01():
    return models.Employee.objects.filter(
        department__description__icontains='TI'
    ).values(
        'id',
        'name',
        'department__description'
    )


def query02():
    return models.Employee.objects.annotate(
        custom_code=LPad(
            Cast(F('id'), output_field=CharField()), 10, V('0')
        )
    ).values('id', 'custom_code')


def query03():
    return models.Employee.objects.annotate(
        name_Upper=Upper('name'),
        name_Lower=Lower('name')
    ).values('name_Upper', 'name_Lower')


def query04():
    return models.Department.objects.annotate(
        calc=ExpressionWrapper(F('salalry_limit') - V(100), output_field=FloatField())
    ).values('salalry_limit', 'calc')


def query05():
    return models.Employee.objects.values('department__description').annotate(
        sum_employee=Sum('salary', output_field=FloatField())
    ).values('department__description', 'sum_employee')
