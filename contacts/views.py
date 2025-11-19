from django.shortcuts import render

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']

        print(title, message)

    return render(request, 'contacts/contact.html')