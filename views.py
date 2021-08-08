from django.shortcuts import render, redirect
from .models import Member

# Create your views here.
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class MemberCreateView(CreateView):
    model = Member
    fields = ['firstname','lastname']

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['firstname','lastname']

class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('index')

class MemberListView(ListView):
    model = Member
    context_object_name = 'members'

# def index(request):
#     members = Member.objects.all()
#     context = {'members': members}
#     return render(request, 'crud/index.html', context)

# def create(request):
#     member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
#     member.save()
#     return redirect('/')

# def edit(request, id):
#     members = Member.objects.get(id=id)
#     context = {'members': members}
#     return render(request, 'crud/edit.html', context)

# def update(request, id):
#     member = Member.objects.get(id=id)
#     member.firstname = request.POST['firstname']
#     member.lastname = request.POST['lastname']
#     member.save()
#     return redirect('/crud/')

# def delete(request, id):
#     member = Member.objects.get(id=id)
#     member.delete()
#     return redirect('/crud/')