from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
import json

from api.cache.cache_data import set_cache_data
from api.forms import UploadFileForm
from api.services.data import handle_uploaded_file 

@api_view(['POST'])
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print(f'{request.FILES["file"]}'.split('.')[1])
        # if form.is_valid():
        response = handle_uploaded_file(file= request.FILES["file"], type_=f'{request.FILES["file"]}'.split('.')[1])
        return HttpResponse(response)
    else:
        form = UploadFileForm()
    return HttpResponse('"form": form')



# @api_view(['POST'])
# def get_data(request):
#     if request.method == 'POST':

#         # import the data from the frontend in bytes format
#         file_data_bytes = request.body.decode()

#         # convert the data into a json format as python dictionary type
#         data_dict = json.loads(file_data_bytes)

#         # saving the data into cache for business logic purpose
#         set_cache_data(data_dict)

#     return HttpResponse('ok', status=200)
