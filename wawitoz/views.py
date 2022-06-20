from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from wawitoz.models import FutureJobsApplicant

branding = [
    'Color Psychology',
    ' Font Styling ',
    'Brand Strategy',
    'Target Audience Research',
    'Tagline ',
    ' Name Assistant',
    ' Logo Design ',
    ' Website Design',
    '  Packaging '
]
printing = ['Letterheads',
            'Business cards',
            'Envelopes',
            ' Brochures',
            'Fliers',
            'Journal',
            'Posters',
            'Banners',
            'Catalogues',
            ' Calendars',
            'Booklets',
            'Dairies',
            'Forms',
            'Newsletters',
            'Magazines']
supply_office = ['Printing papers'
    , 'Flash disks'
    , 'Files'
    , 'Photocopying papers'
    , 'Writing, Legal Pads'
    , 'Short hand notebooks'
    , 'Envelopes'
    , 'Packing & masking tape'
    , 'Folders'
    , 'Highlighters'
    , 'Glue',
                 'Labels'
    , 'Pins',
                 'Colors',
                 'File holders',
                 'Wall clocks'
    , 'Letter trays', 'Markers', 'Paper Punches',
                 'Pens', 'Post it notes', 'Rubber Band', 'Tacks Push pin']
edu_suppy = ['Printing paper',
             'Photocopying papers'
    , ' Pencils'
    , 'Pens'
    , ' Erasers'
    , 'Office Glue'
    , 'Chalk'
    , 'Counter Books'
    , 'Files'
    , 'Notebooks'
    , 'Crayons'
    , 'Geometric sets'
    , 'Colour Pencils'
    , ' Rulers'
    , 'Sharpeners']
IT = ['Cloud services', ' Backup solutions', 'Network security',
      'Email services', 'Software as a service', 'Software development',
      'Troubleshooting and technical support', 'Hardware installations and maintenance',
      'Website development', 'App development']
electronics = ['Desktops', 'Laptops', 'Keyboards', 'Camera',
               'Sound systems', 'CPU', 'Flash drive', 'Memory cards', 'RAM', 'ROM',
               'Smart television', 'Smart phones', 'Tablets', 'Printers', 'Switches',
               'Monitors', 'Disk space', 'Cables'
               ]


# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def back_home(request):
    return redirect('home')


def career(request):
    return render(request, 'career.html')


def jobs(request):
    return render(request, 'jobs.html')


def apply_btn(response):
    return render(response, 'career.html')


def more(request):
    return render(request, 'services.html', {"printing": printing, "office": supply_office, "school": edu_suppy})


def more_i(request):
    return render(request, 'services.html', {"IT": IT, 'electronics': electronics})


def more_b(request):
    return render(request, 'services.html', {"branding": branding})


def apply(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        cv = request.POST['cv']
        gender = request.POST['gender']
        position = request.POST['position']
        if first == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        if last == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        if email == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        if phone == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        if age == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        if cv == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        elif gender == '':
            messages.error(request, 'Fill Blanks')
            return render(request, 'career.html')
        else:
            future_app = FutureJobsApplicant.objects.create(firstname=first, lastname=last, email=email, phone=phone
                                                            , age=age, position=position, cv=cv, gender=gender)
            from_mail = settings.EMAIL_HOST_USER
            send_mail(
                'Career Lookup',
                f'Dear {first} We received your details and we will notify you whenever there is a job opening',
                from_mail,
                [email, ],
                fail_silently=False,
            )
            messages.error(request, 'success')
            return redirect('home')
    else:
        messages.error(request, 'method is denied')
        return render(request, 'career.html')


def apply_job(response):
    if response.method == 'POST':
        first = response.POST['first']
        last = response.POST['last']
        email = response.POST['email']
        phone = response.POST['phone']
        age = response.POST['age']
        cv = response.POST['cv']
        gender = response.POST['gender']
        position = response.POST['position']
        if first == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        if last == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        if email == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        if phone == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        if age == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        if cv == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        elif gender == '':
            messages.error(response, 'Fill Blanks')
            return render(response, 'career.html')
        else:
            future_app = FutureJobsApplicant.objects.create(firstname=first, lastname=last, email=email, phone=phone
                                                            , age=age, position=position, cv=cv, gender=gender)
            from_mail = settings.EMAIL_HOST_USER
            send_mail(
                'Subject here',
                'Here is the message.',
                from_mail,
                [email, ],
                fail_silently=False,
            )
            messages.error(response, 'SUCCESS')
            return redirect('home')
    else:
        messages.error(response, 'method is denied')
        return render(response, 'career.html')
