from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
    emetteur = models.ForeignKey(User, related_name='message_envoye', on_delete=models.CASCADE)
    recepteur = models.ForeignKey(User, related_name='message_recu', on_delete=models.CASCADE)
    contenu = models.TextField(default="")
    dateEnvoi = models.DateTimeField(auto_now_add=True)
    contenuCrypte = models.TextField(default="")
    cle = models.TextField(default="")

    def __str__(self):
        return self.contenu

    class Meta:
        ordering = ['dateEnvoi']