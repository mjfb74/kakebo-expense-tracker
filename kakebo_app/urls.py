from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enter_expense/', views.enter_expense, name='enter_expense'),
    path('get_sums/', views.get_sums, name='get_sums'),
    path('category_detail/<str:category>/<str:year>/<str:month>/', views.category_detail, name='category_detail'),
    path('expenses_list/', views.expenses_list, name='expenses_list'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
