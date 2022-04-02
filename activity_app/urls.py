from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('api/task', TaskViewSet, 'task')
router.register('api/category', CategoryViewSet, 'category')
router.register('api/question', QuestionViewSet, 'question')
router.register('api/test', TestViewSet, 'test')


urlpatterns = router.urls