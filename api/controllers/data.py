from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
import json
import tabula
import pandas as pd
from api.cache.cache_data import set_cache_data
from api.forms import UploadFileForm
from api.services.data import handle_uploaded_file 

@api_view(['POST'])
def upload_file(request):
    print(" we are in uplaod fle")
    if request.method == "POST":
        print(request.body)
        form = UploadFileForm(request.POST, request.FILES)
        print(f'{request.FILES["file"]}'.split('.')[1])
        # if form.is_valid():
        response = handle_uploaded_file(file= request.FILES["file"], type_=f'{request.FILES["file"]}'.split('.')[1])
        # print(response)

        if f'{request.FILES["file"]}'.split('.')[1] == 'pdf':
            input_file = 'C:/Users/DELL/Desktop/ocean_backend/api/services/data.pdf'
            tables = tabula.read_pdf(input_file, pages='all', multiple_tables=True)
            df = pd.concat(tables, ignore_index=True)
            df_dict = df.to_dict()
            # cols = json.loads()
            data_arr = []
            data_arr.append(df.columns.tolist())
            data_arr.append(df.values.tolist())
            # sheet = {"cols":(df.columns),
            #          "vals":(df.values)}
            vals = json.loads(data_arr)
            print(data_arr, 'type-',type(data_arr))   
            
            return JsonResponse(vals)
        else:
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
