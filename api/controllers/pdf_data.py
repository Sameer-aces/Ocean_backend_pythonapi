from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
import tabula
import pandas as pd

from api.services.sort_service import sort


@api_view(['POST'])
def pdf_data(request):
    if request.method == 'POST':
        # import the data from the frontend in bytes format
        print(request.body)
        body_data = request.body.decode('utf-8')
        input_file = 'C:/Users/DELL/Desktop/ocean_backend/api/services/data.pdf'
        tables = tabula.read_pdf(input_file, pages='all', multiple_tables=True)
        df = pd.concat(tables, ignore_index=True)
        print(df)

        return JsonResponse(df, status=200)
