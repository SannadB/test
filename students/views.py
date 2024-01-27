import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Member, Product, Category, Review, Item, Rating
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

def add_review(request):
    data = json.loads(request.body)
    review = Review()
    review.product_id = data.get('product_id')
    review.rating = 10
    review.comment = data.get('comment')
    review.save()

     # Send email
    subject = 'New Review Submitted'
    message = f'A new review has been submitted for product {review.product_id}.'
    from_email = 'sannad98@gmail.com'  # Update with your email
    recipient_list = ['sannad98@gmail.com']  # Update with the recipient's email

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    return JsonResponse({
        'success': True,
        'message': 'Review submitted successfully.'
        })

def ratings(request):
    data = json.loads(request.body)
    rating = Rating()
    rating.item_id = data.get('item_id')
    rating.rating = data.get('review')
    rating.save()

    return JsonResponse({
        'success': True,
        'message': 'Rating submitted successfully.'
        })

def students(request):
    data = Member.objects.all().values()
    return render(request, "index.html", {"data": data})

def students_json(request):
    # Using JsonResponse to directly convert a queryset to JSON
    data = list(Member.objects.all().values())
    return JsonResponse(data, safe=False)

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('firstname') + ' ' + request.POST.get('lastname')
        
        # Access the uploaded image file
        image_file = request.FILES.get('image')
        
        # Save to database
        member = Member()
        member.firstname = request.POST.get('firstname')
        member.lastname = request.POST.get('lastname')

        if image_file:
            # Handle the image file here, you can save it to the filesystem or process it as needed
            # For example, saving to the filesystem:
            member.profile_image = image_file
            member.save()
            
            return HttpResponse(f'Successfully saved {name} with image.')
        else:
            # Handle the case where no image file is provided
            return HttpResponse(f'Error: No image provided for {name}.')
    else:
        # Handle other request methods (GET, etc.) or redirect to an error page
        return HttpResponse('Invalid request method.')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_page.html', {'product': product})

def categories(request):
    return HttpResponse('Categories page')

def items(request):
    items = Item.objects.all().values()
    return render(request, 'items.html', {'items': items})

def get_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item_page.html', {'item': item})

def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    send_mail(
        'New Contact Form Submission',
        f'A new contact form submission has been received from {name} ({email}). Message: {message}',
        'sannad98@gmail.com',['sannad98@gmail.com', 'mehreen.imran2701@gmail.com', 'saba.noman5@gmail.com'], fail_silently=False)
    return HttpResponse('Email sent successfully')

def contact_form(request):
    return render(request, 'contact.html')