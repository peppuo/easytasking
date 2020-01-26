from django.shortcuts import redirect, render
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
        stripe_customer = stripe.Customer.create(
            email=request.user.email, source=request.POST['stripeToken'])
        subscription = stripe.Subscription.create(
            premiumuser=stripe_customer.id)

        premiumuser = PremiumUser()
        premiumuser.user = request.user
        premiumuser.stripe_id = stripe_customer.id
        premiumuser.stripe_subscription_id = subscription.index
        premiumuser.save()

        return redirect('base')
    else:
        price = 1000
        og_euro = 10
        final_euro = 10
        return render(
            request,
            'subscription/checkout.html',
            {'price': price, 'og_euro': og_euro, 'final_euro': final_euro},
        )
