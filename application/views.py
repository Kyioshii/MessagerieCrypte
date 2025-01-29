from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.decorators import login_required
from .Cryptage import AESManager
import base64

@login_required
def user_list(request):
    query = request.GET.get("q")
    users = User.objects.exclude(id=request.user.id)

    # Manao recherche
    if query:
        users = users.filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))

    return render(request, "application/main.html", {"users": users})


@login_required
def chat(request, user_id):
    # maka anle mpandefa message sy andefasana azy
    other_user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(
        (Q(emetteur=request.user, recepteur=other_user) |
         Q(emetteur=other_user, recepteur=request.user))
    )

    decrypted_message = None
    decrypted_message_id = None

    if request.method == "POST":
        # mijery anle bouton cliquenle utilisateur
        action = request.POST.get("action")
        manager = AESManager()

        if action == "send_message":
            # raha mandefa message de alaina le message
            content = request.POST.get("content")

            # raha tsy vide
            if content:
                # atao base64 le cle sy message crypté
                key = base64.b64encode(manager.get_key()).decode("utf-8")
                content_crypted = base64.b64encode(manager.encrypt_message(content)).decode("utf-8")

                # Atsofoka anaty base de donnée
                Message.objects.create(
                    emetteur=request.user,
                    recepteur=other_user,
                    contenu="MESSAGE CRYPTE",
                    contenuCrypte=content_crypted,
                    cle=key,
                )

        # raha decrypte ndray ny bouton nokitiany
        elif action == "decrypt_message":
            # alaina le cle sy contenu decrypte
            encrypted_content = request.POST.get("decrypte")
            decryption_key = request.POST.get("key")

            # raha tsy vide le texte
            if encrypted_content and decryption_key:
                try:
                    # decodena averina binaire aloha le cle sy message crypté
                    encrypted_bytes = base64.b64decode(encrypted_content)
                    decryption_key_bytes = base64.b64decode(decryption_key)

                    # decryptena amzay
                    decrypted_message = manager.decrypt_message(encrypted_bytes, decryption_key_bytes)

                    # Tadiavina ilay message mitovy amin'iny
                    decrypted_message_id = Message.objects.filter(
                        contenuCrypte=encrypted_content
                    ).values_list('id', flat=True).first()

                except Exception as e:
                    decrypted_message = f"Erreur lors du déchiffrement: {str(e)}"


    return render(request, 'application/chat.html', {
        'other_user': other_user,
        'messages': messages,
        'decrypted_message': decrypted_message,
        'decrypted_message_id': decrypted_message_id,
    })



