from modelform.models import *
from rest_framework import viewsets
from modelform import serializers


class StudentRecordViewset(viewsets.ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = serializers.StudentRecordSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name',)
    extra_kwargs = {'url': {'lookup_field': 'name'}}

    #def get_queryset(self):
        #data = self.filter_queryset(StudentRecord.objects
        #                             .filter(id=2)
        #                             .values_list('id', 'name'))
        #   data = self.filter_queryset(StudentRecord.objects.values_list('name', 'enrollment', 'address__name', 'address__items', 'address__items__name'))
        # data = self.filter_queryset(StudentRecord.objects.all())
        # data = StudentRecord.objects.select_related('address').all()
        # students = []
        #
        # for student in data:
        #     students.append({'enrollment': student.enrollment, 'name': student.name, 'address': student.address.name})
        #
        # return students
        # for i in data:
        #print(students)
        # data = self.filter_queryset(StudentRecord.objects.annotate(Count('enrollment')))
        # for i in data:
        #     print(i.enrollment__count)

      #  return data


class CustomerRecordViewset(viewsets.ModelViewSet):
    queryset = CustomerRecord.objects.all()
    serializer_class = serializers.CustomerRecordSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name',)
    extra_kwargs = {'url': {'lookup_field': 'name'}}
