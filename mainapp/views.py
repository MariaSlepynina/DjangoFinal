from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from .models import  *
from .forms import *
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import *
from django.contrib.auth.forms import *



def Client_new(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Client'))
        else:
            form = MakerForm()
        template = loader.get_template('Client_form.html')
        context = {
            'form': form,
            'title': 'new client'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden()

def Client_edit(request, kp):
    if request.user.is_authenticated:
        try:
            client = Client.objects.get(id=kp)
        except Client.DoesNotExist:
            raise Http404("error")
        if request.method == 'POST':
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Client'))
        else:
            form = ClientForm(instance=client)
        template = loader.get_template('Client_form.html')
        context = {
            'form': form,
            'title': 'edit Client'
        }
        return HttpResponse(template.render(context, request))
    else:
        return  HttpResponseForbidden()

def Client_delete(request, kp):
    if request.user.is_authenticated:
        try:
            client = Client.objects.get(id=kp)
        except Client.DoesNotExist:
            raise Http404("error")
        m = f"client{client.name} was deleted"
        client.delete()
        return HttpResponseRedirect(reverse('Client'))
    else:
        return HttpResponseForbidden()


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))





def Client(request):
    template = loader.get_template('Client.html')
    context = {
        'Client': Client.objects.all(),
        'title': "Clients",
        'p_user': request.user.groups.filter(name='test').exists
    }
    return HttpResponse(template.render(context, request))
def Tarif(request):
    template = loader.get_template('Tarif.html')
    context = {
        'tarifs': Tarif.objects.all(),
        'title': "Tarif",
    }
    return HttpResponse(template.render(context, request))

def oneTarif(request, dk):
    try:
        tarif = Tarif.objects.get(id=dk)
    except Tarif.DoesNotExist:
        raise Http404("error")
    template = loader.get_template('oneTarif.html')

    context = {
        'tarif': tarif,
        'title': "one tarif",
    }
    return HttpResponse(template.render(context, request))

def Operator(request):
    songs = Operator.objects.all()
    context = {
        'operators': Operator.objects.all(),
        'title': 'Operators',
    }
    return render(request, 'Operator.html', context)
    
    
def Sity(request):
    songs = Sity.objects.all()
    context = {
        'Sity': Sity.objects.all(),
        'title': 'Sity',
    }
    return render(request, 'Sity.html', context)

def Sity_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SityForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Tarif'))
        else:
            form = SityForm()
        template = loader.get_template('Sity_form.html')
        context = {
            'form': form,
            'title': 'new sity'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden

def Sity_edit(request, kp):
    if request.user.is_authenticated:
        try:
            Sitys = Sity.objects.get(id=kp)
        except Tarif.DoesNotExist:
            raise Http404("error")
        if request.method == 'POST':
            form = SityForm(request.POST, instance=tarifs)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Sity'))
        else:
            form = SityForm(instance=sitys)
        template = loader.get_template('Sity_form.html')
        context = {
            'form': form,
            'title': 'edit Sitys'
        }
        return HttpResponse(template.render(context, request))
    else:
        return  HttpResponseForbidden

def Sity_delete(request, kp):
    if request.user.is_authenticated:
        try:
            sitys = Sity.objects.get(id=kp)
        except Sity.DoesNotExist:
            raise Http404("error")
        m = f"Sity{sitys.name} was deleted"
        sitys.delete()
        return HttpResponseRedirect(reverse('Sity'))
    else:
        return HttpResponseForbidden


def Tarif_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TarifForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Tarif'))
        else:
            form = TarifForm()
        template = loader.get_template('Tarif_form.html')
        context = {
            'form': form,
            'title': 'new tarif'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden

def Tarif_edit(request, kp):
    if request.user.is_authenticated:
        try:
            tarifs = Tarif.objects.get(id=kp)
        except Tarif.DoesNotExist:
            raise Http404("error")
        if request.method == 'POST':
            form = TarifForm(request.POST, instance=tarifs)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Tarif'))
        else:
            form = TarifForm(instance=tarifs)
        template = loader.get_template('Tarif_form.html')
        context = {
            'form': form,
            'title': 'edit Tarifs'
        }
        return HttpResponse(template.render(context, request))
    else:
        return  HttpResponseForbidden

def Tarif_delete(request, kp):
    if request.user.is_authenticated:
        try:
            tarifs = Tarif.objects.get(id=kp)
        except Tarif.DoesNotExist:
            raise Http404("error")
        m = f"Tarif{tarifs.name} was deleted"
        tarifs.delete()
        return HttpResponseRedirect(reverse('Tarif'))
    else:
        return HttpResponseForbidden

def Operator_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OperatorForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Operator'))

        else:
            form = OperatorForm()
        template = loader.get_template('Operator_form.html')
        context = {
            'form': form,
            'title': 'new Operator'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden()

def Operator_edit(request, kp):
    if request.user.is_authenticated:
        try:
            operator = Operator.objects.get(id=kp)
        except Operator.DoesNotExist:
            raise Http404("error")
        if request.method == 'POST':
            form = OperatorForm(request.POST, instance=operator)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Operator'))

        else:
            form = OperatorForm(instance=operator)
        template = loader.get_template('Song_form.html')
        context = {
            'form': form,
            'title': 'edit Operator'
        }
        return HttpResponse(template.render(context, request))
    else:
        return  HttpResponseForbidden

def Operator_delete(request, kp):
    if request.user.is_authenticated:
        try:
            operator = Operator.objects.get(id=kp)
        except Operator.DoesNotExist:
            raise Http404("error")
        m = f"Operator {operator.name} was deleted"
        operator.delete()
        return HttpResponseRedirect(reverse('Operator'))
    else:
        return HttpResponseForbidden

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    template = loader.get_template('user_form.html')
    context = {
        'form': form,
        'title': 'Create User'
    }
    return HttpResponse(template.render(context, request))


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=username,password=userpass)
            if user is not  None:
                login(request,user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AuthenticationForm()
    template = loader.get_template('user_form.html')
    context = {
        'form': form,
        'title': 'Create User'
    }
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return HttpResponseRedirect(reverse('index'))

