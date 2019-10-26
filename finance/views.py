from django.shortcuts import render

from .models import Finance

# Create your views here.
def finance_view(request):
    finance = Finance.objects.all().first()

    return render(request, 'finance/finance_view.html', {
        'finance': finance,
    })
