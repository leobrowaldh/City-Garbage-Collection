# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import GCRequest
from .forms import GCRequestForm
import datetime
# Create your views here.
def home(req):
    return render(req,'clientapp/home.html')

def contact_us(req):
    return render(req,'clientapp/contact_us.html')

def request_view(req):
    if(req.user.is_authenticated):
        return render(req,'clientapp/request.html',{'form':GCRequestForm()})
    else:
        return redirect('/')

def requests_view(req):
    if(req.user.is_authenticated):
        requests=GCRequest.objects.filter(user=req.user)
        return render(req,'clientapp/requests.html',{'requests':requests})
    else:
        return redirect('/')

def post_request(req):
    if req.method=='POST':
        form = GCRequestForm(req.POST, req.FILES)
        if form.is_valid():
            data=form.cleaned_data
            rq=GCRequest(user=req.user,
                        description=data['description'],
                        image=data['image'],
                        latitude=data['latitude'],
                        longitde=data['longitde'],
                        requested_on=datetime.datetime.now())
            rq.save()
            return redirect('/requests')
    else:
        form=GCRequestForm()
    return render(req,'clientapp/request.html',{'form':form})
