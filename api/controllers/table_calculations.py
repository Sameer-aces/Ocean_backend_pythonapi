from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from requests import Response 

from api.services.table_calculations import table_calc


@api_view(['POST'])
def table_calc_api(request):
    if request.method == 'POST':

        # import the data from the frontend in bytes format
        body_data = request.body.decode('utf-8')

        # convert the data into a json format as python dictionary type
        dict_data = json.loads(body_data)

        # print( "=========================================================\n",type(dict_data), '\n ',dict_data)
        result = table_calc(heading=tuple(dict_data.values())[0], side_heading=tuple(
            dict_data.values())[1], text=tuple(dict_data.values())[2])
        print(type(json.dumps(result)))
        return JsonResponse(result, safe=False, status=200)
