from django.views.generic import FormView
from django.views.generic import ListView,DetailView
from . forms import CandidateForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . models import Question
import os
from django.core.mail.message import EmailMessage
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile


class IndexView(ListView):
    template_name = 'candidate/index.html'
    context_object_name = 'ques_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(ListView):
    template_name = 'candidate/detail.html'
    context_object_name = 'ques_list'
    paginate_by = 1

    def get_queryset(self):
        return Question.objects.all()


class CompileView(DetailView):
    model=Question
    template_name = 'candidate/compile.html'

    def post(self, request,num):
        language=request.POST.get("language")

        def ext(x):
            return {"C": ".c",
             "Python": ".py",
             "Java": ".java",
             }[x]
        code_filename="code"+str(num)+ext(language)
        code_file_path = os.path.join(settings.FILES_DIR, code_filename)
        output_filename="output"+str(num)+".txt"
        output_file_path = os.path.join(settings.FILES_DIR, output_filename)

        f= open(code_file_path,"w+")
        lang="# language = "+language+"\n"
        p=request.POST.get("codearea")
        f.write(p)
        f.close()

        if language== "Java" :
            os.system("javac %s" % (code_file_path))
            os.system("java %s > %s 2> %s" % (code_file_path[ :-5], output_file_path, output_file_path))

        elif language == "C":
            os.system("gcc %s" % (code_file_path))
            os.system("./a.out > %s 2> %s" % (output_file_path,output_file_path))

        elif language == "Python":
            os.system("python %s > %s 2> %s" % (code_file_path, output_file_path, output_file_path))

        f = open(output_file_path, "r")
        return HttpResponse(f.read())


def rand(self):

    candidate = self.user.first_name
    html_message="""Hey HR,\n\t This email contains the answer sheets of %s .Please take this for further evaluation, and publish the result as soos as possible.\nCandidate name : %s\nCategory : Fresher """%(candidate,candidate)

    email = EmailMessage()
    file_path=os.path.join(settings.FILE_DIR, 'media')
    email.subject = "Programming Test-Answer Sheet"
    email.body = html_message
    email.from_email = "Programming Test-Answer Sheet! <bensha.sayone@gmail.com>"
    email.to = ["bensha.sayone@gmail.com" ]
    list = os.listdir(file_path)

    for file in list :
        path="media/" + file
        attach_file_path = os.path.join(settings.FILE_DIR, path)
        email.attach_file(attach_file_path)
    email.send()
    os.system("rm -r media")
    return HttpResponseRedirect('/')



def signup(request):
    logout(request)
    os.system("mkdir media")
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CandidateForm()
    return render(request, 'candidate/signup.html', {'form': form})


