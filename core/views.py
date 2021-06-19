from django.http import request
from django.shortcuts import redirect, render
from datetime import date, datetime
import calendar
from .models import MeetLink, Profile
from .task import sleepy, show_live_meeting
from .forms import RegisterUserForm, UpdateMeeting
from django.contrib import messages
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

@unauthenticated_user
def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            gender = form.cleaned_data.get('gender')
            profile = Profile.objects.get(user = form_save)
            profile.gender = gender
            profile.save()
            return redirect('login')
        else:
            messages.error(request, 'Something going wrong! Fill again to get registered.')
            return redirect('register')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    total_meets = MeetLink.objects.filter(user=request.user)
    day = calendar.day_name[date.today().weekday()]
    meetings = MeetLink.objects.filter(user=request.user, day=day)
    live_meet = show_live_meeting(request.user)
    todays_date = date.today()
    current_time = datetime.now().strftime('%H:%M:%S')
    meetings_width = 0
    live_meetings_width = 0
    if(total_meets.count() != 0):
        meetings_width = (meetings.count()/total_meets.count())*100
        live_meetings_width = (len(live_meet)/total_meets.count())*100

    
    context = {
        'meetings': meetings,
        'live_meet': live_meet,
        'live_meet_count': len(live_meet),
        'total_meets_today': meetings.count(),
        'total_meets_count': total_meets.count(),
        'total_meets': total_meets,
        'live_meets': live_meet,
        'day': day,
        'date': todays_date,
        'time': current_time,
        'meetings_width': meetings_width,
        'live_meetings_width': live_meetings_width
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
def create_meet(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        meet_link = request.POST.get('meet_link')
        start_time = request.POST.get('start_time')+':00'
        end_time = request.POST.get('end_time')+':00'
        day = request.POST.get('day')
        MeetLink.objects.create(
            user=request.user,
            course_name=course_name,
            meet_link=meet_link,
            start_time=start_time,
            end_time=end_time,
            day=day
        )
        return redirect('index')
    context = {}
    return render(request, 'create_meet.html', context)

@login_required(login_url='login')
def delete_meet(request, pk):
    meet_to_delete = MeetLink.objects.get(pk=pk)
    if request.method == 'POST':
        meet_to_delete.delete()
        return redirect('index')
    context = {}
    return render(request, 'delete_meet.html', context)

@login_required(login_url='login')
def update_meet(request,pk):
    get_meet = MeetLink.objects.get(pk=pk)
    form = UpdateMeeting(instance=get_meet)
    if request.method == 'POST':
        form = UpdateMeeting(request.POST, instance=get_meet)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.warning(request, 'Fill the form properly')
            return redirect('update_meet', pk=get_meet.pk)
    context = {
        'meet': get_meet,
        'form': form
    }
    return render(request, 'update_meet.html', context)