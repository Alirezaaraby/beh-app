from django.shortcuts import render

# Create your views here.


def index(request):
    # return redirect("dashboard")
    return render(request, "dashboard/index.html")


def daily_evaluation(request):
    return render(request, "dashboard/daily-evaluation/index.html")


def daily_evaluation_create(request):

    if request.method == "POST":
        invention_name = request.POST.get("title")
        invention_details = request.POST.get("details")

        current_datetime = datetime.now()

        date = current_datetime.strftime("%Y-%m-%d")
        time = current_datetime.strftime("%H:%M:%S")

        id = request.user

        patient = Inventions(
            title=invention_name,
            details=invention_details,
            date=date,
            time=time,
            uid=id,
        )
        patient.save()

    return render(request, "dashboard/daily-evaluation/create.html")


def editor(request):
    return render(request, "dashboard/daily-evaluation/editor.html")


def personnel(request):
    return render(request, "dashboard/personnel/index.html")


def substitute(request):
    return render(request, "dashboard/substitute/index.html")


def logs(request):
    return render(request, "dashboard/logs/index.html")


def reports(request):
    return render(request, "dashboard/reports/index.html")
