from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import PremiumUser
import stripe

@login_required
def checkout(request):

    try:
        if request.user.premiumuser:
            return redirect('base')
    except PremiumUser.DoesNotExist:
        pass

    if request.method == 'POST':
        stripe_customer = stripe.PremiumUser.create(
            email=request.user.email, source=request.POST['stripeToken'])
