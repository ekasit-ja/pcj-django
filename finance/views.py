from django.shortcuts import render, redirect

from .models import Finance

# Create your views here.
def finance_view(request):

    if len(request.GET) < 1:
        finance = Finance.objects.all().first()

        return render(request, 'finance/finance_view.html', {
            'finance': finance,
        })
    else:
        return redirect(finance_view)
