from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Options, Vote


# Create your views here.
def index(requste):
    votes = Vote.objects.all()
    return render(requste, 'polls_index.html', {"votes": votes})


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
