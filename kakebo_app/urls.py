from django.urls import path
from . import views

urlpatterns = [
    path('enter_expense/', views.enter_expense, name='enter_expense'),
    path('get_sums/', views.get_sums, name='get_sums'),
    path('category_detail/<str:category>/<str:year>/<str:month>/', views.category_detail, name='category_detail'),
]
