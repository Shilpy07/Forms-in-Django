from rest_framework import routers
from modelform import api_views

router = routers.DefaultRouter()
router.register(r'Student Records', api_views.StudentRecordViewset)
router.register(r'CustomerRecords', api_views.CustomerRecordViewset)
