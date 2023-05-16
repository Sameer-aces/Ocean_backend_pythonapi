from django.shortcuts import  HttpResponse
from rest_framework.decorators import api_view
import json

from ML_algo.services.predict_service import prediction


@api_view(['POST'])  
def prediction_api(request):
    if request.method == 'POST':
        
        # import the data from the frontend in bytes format 
        form_data_bytes = request.body.decode('utf-8')
       
        # convert the data into a json format as python dictionary type
        data_dict = json.loads(form_data_bytes) 

        result = prediction(data_dict)
        return HttpResponse(result ,status = 200)
    