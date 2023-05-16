from django.urls import path

from ML_algo.controllers.predict_API import prediction_api

urlpatterns = [
    
    path('data/', prediction_api, name = 'data'),
    # path('description/', post_data, name = 'data'),
    
    
    
]