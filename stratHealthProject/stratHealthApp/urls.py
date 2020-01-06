from django.urls import include, path
from rest_framework import routers
from . import controller
from . import views

router = routers.DefaultRouter()
router.register('hospital_groups', controller.HospitalGroupViewSet)
router.register('hospital', controller.HospitalViewSet)
router.register('contact', controller.ContactViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.index, name="index"),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('log_user_out/', views.log_user_out, name='log_user_out'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
