from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:writer_id>', profile, name="profile"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]
