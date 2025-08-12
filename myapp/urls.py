from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('predict/', views.predict_hotspot, name='predict_hotspot'),  # Prediction form
    # path('result/', views.predict_result, name='predict_result'),  # Result page
]

