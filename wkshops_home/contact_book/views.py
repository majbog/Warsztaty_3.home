from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

from contact_book.models import Person, Phone, Mail, Address, ContactGroup
from contact_book.forms import AddPhoneForm, AddMailForm


class NewContactView(CreateView):
    model = Person
    fields = ("first_name", "last_name", "description")
    success_url = reverse_lazy('index')


class ShowAllContactsView(View):
    def get(self, request):
        contacts = Person.objects.all()
        ctx = {
            "contacts": contacts
        }
        return render(request, "all_contacts.html", ctx)


class ContactDetailsView(View):
    def get(self, request, contact_id):
        contact = Person.objects.get(id=contact_id)
        contact_phones = Phone.objects.filter(contact_person=contact.id)
        contact_mails = Mail.objects.filter(contact_person=contact.id)
        ctx={
            'contact': contact,
            'contact_phones': contact_phones,
            'contact_mails': contact_mails
        }
        return render(request, 'contact_details.html', ctx)


class AllGroupsView(View):
    def get(self, request):
        groups = ContactGroup.objects.all()
        ctx = {
            'groups': groups
        }
        return render(request, "all_groups.html", ctx)


class AddPhoneView(View):
    def get(self, request, contact_id):
        form = AddPhoneForm(initial={
                "contact_person": contact_id
            })
        ctx ={
            "form": form
        }
        return render(request, 'add_phone_form.html', ctx)
    def post(self, request, contact_id):
        form = AddPhoneForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            type = form.cleaned_data["type"]
            phone = Phone.objects.create(number=number, type=type, contact_person = Person.objects.get(id=contact_id))
            return redirect("contact/{}" .format(contact_id))


class AddMailView(View):
    def get(self, request, contact_id):
        form = AddMailForm(initial={
                "contact_person": contact_id
            })
        ctx ={
            "form": form
        }
        return render(request, 'add_mail_form.html', ctx)
    def post(self, request, contact_id):
        form = AddMailForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            type = form.cleaned_data["type"]
            mail = Mail.objects.create(mail_address=address, type=type, contact_person = Person.objects.get(id=contact_id))
            return redirect("/contact/{}" .format(contact_id))

        ctx={
            "form": form
        }
        return render(request, 'add_mail_form.html', ctx)


