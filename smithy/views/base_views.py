from django.shortcuts import render
# from django.views.generic import CreateView
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse, reverse_lazy
# from django.shortcuts import render, get_object_or_404
from smithy.views.ko_slogan import process, ko_api, differ, extraction
from smithy.views.en_slogan import enslogan
from smithy.views.ko_model import koslogan

# from django.core.paginator import Paginator

# Create your views here.


def main_slogan(request):
    if request.method == "POST":
        return render(request, "smithy/index.html")
    else:
        return render(request, "smithy/index.html")


def loading_view(request):
    request.session["select"] = request.POST.get("select", None)
    request.session["info"] = request.POST.get("info", None)
    request.session["sim"] = request.POST.get("sim", None)
    return render(request, "smithy/loading.html")


def result(request):
    select = request.session["select"]
    info = request.session["info"]
    sim = request.session["sim"]
    sim = int(sim)
    if select == "ko_slogan":
        text = process(info, sim)
        slogan_list = ko_api(text)
        kor_list = differ(slogan_list)
        total_slogan = extraction(kor_list, sim)
        context = {"slogans": total_slogan, "select": select, "info": info, "sim": sim}
    elif select == "en_slogan":
        slogans = enslogan(info)
        context = {"slogans": slogans, "select": select, "info": info, "sim": sim}
    else:
        slogans = koslogan(info)
        context = {"slogans": slogans, "select": select, "info": info, "sim": sim}

    return render(request, "smithy/result_slogan.html", context=context)