from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge = {
     "january": "for at least 20 minitues every day!",
     "february": "Walk for at least 20 minitues every day! ",
     "march": "Learn Django for at least 20 minitues every day!",
     "april": "for at least 20 minitues every day!",
     "may": "Walk for at least 20 minitues every day! ",
     "june": "Learn Django for at least 20 minitues every day!",
     "july": "for at least 20 minitues every day!",
     "august": "Walk for at least 20 minitues every day! ",
     "september": "Learn Django for at least 20 minitues every day!",
     "october": "for at least 20 minitues every day!",
     "november": "Walk for at least 20 minitues every day! ",
     "december": None
}
# Create your views here.

def index(request):
     months = list(monthly_challenge.keys())
    
     return render(request, "challenges/index.html", {
          "months": months

     })

def monthly_challenges_by_number(request, month):
       months = list(monthly_challenge.keys())

       if month > len(months):
            return HttpResponseNotFound ("invalid month")
       redirect_month = months[month - 1]
       redirect_path = reverse("month_challenge", args=[redirect_path])
       return HttpResponseRedirect("/challenge/" + redirect_month)


def monthly_challenges(request , month):
    try:
         challenge_text =monthly_challenge[month]
         return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()

         })
    except:
       raise Http404()
