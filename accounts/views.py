from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    # raha efa nampiditra ny anarany sy mdp ilay utilisateur
    if request.method == "POST":
        # alaina le anarana sy mot de passe avy amin POST
        username = request.POST["username"]
        password = request.POST["password"]
        # jerena hoe misy ao amin'ny base de donnée ve ilay information nampidiriny
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # omena fahafahana miditra ao amin'ny compteny amzay ny utilisateur
            login(request, user)

            return redirect("application:user_list")

        # raha tsy misy de mamoaka message d'erreur
        else:
            messages.info(request,"Identifiant ou mot de passe incorrect")

    # raha mbola tsy nampiditra n'inon'inona kosa izy de omena formulaire vide
    form = AuthenticationForm()
    return render(request,"login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect("accounts:login")

def register_user(request):
    # raha efa voafeno ny anarana sy ny mot de passe
    if request.method == "POST":
        # andramana ireo information nomeny
        form = UserCreationForm(request.POST)

        # raha manaraka ny norme rehetra
        if form.is_valid():
            # tehirizina de alefa mankany amin'ny page de login
            form.save()
            return redirect("application:user_list")
    # omena formulaire d'inscription vide kosa raha mbola tsy nameno
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
