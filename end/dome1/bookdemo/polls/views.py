from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView as DV, DeleteView
from django.contrib.auth import login as lin, logout as lon, authenticate
from .forms import *


# Create your views here.
def index(requste):
    votes = Vote.objects.all()
    return render(requste, 'polls_index.html', {"votes": votes})


class IndexView(ListView):
    template_name = 'polls/polls_index.html'
    context_object_name = 'votes'
    queryset = Vote.objects.all()


class DetailView(View):
    def get(self, resquste, voteid):

        if resquste.user and resquste.user.username != "":
            try:
                vote = Vote.objects.get(id=voteid)

                if vote in resquste.user.votes.all():

                    url = reverse("polls:polls_result", args=(voteid,))
                    print(vote, "++_")
                    return redirect(to=url)
                else:
                    try:
                        options = vote.options_set.all()
                        return render(resquste, 'polls/polls_detail.html', {"vote": vote, "options": options})
                    except:
                        return HttpResponse("问题不合法")
            except Exception as e:
                print(e)
                return HttpResponse("++")
        else:
            url = reverse("polls:login") + "?next=/polls/detail/" + voteid + "/"
            return redirect(to=url)

    def post(self, requste, voteid):
        try:
            vote = Vote.objects.get(id=voteid)
            requste.user.votes.add(vote)
            option_id = requste.POST.get("poll")
            option = Options.objects.get(id=option_id)
            option.opt_poll += 1
            option.save()
            url = reverse("polls:polls_result", args=(voteid,))

            return redirect(to=url)
        except:
            return HttpResponse("选项不合法")


class ResultView(View):
    def get(self, resquste, voteid):
        try:
            vote = Vote.objects.get(id=voteid)
            options = vote.options_set.all()
            return render(resquste, 'polls/polls_result.html', {"vote": vote, "options": options})

        except:
            return HttpResponse("问题不合法")


def detail(requste, voteid):
    vote = Vote.objects.get(id=voteid)
    options = vote.options_set.all()
    if requste.method == "GET":
        return render(requste, 'polls_detail.html', {"vote": vote, 'options': options})
    elif requste.method == "POST":
        option_id = requste.POST.get("poll")
        option = Options.objects.get(id=option_id)
        option.opt_poll += 1
        option.save()
        url = reverse("polls:polls_index")
        return redirect(to=url)


def add_option(requste, voteid):
    vote = Vote.objects.get(id=voteid)
    if requste.method == "GET":
        return render(requste, 'polls_add_option.html', {"vote": vote})
    elif requste.method == "POST":
        option = Options()
        option.opt_title = requste.POST.get("title")
        option.opt_vote = vote
        option.save()
        url = reverse("polls:polls_detail", args=(voteid,))
        return redirect(to=url)


def login(requste):
    if requste.method == "GET":
        lf = LoginForm()
        return render(requste, 'polls/login.html', {"lf": lf})
        # return render(requste, 'polls/login.html')
    elif requste.method == "POST":
        lf = LoginForm(requste.POST)
        if lf.is_valid():
            username = lf.cleaned_data.get("username")
            password = lf.cleaned_data.get("password")
            # username = requste.POST.get("username")
            # password = requste.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                lin(requste, user)
                if requste.GET.get("next"):
                    url = requste.GET.get("next")
                else:
                    url = reverse("polls:polls_index")
                return redirect(to=url)
            else:
                return render(requste, 'polls/login.html', {"lf": lf, "errors": "用户名密码不匹配"})
        else:
            return HttpResponse("未知错误")


def logout(requste):
    lon(requste)
    url = reverse("polls:polls_index")
    return redirect(to=url)


def regist(requste):
    if requste.method == "GET":
        rf = RegistForm()
        return render(requste, 'polls/regist.html', {"rf": rf})
    elif requste.method == "POST":
        rf = RegistForm(requste.POST)
        if rf.is_valid():
            username = rf.cleaned_data.get("username")
            password1 = rf.cleaned_data.get("password")
            password2 = rf.cleaned_data.get("password2")

            # username = requste.POST.get("username")
            # password1 = requste.POST.get("password1")
            # password2 = requste.POST.get("password2")
            if User.objects.filter(username=username).count() > 0:
                return render(requste, 'polls/regist.html', {"errors": "用户名已存在"})
            else:
                if password1 == password2:
                    User.objects.create_user(username=username, password=password1)
                    url = reverse("polls:login")
                    return redirect(to=url)
                else:
                    return render(requste, 'polls/regist.html', {"rf": rf, "errors": "两次密码不一致"})
        else:
            return HttpResponse("未知错误")


def add_vote(requste):
    if requste.method == "GET":
        return render(requste, 'polls_add_vote.html')
    elif requste.method == "POST":
        vote = Vote()
        vote.title = requste.POST.get("title")
        vote.save()
        url = reverse("polls:polls_index")
        return redirect(to=url)


def delete_option(request, option_id):
    option = Options.objects.get(id=option_id)
    vote_id = option.opt_vote.id
    option.delete()
    url = reverse("polls:polls_detail", args=(vote_id,))
    return redirect(to=url)


def delete_vote(request, vote_id):
    vote = Vote.objects.get(id=vote_id)
    vote.delete()
    url = reverse("polls:polls_index")
    return redirect(to=url)
