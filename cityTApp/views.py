from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from .forms import UserForm,Userdb,Agentdb,AgentForm,UserloginForm,AgentloginForm
from datetime import date

from.models import User,Agent,TripPlan,Attraction,Passenger,Ticket
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout 

from datetime import datetime
import razorpay
# Create your views here.

def index(request):
    trip_plans = TripPlan.objects.all()
    for trip in trip_plans:
        print(trip.city)
    context = {'trip':trip_plans}
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')


def service(request):
    return render(request,'service.html')


def registration(request):
    return render(request,'registration.html')

def user_registration(request):
    if request.method == 'POST':
        context = {}
        form = Userdb(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            context['form']=form
            return render(request,'display.html',context)
    else:
        form = UserForm()
        print(form.fields['dob'])
        return render(request,'user_registration.html',{'form':form})
    
def agent_registration(request):
    if request.method == 'POST':
        context={}  
        form = Agentdb(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            context['form']=form
            return render(request,'index.html',context)
        else:
            messages.error(request,'')
            messages.error(request,"some unique constrain vioalate")
            return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        form = AgentForm()
        return render(request,'Agent_registration.html',{'form':form})
    
def user_login(request):
    if request.method == 'POST':
        print('is valid')
        form = AuthenticationForm(request, data=request.POST)
        print(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print("usename "+username)
        print("password "+password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:    
            u = User.objects.get(username=user.username)
            print(u)
            request.session['username'] = u.username
            print(request.session.get('username'))
            request.session['userid'] = u.id
            print(request.session.get('userid'))
            login(request, user)
            print("yes its working...")
            # messages.info(request, f"You are now logged in as {username}.")
            # return HttpResponse("login successfully")
            return redirect('index')
        else:
            print("gooooooooo")
            messages.error(request, '')
            messages.error(request,"Invalid username or password.")
            return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        form = UserloginForm()
        return render(request,'User_login.html',{'form':form})

def agent_login(request):
    if request.method == 'POST':
        print("post method")
        form = AgentloginForm(request.POST)
        print(form)
        if form.is_valid():
            print("is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print(username+" "+password)
            agent = authenticate(request, username=username, password=password)
            # print(agent)
            if agent is not None:
                request.session['agentname'] = agent.username
                print(request.session.get('agentname'))
                request.session['agentid'] = agent.id
                print(request.session.get('agentid'))
                print("login start")
                login(request, agent)
                print("login end")
                return redirect('index')
            else:
                # Handle invalid credentials
                print("error in agent")
                messages.error(request,'')
                messages.error(request,"Invalid username or password.")
                return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        form = AgentloginForm()
        return render(request, 'agent_login.html', {'form': form})

       
def log_out(request):
    logout(request)
    # messages.info(request, "You have successfully logged out.")
    # messages.error(request,'')
    return redirect('index')

def package_view(request):
    # for pack in packeges:
    request.session['is_editable']=0
    print("status")
    print(request.session.get('is_editable'))   
    context = {}
    context["dataset"] = TripPlan.objects.all()
    return render(request,"package.html",context)

def add_trip_plan(request):
    if request.method=='POST':
       print("start trip")
       agency_id = request.session.get('agentid')
       agent = Agent.objects.get(pk=agency_id)
       trip_name = request.POST['name']
       city = request.POST['city']
       price = request.POST['price']
       capacity = request.POST['capacity']
       depa_date = request.POST['depa_date']
       depa_time = request.POST['depa_time']
       depa_place = request.POST['depa_place']
       return_date = request.POST['return_date']
       return_time = request.POST['return_time']
       return_place = request.POST['return_place']
       special = request.POST['special']
       img = request.FILES.get('thumbnail')
        #   validation

       date_format = "%Y-%m-%d"
       depa_date_obj = datetime.strptime(depa_date, date_format)
       return_date_obj = datetime.strptime(return_date,date_format)
       sub_date = (return_date_obj - depa_date_obj)
       a_duration = sub_date.days
       
       if depa_date > return_date or a_duration<=1:
           messages.error(request,'')
           messages.error(request,"check departure and return date again")
           return redirect(request.META.get('HTTP_REFERER','/'))
       
       
       form = TripPlan(agency_id=agent,trip_name=trip_name,city=city,price=price,capacity=capacity,departure_date=depa_date,departure_time=depa_time,departure_place=depa_place,return_date=return_date,return_time=return_time,return_place=return_place,duration=a_duration,extra_info=special,thumbnail=img)
       form.save()
       request.session['trip_id'] = form.id 
       print(request.session.get('trip_id'))
       print("savessssssss")
       return redirect('add_att')
    else:    
        # form = ImageForm()
        return render(request,'Trip_plan_form.html')
    
def view_trip_details(request,pack_id):
    print("hello its working")
    attraction = Attraction.objects.filter(trip_id=pack_id)
    for att in attraction:
        print(att.att_imgs)
    context={}
    trip_deatails = TripPlan.objects.filter(id=pack_id).first()

    print("tripppppppppppppppp")
    print(trip_deatails.agency_id)
    agent = Agent.objects.get(username=trip_deatails.agency_id)
    context['pack'] = trip_deatails
    context['other1']={'agent_instance':agent}
    print(context['pack'].trip_name)
    context['other']={'attraction':attraction}

    return render(request,'trip_details.html',context)


def make_session_for_att(request):
    if request.method == 'POST':
        request.session['trip_name'] = request.POST['trip_name']
        print(request.session.get('trip_name'))
        return redirect('add_att')
    else:
        return render(request,'make_session.html')


def add_att(request):
    if request.method == 'POST':
        print("its working .........")
        att_name = request.POST.get('name')
        img = request.FILES.get('img')
        trip_id = request.session.get('trip_id')
        trip_plan_instance = TripPlan.objects.get(pk=trip_id)
        att_instance = Attraction.objects.create(trip_id=trip_plan_instance, name=att_name, att_imgs=img)
        return redirect('add_att')
    else:
        print("else workin....")
        trip_id = request.session.get('trip_id')
        trip_plan_instance = TripPlan.objects.get(pk=trip_id)
        attractions = Attraction.objects.filter(trip_id=trip_id)
        context = {'attractions': attractions}
        for attraction in attractions:
          print(attraction.att_imgs)
        return render(request, 'add_att.html', context)
    
def del_att(request,id):
        Attraction.objects.filter(id=id).delete()
        print("complete")
        return redirect(request.META.get('HTTP_REFERER','/'))

def edit_att(request,id):
            if request.method == 'POST':
               print("update")
               attraction = get_object_or_404(Attraction,id=id)
               attraction.att_imgs = request.FILES['img']
               print(request.FILES['img'])
               attraction.name = request.POST['name']
               attraction.save()
               del request.session['is_edit']
               return redirect('add_att')
            else:
               trip_id = request.session.get('trip_id')
               trip_plan_instance = TripPlan.objects.get(pk=trip_id)
               print("trip_id")
               print(trip_id)
               request.session['is_edit'] = 1
               print(request.session.get('is_edit'))
               trip_id = request.session.get('trip_id')
               attraction_instance = Attraction.objects.get(pk=id)
               attractions = Attraction.objects.filter(trip_id=trip_id)
               print(attraction_instance.name)
               
               context = {'attractions':attractions}
               context['other'] = {'instance': attraction_instance}
               for attraction in attractions:
                 print(attraction.att_imgs)
               return render(request, 'add_att.html', context)
               
def dummy(request):
    # attraction = get_object_or_404(Attraction,trip_id=12)
    # attraction.att_imgs
    attraction = Attraction.objects.filter(trip_id=12)
    for att in attraction:
        print(att.att_imgs)
    # return HttpResponse("WELCOME")
        context={}
        context['attractions']=attraction
    return render(request,'index2.html',context)

def view_agent_pack(request):
    print(request.session.get('is_editable'))
    context = {}
    agent_id = request.session.get('agentid')
    print("sssssssssssssssssssssssssssss")
    print(request.session.get('agentname'))
    request.session['is_editable'] = 1
    print("yes ")
    print(request.session.get('is_editable'))
    print("agent_id =")
    print(agent_id)
    mytrips = TripPlan.objects.filter(agency_id=agent_id)
    print(mytrips)
    
    for data in mytrips:
        if request.session.get('agentname') == data.agency_id:
           print("found")
           print(data.agency_id)
        else:
            print(data.agency_id)
    context['dataset'] = mytrips
    return render(request,'package.html',context) 

def edit_pack(request,id):
    if request.method == 'POST':
       request.session['is_trip_editable'] = 0
       tripplan = get_object_or_404(TripPlan,id=id)
       tripplan.trip_name = request.POST.get('name')
       tripplan.city = request.POST.get('city')
       tripplan.price = request.POST.get('price')
       tripplan.capacity = request.POST.get('capacity',None)
       tripplan.departure_date = request.POST.get('depa_date')
       tripplan.departure_time = request.POST.get('depa_time')
       tripplan.departure_place = request.POST.get('depa_place')
       tripplan.return_date = request.POST.get('return_date')
       tripplan.return_time = request.POST.get('return_time')
       tripplan.return_place = request.POST.get('return_place')
       tripplan.extra_info = request.POST.get('special',None)
       tripplan.thumbnail = request.FILES.get('thumbnail')

       request.session['trip_id'] = tripplan.id 

       date_format = "%Y-%m-%d"
       depa_date_obj = datetime.strptime(tripplan.departure_date, date_format)
       return_date_obj = datetime.strptime(tripplan.return_date,date_format)
       sub_date = (return_date_obj - depa_date_obj)
       a_duration = sub_date.days
       
       
       if tripplan.departure_date > tripplan.return_date or a_duration<=1:
           messages.error(request,'')
           messages.error(request,"check departure and return date again")
           return redirect(request.META.get('HTTP_REFERER','/'))
       tripplan.save()       
       return redirect('add_att')
    else:
        trip_plan_instance = TripPlan.objects.get(pk=id)
        request.session['is_trip_editable'] = 1
        print(request.session.get('is_trip_editable'))
        context = {}
        # tripoldvalue = TripPlan.objects.filter(id=trip_plan_instance)
        return render(request,'Trip_Plan_form.html',{'trip_plan_instance':trip_plan_instance})
    
def del_pack(request,id):
    TripPlan.objects.filter(id=id).delete()
    return redirect(request.META.get('HTTP_REFERER','/'))

def booking(request,id):
    request.session['trip_id'] = id
    trip_instance = TripPlan.objects.filter(id=id).first()
    print(request.session.get('trip_id'))
    user_id = request.session.get('userid')
    user_instance = User.objects.filter(id=user_id).first()
    ticket = Ticket.objects.create(trip_id=trip_instance,user_id=user_instance)
    request.session['ticket_id'] = ticket.id
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\     ")
    print(request.session.get('ticket_id'))
    return redirect('add_passenger')

def add_passenger(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        id = request.session.get('ticket_id')
        ticket_instance = Ticket.objects.filter(id=id).first()
        print("///////////////////")
        print(ticket_instance)
        passe = Passenger(ticket_id=ticket_instance, name=name, age=age)
        if 7 < int(age) < 100:
            passe.save()
        else:
            messages.error(request, "Age should be between 7 and 100")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        return redirect('add_passenger')
    else:
        id = request.session.get('ticket_id')
        passengers = Passenger.objects.filter(ticket_id=id)
        trip_id = request.session.get('trip_id')
        trip = TripPlan.objects.filter(pk=trip_id).first()
        total_price = trip.price * len(passengers)
        request.session['total_price'] = total_price
        print(request.session.get('total_price'))
        context = {
            'passengers': passengers,
            'other': {'trip': trip},
            'total_price': total_price,
        }

        return render(request, 'add_passengers.html', context)


def edit_passenger(request,id):
    if request.method == 'POST':
        psr = get_object_or_404(Passenger,id=id)
        psr.name = request.POST['name']
        psr.age = request.POST['age']
        ticket_instance = Ticket.objects.filter(id=request.session.get('ticket_id')).first()
        psr.ticket_id = ticket_instance
        print("///////////////////////")
        if int(psr.age) > 7 and int(psr.age) < 100 :
            psr.save()
        else:
            messages.error(request,"")
            messages.error(request,"age check again")
            return redirect(request.META.get('HTTP_REFERER','/'))
        
        print(psr)
        request.session['is_edit_passenger'] = 0
        return redirect('add_passenger')
    else:
        tempid = request.session.get('ticket_id')
        print("....................")
        print(".....................    ")
        print(id)
        request.session['is_edit_passenger'] = 1
        passengers = Passenger.objects.filter(ticket_id=tempid)
        context = {'passengers': passengers}
        passenger_instance = Passenger.objects.get(pk=id)
        context['other']={'instance':passenger_instance}
        print("asssssssssssssssssssssssssss")
        for passr in passengers:
           print(passr.name)
        return render(request,'add_passengers.html', context)


def del_passenger(request,id):
    Passenger.objects.filter(id=id).delete()
    print("deleted")
    return redirect(request.META.get('HTTP_REFERER','/'))

def payment(request):
    return render(request,'payment.html')


def pay(request):
        total = request.session.get('total_price')
        total_price = total*100
        amount = total_price
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_6dq9f5n25OyVzT', 'YWdWCxu9BKgiZ97OqqTYo5Dg'))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment['amount'])
        trip_id = request.session.get('trip_id')
        trip = TripPlan.objects.filter(id=trip_id).first()
        temp_id = request.session.get('tempid')
        passenger = Passenger.objects.filter(ticket_id=temp_id)
        print(passenger)
        for ps in passenger:
            print(ps.name)
        context = {'pack':trip,'passenger':passenger,'amount':amount,'total':total}
        return render(request, 'pay.html',context)

from django.views.decorators.csrf import csrf_exempt

csrf_exempt
def success(request):
    return render(request, "success.html")


def ticket_view(request):
    trip_id = request.session.get('trip_id')
    print(trip_id)
    trip = TripPlan.objects.filter(id=trip_id).first()
    temp_id = request.session.get('tempid')
    user_id = request.session.get('userid')
    print(user_id)
    user = User.objects.filter(id=user_id).first()
    print("....................")
    print(user)
    passenger = Passenger.objects.filter(ticket_id=temp_id)
    total = len(passenger)*trip.price
    today = date.today().strftime('%Y-%m-%d')
    agent = Agent.objects.filter(username=trip.agency_id).first()
    print(agent.email_id)
    context={'pack':trip,'passenger':passenger,'total':total,'today':today,'agent':agent}
    return render(request,'ticket.html',context)

def download(request):
    trip_id = request.session.get('trip_id')
    print(trip_id)
    trip = TripPlan.objects.filter(id=trip_id).first()
    temp_id = request.session.get('tempid')
    user_id = request.session.get('userid')
    print(user_id)
    user = User.objects.filter(id=user_id).first()
    print("....................")
    print(user)
    passenger = Passenger.objects.filter(ticket_id=temp_id)
    total = len(passenger)*trip.price
    today = date.today().strftime('%Y-%m-%d')
    agent = Agent.objects.filter(username=trip.agency_id).first()
    print(agent.email_id)
    context={'pack':trip,'passenger':passenger,'total':total,'today':today,'agent':agent}
    return render(request,'download.html',context)
