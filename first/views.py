from django.shortcuts import render, redirect, get_object_or_404
from .models import Hobby
from .forms import HobbyForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

@login_required
def home(request):
    form = HobbyForm()

    if request.method == "POST":
        form = HobbyForm(request.POST)
        if form.is_valid():
            hobby = form.save(commit=False)
            hobby.user = request.user  # Assign logged-in user
            hobby.save()
            messages.success(request, "Hobby added successfully!")
            return redirect("home")

    hobbies = Hobby.objects.filter(user=request.user)  # Show only user’s hobbies
    return render(request, "first/home.html", {"form": form, "hobbies": hobbies})

@login_required
def delete_hobby(request, hobby_id):
    hobby = get_object_or_404(Hobby, id=hobby_id, user=request.user)  # Only delete user’s own hobbies
    hobby.delete()
    messages.success(request, "Hobby deleted successfully!")
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = UserCreationForm()
    
    return render(request, "first/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "first/profile.html", {"form": form})

def about(request):
    return render(request, "first/about.html")


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Hobby  # Import Hobby model
# from .forms import HobbyForm
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# from django.shortcuts import redirect

# # from django.views.decorators.csrf import csrf_exempt


# def add_hobby(request):
#     if request.method == 'POST':
#         form = HobbyForm(request.POST)
#         if form.is_valid():
#             hobby = form.save(commit=False)  # Don't save yet
#             hobby.user = request.user  # Assign logged-in user
#             hobby.save()
#             return redirect('home')  # Redirect to home page after submission
#     else:
#         form = HobbyForm()
#     return render(request, 'home.html', {'form': form})


# @login_required # type: ignore
# def home(request):
#     message = ""  # Initialize message
#     form = HobbyForm()  # Initialize form


#     if request.method == "POST":
#         form = HobbyForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             hobby = form.cleaned_data.get("hobby")

#             # ✅ Check if the same name-hobby pair already exists
#             if Hobby.objects.filter(name=name, hobby=hobby).exists():
#                 message = f"{name}, you have already recorded {hobby} as your hobby!"
#             else:
#                 form.save()
#                 return redirect("/")  # Redirect to prevent duplicate form submission

#     # ✅ Fetch all stored hobbies
#     hobbies = Hobby.objects.all()

#     return render(request, "first/home.html", {"form": form, "message": message, "hobbies": hobbies})

# def about(request):
#     return render(request, "first/about.html")

# @login_required
# def delete_hobby(request, hobby_id):
#     hobby = get_object_or_404(Hobby, id=hobby_id) # type: ignore
#     hobby.delete()
#     messages.success(request, "Hobby deleted successfully!")  # Success message  # type: ignore
#     return redirect('home')   # Redirect back to the home page

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user
#             messages.success(request, "Your account has been created! You can now log in.")
#             return redirect("login")  # Redirect to login page
#         else:
#             messages.error(request, "Registration failed. Please check the form.")
#     else:
#         form = UserCreationForm()

#     return render(request, "first/register.html", {"form": form})  # ✅ Always returns a response

# from django.urls import path
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),  # Redirect to login after logout
# ]

# from django.contrib import messages

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST) # type: ignore
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password) # type: ignore
#             if user is not None:
#                 login(request, user) # type: ignore
#                 messages.success(request, f"Welcome back, {username}!")  # Success message
#                 return redirect("home")
#         messages.error(request, "Invalid username or password. Please try again.")  # Error message
#     else:
#         form = AuthenticationForm() # type: ignore
#     return render(request, "first/login.html", {"form": form})


#  # Temporarily disable CSRF (not recommended for production)
# def logout_view(request):
#     if request.method == "POST":  # Only allow POST requests
#         logout(request)
#         messages.info(request, "You have been logged out.")
#         return redirect("login")  # Redirect to login page after logout
#     else:
#         return redirect("home")  # Redirect to home if accessed incorrectly

# @login_required
# def profile_view(request):
#     if request.method == "POST":
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully!")
#             return redirect("profile")  # Redirect to profile page
#     else:
#         form = UserChangeForm(instance=request.user)

#     return render(request, "first/profile.html", {"form": form})






#     # from django.http import HttpResponse # type: ignore

# # def home(request):
# #     return HttpResponse("Hello, Mayur! 🤡")





# # from django.shortcuts import render

# # def home(request):
# #     return render(request, "first/home.html")  # Render the template





# # from django.shortcuts import render

# # def home(request):
# #     context = { # Create a dictionary to pass data to the template
# #         'name':'Mayur Shingrakhiya', # A string variable
# #         'age':20, # A number variable
# #         'hobbies': ['Coding','Gaming','Reading'] # A list variable
# #  }
# #     return render(request, "first/home.html", context)

# # def about(request):
# #     return render(request, "first/about.html") # Rendering about.html
# # # Create your views here.




# # from django.shortcuts import render, redirect
# # from.forms import HobbyForm
# # from .models import Hobby  # Import the Hobby model

# # def home(request):
# #     message = ""  # To store success message

# #     if request.method == "POST":
# #         print("Form submitted!")
# #         form = HobbyForm(request.POST)  # Get submitted data
# #         if form.is_valid():  # Validate form
# #             # form.save()
# #             Hobby.objects.create(
# #                 name=form.cleaned_data["name"],
# #                 hobby=form.cleaned_data["hobby"]
# #             )
          
# #             # return redirect("/")   # Redirect to clear the form after submission
# #             # name = form.cleaned_data["name"]
# #             # hobby = form.cleaned_data["hobby"]
# #             # Hobby.objects.create(name=name, hobby=hobby)
# #             # message = f"Thank you, {name}! Your hobby ({hobby}) has been recorded."
# #             message = "Thank you! Your hobby has been recorded."
# #     else:
# #         form = HobbyForm()  # Show blank form

# #      # Retrieve all hobbies from the database
# #     hobbies = Hobby.objects.all()

# #     return render(request, "first/home.html", {"form": form, "message": message, "hobbies": Hobby.objects.all()})










