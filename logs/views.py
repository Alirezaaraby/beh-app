from django.shortcuts import render
from dashboard.models import Assessments
import csv
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    data = Assessments.objects.all()
    
    if request.method == "POST":
        selected_columns = request.POST.getlist("columns")
        print("Selected columns:", selected_columns)

        # Define a mapping of form values to model field names
        column_mapping = {
            "pid": "pid",
            "assessor_id": "assessor_id",
            "occure_date": "occure_date",
            "occure_time": "occure_time",
            "in_id": "in_id",
            "it_id": "it_id",
            "score": "score",
            "status": "status",
            "record_id": "record_id",
            "record_date": "record_date",
            "record_time": "record_time",
            "current": "current",
            "forecastEffectTime": "forecastEffectTime",
            "realeffect_time": "realeffect_time",
            "description": "description"
        }

        fields_to_include = [column_mapping[col] for col in selected_columns if col in column_mapping]

        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="assessments.csv"'
        response.write('\ufeff'.encode('utf8'))

        writer = csv.writer(response)

        writer.writerow([col for col in selected_columns if col in column_mapping])
        
        for assessment in data:
            row = [getattr(assessment, field) for field in fields_to_include]
            writer.writerow(row)

        return response

    return render(request, "dashboard/logs/index.html", {"data": data})