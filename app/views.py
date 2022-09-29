from django.shortcuts import render,HttpResponse,redirect
from .models import Messagebox
from app.forms import Form1
import requests
#from . import requests

# Create your views here.

def home(request):
    if request.method == 'POST':

        data = request.POST.copy()
        form = Form1(request.POST or None)
        if form.is_valid():
            newdata = form.save()
          
        task = Messagebox.objects.get(pk=newdata.pk)

        Client_Name = task.Name
        Client_Mail = task.Email

        http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client_Name + " for " + Client_Mail + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
        requests.get(http_req)

        return render(request,'thankyou.html')
        #return redirect('/')
        #return HttpResponse("Sent Message!!!")

    return render(request,'home.html')


    