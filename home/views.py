from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("this is home page")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')


def events(request):
    #return HttpResponse("this is events page")
    return render(request,'events.html')


def gallery(request):
    #return HttpResponse("this is gallery page")
    return render(request,'gallery.html')


def aboutIEI(request):
    #return HttpResponse("this is aboutIEI page")
    return render(request,'aboutIEI.html')


def about_history(request):
    #return HttpResponse("this is about_history page")
    return render(request,'about_history.html')
def about_vision(request):
    #return HttpResponse("this is about_vision page")
    return render(request,'about_vision.html')

def about_team(request):
    #return HttpResponse("this is about_team page")
    return render(request,'about_team.html')

def about_alumni(request):
   # return HttpResponse("this is about_alumni page")
   return render(request,'about_alumni.html')


def aboutIEI_benefits(request):
    #return HttpResponse("this is events_a_y_2018_2019 page")
    return render(request,'IEI_benefits.html')
def aboutIEI_membership(request):
    #return HttpResponse("this is events_a_y_2018_2019 page")
    return render(request,'IEI_membership.html')

def contactus(request):
    #return HttpResponse("this is contactus page")
    return render(request,'contactus.html')

