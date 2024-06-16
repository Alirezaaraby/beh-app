from django.shortcuts import render
from dashboard.models import Assessments
from django.db.models import Sum
# Create your views here.

def index(request):
    data = Assessments.objects.filter(pid = request.user.id)
    filtered_data = data.filter(status=2)
    total_score = filtered_data.aggregate(total_score=Sum('score'))['total_score']

    return render(request, "dashboard/reports/index.html", {"data":filtered_data, "total":total_score})