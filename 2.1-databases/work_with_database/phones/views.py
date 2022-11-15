from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()
    phone = [{'name': p.name, 'price': p.price, 'slug': p.slug, 'image': p.image} for p in phone_objects]
    context = {'phones': phone}
    template = 'catalog.html'
    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.filter(slug=slug)
    phones = [{'name': p.name, 'price': p.price, 'slug': p.slug,
               'image': p.image, 'release_date': p.release_date,
               'lte_exists': p.lte_exists} for p in phone_objects]
    phone = phones[0]
    context = {'phone': phone}
    template = 'product.html'
    return render(request, template, context)
