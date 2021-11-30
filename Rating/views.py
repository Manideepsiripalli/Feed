from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import FeedbackData
from .forms import FeedbackFrom

import datetime as dt
Date=dt.datetime.now()

def Feed_view(request):
    if request.method == 'POST':
        ffrom= FeedbackFrom(request.POST)
        if ffrom.is_valid():
            Name = request.POST.get('Name','')
            Rating= request.POST.get('Rating','')
            Location = request.POST.get('Location','')
            Feedback = request.POST.get('Feedback','')

            Data = FeedbackData(
                Name=Name,
                Rating=Rating,
                Location=Location,
                Feedback=Feedback

            )

            Data.save()
            fform=FeedbackFrom()
            Feedback=FeedbackData.objects.all()
            return render(request,'Feedback.html',{'fform':fform,'Feedback':Feedback})
    else:
            Feedback= FeedbackData.objects.all()
            fform=FeedbackFrom()
            return render(request,'Feedback.html',{'fform':fform,'Feedback':Feedback})










