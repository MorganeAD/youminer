youminer
========
youminer est un outils conçu dans le cadre d'un projet de *Big Data et
Médias Sociaux* et d'*Architecture des Application Multimédias* pour
[Polytech' Marseille][polytech]. Cet outil est un service web permettant
de visionner des vidéos [YouTube][youtube] diffusées depuis le service
youminer. Il offre aussi la possibilité de commenter les vidéos et de
répondre des un quizz lorsqu'un certain nombres de vidéos ont été vues. Ce
fichier aborde l'installation et l'utilisation de youminer.


Prérequis
---------
Cet outil est conçu pour fonctionner sur [GNU/Linux][gnulinux] et à priori
tous les système \*nix. youminer utilise le framework [Django][django]. Il
est donc nécéssaire d'avoir [Python 3.6][python] installé sur le server.
Ce guide ne courve l'installation que pour [Arch Linux][archlinux].

Vous aurez aussi besoin d'une clé développeur YouTube pour permettre à
youminer de communiquer avec l'API de YouTube. Vous devrez inserer cette
clé dans un fichier plus tard dans ce guide.


Installation
------------
Commencez d'abord par récuperer youminer :

    $ git clone https://github.com/Niouby/youminer.git
    $ cd youminer

Avant toute chose, entrez votre clé développeur dans le fichier
`youminer/apikey.sh`. Le fichier doit ressembler à ceci :

    $ cat youminer/apikey.sh
    APIKEY=<your_youtube_api_key>

L'installation de youminer commence par la mise en place d'un
environnement virtuel Python et l'installation de Django et des outils
nécéssaires au bon fonctionnement de youminer. Installez d'abord le module
d'environnement virtuel pour Python ainsi que les outils pour MongoDB:

    $ sudo pacman -Syu
    $ sudo pacman -S python python-virtualenv mongodb mongodb-tools

Activez le service MongoDB puis importez la base de données du quizz :

    $ sudo systemctl start mongodb.service
    $ mongoimport -d quizz -c quizz --jsonArray <questions.json

Mettez ensuite en place l'environnement virtuel - vérifiez bien que vous
êtes dans le répertoire de youminer.

    $ python -mvenv myvenv

Placer des l'environnement virtuel créé puis installer Django et le module
[MongoDB][mongodb] pour Python.

    $ source myvenv/bin/activate
    $ pip install django~=1.11.0
    $ pip install mongoengine

Pour finir, il ne reste qu'a effectuer une migration de la base de données
puis à lancer le serveur.

    $ python manage.py migrate
    $ python manage.py runserver

Essayez ensuite d'acceder à cette URL http://127.0.0.1:8000/registration/
depuis un navigateur internet. Vous devrez arriver sur la page
d'inscription de youminer. Si oui, félicitation, youminer est désormais
prêt à l'emploi.

Utilisation
-----------
Commencer par vous créer un utilisateur. Vous pourrez ensuite consulter
les videos et le quizz. Il y a 3 catégories de videos disponibles :

- 3D ; 
- big data ;
- réalité virtuelle.

Pour accéder à chacune des ces catégories, utilisez ces adresses :

- http://127.0.0.1:8000/videos/big%20data/
- http://127.0.0.1:8000/videos/3D/
- http://127.0.0.1:8000/videos/realite%20virtuelle/

Pour démarrer le quizz, utilisez cette adresse :

- http://127.0.0.1:8000/videos/questions/

> Il est nécéssaire d'avoir regardé un certain nombre de videos pour
débloquer toutes les questions du quizz.

[archlinux]: https://www.archlinux.org/
[django]: https://www.djangoproject.com/
[gnulinux]: https://www.gnu.org/
[mongodb]: https://www.mongodb.com/
[polytech]: https://polytech.univ-amu.fr/
[python]: https://www.python.org/
[youtube]: https://youtube.com

