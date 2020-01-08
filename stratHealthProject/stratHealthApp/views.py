from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Contact, Hospital, Staff, Procedures
from .forms import ContactForm

# TODO: End Phase: When adding a procedure, confirm the selected hospital has the selected corresponding staff


def index(request):
    """ GET: If the user is authenticated, send them to the home page. If not, render the log in page.
        POST: Authenticate the user's credentials and redirect to the index page to render the home page. """
    if request.user.is_authenticated and not request.user.is_superuser:
        logged_in_contact_instance = Contact.objects.get(contact_django_user=request.user)
        hospital_list = logged_in_contact_instance.contact_hospital_list.all()

        # Staff Average, highest paid staff, highest procedure cost, and average procedure cost
        total_salary_for_each_hospital = 0

        hospital_info_list = {}  # Used for the dictionary
        # hospital_info_list = []  # Used for the list (array)

        # Iterate through the list of all hospitals associated with the logged in contact
        for eachHospital in hospital_list:
            highest_paid_staff_instance = 0

            # Get a list of all staff associated with the hospital
            staff_of_each_hospital = Staff.objects.filter(staff_hospital_list = eachHospital)
            # Initializing the highest paid staff with the first employee
            if len(staff_of_each_hospital) > 0:
                highest_paid_staff_instance = staff_of_each_hospital[0]

            # Get the total salary and check for the highest paid employee of the staff
            for eachStaff in staff_of_each_hospital:
                total_salary_for_each_hospital += eachStaff.staff_salary
                if highest_paid_staff_instance.staff_salary < eachStaff.staff_salary:
                    highest_paid_staff_instance = eachStaff
            print(eachHospital.hospital_name)
            # Get the procedures for each hospital
            total_procedure_cost = 0
            highest_cost_procedure = 0
            procedures_of_each_hospital = Procedures.objects.filter(procedure_hospital=eachHospital)

            if len(procedures_of_each_hospital) > 0:
                highest_cost_procedure = procedures_of_each_hospital[0].procedure_cost
            for eachProcedure in procedures_of_each_hospital:
                print(eachProcedure.procedure_name)
                total_procedure_cost += eachProcedure.procedure_cost
                if highest_cost_procedure < eachProcedure.procedure_cost:
                    highest_cost_procedure = eachProcedure.procedure_cost

            if len(staff_of_each_hospital) > 0:
                salary_average = total_salary_for_each_hospital/len(staff_of_each_hospital)
            else:
                salary_average = 0
            if len(procedures_of_each_hospital) > 0:
                avg_procedure_cost = total_salary_for_each_hospital/len(staff_of_each_hospital)
            else:
                avg_procedure_cost = 0

            print(highest_cost_procedure)
            print(avg_procedure_cost)

            # Dictionary of all hospitals with their information provided.
            hospital_info_list[eachHospital.hospital_name] = {
                "hospital_address": eachHospital.hospital_address,
                "salary_average": salary_average,
                "highest_paid_staff": highest_paid_staff_instance,
                "avg_procedure_cost": avg_procedure_cost,
                "highest_cost_procedure": highest_cost_procedure,
                "number_of_procedures": len(procedures_of_each_hospital),
            }

            # A list(array) of hospital objects with it's necessary information. Same information as above.
            # Couldn't decided on which one to use.

            # hospital_info_list.append({
            #     "name": eachHospital.hospital_name,
            #     "salary_average": total_salary_for_each_hospital/len(staff_of_each_hospital),
            #     "highest_paid_staff": highest_paid_staff_instance
            # })
            total_salary_for_each_hospital = 0

        # TODO: Calculate the highest procedure cost and average procedure cost per hospital

        context = {
            "contact_name": logged_in_contact_instance.contact_name,
            "hospital_info": hospital_info_list
        }

        return render(request, "stratHealthApp/home.html", context)

    context = {
        "form": ContactForm()
    }

    if request.method == "POST":

        is_user_authenicated = authenticate(username=request.POST["django_username"], password=request.POST["django_password"])
        if is_user_authenicated is None:
            context["error"] = "The username or password you entered is incorrect."
        else:
            login(request, is_user_authenicated)
            return redirect("index")

    return render(request, "stratHealthApp/index.html", context)


def new_contact(request):
    """ GET: Render the information for a new contact.
            POST:
                1) Creates a new django auth User.
                2) Creates and saves the one to one relationship to the User.
                3) Adds the many to many relationship of hospitals to the contact. """
    context = {
        "form": ContactForm()
    }

    if request.method == "POST":
        # Checks to see if the username already exists. If so, adds an error message to page.
        if User.objects.filter(username=request.POST["django_username"]).exists():
            context["error"] = "Please choose a different username"
        else:
            # Create a new instance of the built-in Django User for authentication
            new_django_auth_user = User.objects.create_user(
                username=request.POST["django_username"],
                email="",
                password=request.POST["django_password"])

            # Include the additional information using a one-to-one relationship to the User model.
            new_contact_instance = Contact(
                contact_django_user=new_django_auth_user,
                contact_name=request.POST["contact_name"],
                contact_address=request.POST["contact_address"],
                contact_phone=request.POST["contact_phone"],
                contact_position=request.POST["contact_position"],
            )

            # Have to save the new instance in order to add the many to many relationship to it.
            new_contact_instance.save()

            contact_hospital_queryset = Hospital.objects.filter(pk__in=request.POST.getlist("contact_hospital_list"))
            new_contact_instance.contact_hospital_list.set(contact_hospital_queryset)

            login(request, new_django_auth_user)
            return redirect("index")

    return render(request, "stratHealthApp/new_contact.html", context)


def log_user_out(request):
    """ Log out the currently logged in user. """
    logout(request)
    return redirect("index")
