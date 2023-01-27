from django.shortcuts import render, redirect
from todoproject.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # instanciation avec données
        if form.is_valid():
            return redirect('/thanks/')
    else:
        form = ContactForm()  # instanciation sans données
    # Affichage du formulaire via un template
    return render(request, 'contact.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')