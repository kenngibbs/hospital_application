from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Contact, Hospital
from .forms import ContactForm


def index(request):
    """ GET: Renders the index file. It has the log in form
        TODO POST: Authenticate the user's credentials and render the home page on the index """
    if request.POST == "POST":
        print("Logged In")
    return render(request, "startHealthApp/index.html")


def new_contact(request):
    """ GET: Render the information for a new contact
        POST:
            1) Creates a new django auth User
            2) Creates and saves the one to one relationship to the User
            3) Adds the many to many relationship of hospitals to the contact """
    if request.method == "POST":
        # FIXME Breaks when you use an existing username. Add validation.
        new_django_auth_user = User.objects.create_user(
            username=request.POST["contact_username"],
            email="",
            password=request.POST["contact_password"])

        new_contact_instance = Contact(
            contact_djangoUser=new_django_auth_user,
            contact_name=request.POST["contact_name"],
            contact_address=request.POST["contact_address"],
            contact_phone=request.POST["contact_phone"],
            contact_jobTitle=request.POST["contact_jobTitle"],
        )
        new_contact_instance.save()

        contact_hospital_select_queryset = Hospital.objects.filter(pk__in=request.POST.getlist("contact_hospitalGroup"))
        new_contact_instance.contact_hospitalGroup.set(contact_hospital_select_queryset)

    return render(request, "startHealthApp/new_contact.html", {"form": ContactForm()})
