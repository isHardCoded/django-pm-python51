from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def send_message(request):
    success = False
    error = False

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if name and email and message:
            subject = f"Сообщение с сайта"
            full_message = f"От: {name} <{email}>\n\n{message}"

            if send_mail(subject, full_message, email, ['iotsutstvuet@yandex.ru'], fail_silently=False):
                success = True
            else:
                error = True
        else:
            error = True

    return render(request, 'contacts/contact.html', {
        'success': success,
        'error': error,
    })