from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Setupuser,Buildkb
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm,Set_User_Form,Build_kbform
from django.views.generic.edit import FormView,UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.postgres.search import SearchVector,TrigramSimilarity


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def home(request):
    return render(request,"home.html")


@method_decorator(login_required, name='dispatch')
class Set_user(FormView):
    template_name="pkm_templates/set_up_user.html"
    form_class = Set_User_Form
    success_url = '/thanks/'

    def form_valid(self, form):
        nickname=self.request.user.username
        org = form.cleaned_data.get('your_organization')
        phone=self.request.user.phone_number
        cuemail_id=self.request.user.email
        if Setupuser.objects.filter(email_id=cuemail_id):
            messages.error(self.request,'setup completed already,Start build knowledge.')
            return redirect("/")
        Desig = form.cleaned_data.get("your_designation")
        job = form.cleaned_data.get("your_job_level")
        emails = form.cleaned_data.get("share_KB_with")
        instance = Setupuser.objects.create(your_nickname=nickname,your_phone_no=phone,your_organization=org, email_id=cuemail_id,your_designation=Desig,your_job_level=job)
        for user in emails:
            instance.share_KB_with.add(user)
            instance.save()
        messages.success(self.request,"Data saved succesfully")
        return redirect("/")

@method_decorator(login_required, name='dispatch')
class Set_user_update(UpdateView):
    model = Setupuser
    fields = ["your_designation","your_job_level"]#,"share_KB_with"]
    template_name = "pkm_templates/setup_user_update_form.html"
    success_url = "/"

@method_decorator(login_required, name='dispatch')
class Build_Kb(FormView):
    template_name = "pkm_templates/buildkb.html"
    form_class = Build_kbform
    success_url = '/thanks/'
    def get_form_kwargs(self):
        kwargs = super(Build_Kb, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def form_valid(self, form):
        cuemail_id=self.request.user.email
        knowledge_category=form.cleaned_data.get("knowledge_category")
        title=form.cleaned_data.get("title")
        knowledge=form.cleaned_data.get("knowledge")
        keywords=form.cleaned_data.get("keywords")
        document=self.request.FILES.getlist('document')
        share_with=form.cleaned_data.get("share_with")
        instance = Buildkb.objects.create(email=cuemail_id,knowledge_category=knowledge_category,
                                          title=title,knowledge=knowledge,keywords=keywords,document=document)
        for user in share_with:
            instance.share_with.add(user)
            instance.save()
        messages.success(self.request, "Knowledge saved succesfully")
        return redirect("/")

def terms(request):
    return render(request,"pkm_templates/terms & conditions.html")

def basetest(request):
    return render(request,"registration/basetest.html")

@login_required
def help(request):
    return render(request,"pkm_templates/help.html")

@login_required
def sharedknowledge(request):
    knowledge=Buildkb.objects.values("id","title","knowledge","email").filter(id__in=Buildkb.share_with.through.objects.values_list("buildkb_id").filter(user_id=request.user.id))
    return render(request, 'pkm_templates/sharedknowledge.html',
                  {'knowledges': knowledge})

@login_required
def search_form(request):
    return render(request, "pkm_templates/search_form.html")

@login_required
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        titles = Buildkb.objects.filter(title__icontains=q)
        #titles=Buildkb.objects.filter(title = TrigramSimilarity('title', q)).filter(title__gt=0.3).order_by('-title')
        return render(request, 'pkm_templates/search_form.html',
                      {'found': titles, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

@login_required
def detailknolwledge(request,id=None):
    detail=Buildkb.objects.values("knowledge_category","knowledge","title","email").filter(id=id)
    return render(request, 'pkm_templates/detail.html',{"detail":detail})

