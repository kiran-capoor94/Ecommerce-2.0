from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from billing.models import BillingProfile

from .forms import AddressForm
from .models import Address

def checkout_address_create_view(request):
    # FBV to add addresses.
    form = AddressForm(request.POST or None) #Importing AddressForm form.
    context = {
        "form": form,
    }# adding form context to be called and rendered by the HTML Form.

    """Using "next" we can safely route our URLs
        main use is to create a URL and then pass through
        Django Framework to say its safe to go to the
        respective URL.
    """
    next_ = request.GET.get('next')
    next_post= request.POST.get('next')
    redirect_path = next_ or next_post or None
    """ Using the inbuilt .is_valid() function for forms
        we can let django validate the authenticity of the forms.
    """
    if form.is_valid():
        # print(request.POST)
        instance = form.save(commit=False)#creating an object of the Model Form(Address Form) to call objects relevant to the view.
        
        """Importing Billing Profile from its respective model to validate
            the billing_profile and save the addresses to the respective
            Billing Profile.
        """
        billing_profile, billing_profile_created= BillingProfile.objects.new_or_get(request)

        if billing_profile is not None:
            address_type = request.POST.get("address_type","shipping")
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")
        else:
            print("Error")
            return redirect("carts:checkout")

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('carts:checkout')
    return redirect('carts:checkout')

def address_list_view(request):
    return render(request, 'addresses/list.html',{})

def checkout_address_reuse_view(request):
    context = {}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if request.method == "POST":
        print(request.POST)
        shipping_address = request.POST.get('shipping_address', None)
        address_type = request.POST.get('address_type', 'shipping')
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if shipping_address is not None:
            qs = Address.objects.filter(billing_profile=billing_profile, id=shipping_address)
            if qs.exists():
                request.session[address_type + "_address_id"] = shipping_address
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
    return redirect("cart:checkout")