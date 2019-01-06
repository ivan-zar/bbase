from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.patient_choice, name='index'),
    path('patient/<int:patient_id>/', views.patient, name="patient"),
    path('/patient_choice', views.patient_choice, name="patient_choice"),
    path('new_patient', views.new_patient, name="new_patient"),
    path('new_test/<int:patient_id>/', views.new_test, name="new_test"),
    path('test/<int:patient_id>/<int:test_id>/', views.test, name="test"),
    path('delete_test/<int:patient_id>/<int:test_id>', views.delete_test, name="delete_test"),
    path('admin/', admin.site.urls),
]