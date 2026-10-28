from django.shortcuts import render
import re

def login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if not re.fullmatch(r"[A-Za-z]{3,15}", username):
            message = "Invalid username! Use 3-15 letters."

        elif not re.fullmatch(r"(?=.*[A-Za-z])(?=.*[0-9])[A-Za-z0-9]{6,12}", password):
            message = "Invalid password! Use 6-12 letters and digits."

        else:
            message = "Login Successful!"

    return render(request, "login.html", {"message": message})