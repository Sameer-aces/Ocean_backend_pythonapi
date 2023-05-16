from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

from api.services.sort_service import sort


@api_view(['POST'])
def sort_api(request):
    if request.method == 'POST':

        # import the data from the frontend in bytes format
        body_data = request.body.decode('utf-8')

        # convert the data into a json format as python dictionary type
        sort_dict = json.loads(body_data)

        # print("=========================================================\n",
        #   type(sort_dict), '\n ', sort_dict)
        result = sort(action=tuple(sort_dict.values())[0], x=tuple(
            sort_dict.values())[1], y=tuple(sort_dict.values())[2])

        return JsonResponse(result, status=200)
