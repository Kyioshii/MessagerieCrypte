Cette projet necessite l'installation de Django et pycryptodome
Installation de pycryptodome:
Ouvrir terminale et taper la commande (nécessite l'installation de python) :
     pip install pycryptodome

Installation de DJANGO:
Ouvrir terminale et taper la commande (nécessite l'installation de python) :
     pip install Django


Vous devez créer un dossier nommé "messagerieCrypte" et mettre ces fichiers dans ce dossier.
Des explications sont fournis dans le code par des commentaires.

Le pycryptodome est une bibliothèque de cryptographie pour chiffrer des textes, images, fichiers, images. Elle est légèrement rapide et légère.
AES-256 est l'un des algorithmes de chiffrement symétriques les plus sûrs, largement adopté pour des applications sensibles tels que les messages privés.Une clé 256 bits offre un
nombre extrêmement élevé de combinaison possibles, Soit 2^256, ce qui est pratiquement incassable.

DJANGO est un framework Web qui utilise le langage Python pour concevoir des applications webs complexes rapidement efficacement en utilisant l'architecture MVT (Model - Template - View).

Pour exécuter le projet: 
      Ouvrir terminal:
          Entrer dans dossier messagerieCrypte à l'aide du commande
                cd messagerieCrypte
          Lancer la commande (pour effectuer la migration de la base de donnée)
                python manage.py makemigrations
                python manage.py migrate
          Pour lancer le server, taper dans le terminal la ligne de commande:
                python manage.py runserver
          Copier le lien localhost dans votre navigateur ou Ctrl + Click sur le lien
          Creer deux onglets pour créer deux comptes différents et s'envoyer des messages Chiffrés
