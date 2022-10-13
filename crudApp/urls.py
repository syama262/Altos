from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.show_regform,name='show_regform'),
    path('add_employeeDetails',views.add_employeeDetails,name='add_employeeDetails'),
    path('show_employeeDetails',views.show_employeeDetails,name='show_employeeDetails'),
    path('editPage/<int:pk>',views.editPage,name='editPage'),
    path('deletePage/<int:pk>',views.deletePage,name='deletePage'),
    path('edit_employeeDetails/<int:pk>',views.edit_employeeDetails,name='edit_employeeDetails'),
    path('delete_Employee/<int:pk>',views.delete_Employee,name='delete_Employee'),
]