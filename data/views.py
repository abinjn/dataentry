from multiprocessing import context
from unicodedata import name
from urllib import request
from django.forms import NullBooleanField
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, SearchForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile
from django.db.models import Q

# Create your views here.

@login_required 
def dataEntry(request):
    data_id = request.GET.get('data_id')
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if data_id != None:
            temp = Profile.objects.get(id=data_id)
            temp.name = request.POST.get('name')
            temp.grade = request.POST.get('grade')
            temp.save()
            messages.success(request, 'Data successfully updated---------------')
            return redirect('data-search')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'Data successfully Added')
            form.save()
            return redirect('data-entry')

    elif data_id != None:
        data_id = request.GET.get('data_id')

        data = Profile.objects.filter(id=data_id)
        #data = data.get() 
        #return redirect('data-entry')
        
        data = {
            'name':data.first().name, 
            'grade':data.first().grade,
            'school':data.first().school,
            'email':data.first().email,
            'parent_name':data.first().parent_name,
            'contact_number':data.first().contact_number,
            'alternate_contact_number':data.first().alternate_contact_number,
            'enquiry_source':data.first().enquiry_source,
            'enquiry_date':data.first().enquiry_date,
            'remark':data.first().remark,
            }
        
        form = ProfileUpdateForm(initial=data)
    else:
        form = ProfileUpdateForm()
    context = {'form': form, 'title': 'Data Entry'}
    return render(request, 'data/form_.html', context)


@login_required
def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        print(search_query)
        Data = Profile.objects.filter(Q(name__contains=search_query) |
        Q(grade__contains=search_query) |
        Q(school__contains=search_query) |
        Q(email__contains=search_query) 
        )
    else:
        Data = Profile.objects.all()
    context = {'Data': Data, 'title' : 'Search'}
    return render(request, 'data/table.html', context)

    
