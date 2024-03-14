# Si vous utilisez ces sources Github

L'application ne fonctionnera pas tant que vous n'aurez pas créé votre propre base firebase gratuite 
voir documentation firebase pour creation d'une database "RealTime Database"
https://www.youtube.com/watch?v=qKxisFLQRpQ

ainsi que la clef privée d'accès à cette base 
voir documentation pour la creation de clef privée permettant d'activer l'accès à la base avec la bibliothèque python firebase_admin
https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/

https://firebase.google.com/docs/database/admin/start?hl=fr

https://medium.com/theleanprogrammer/connecting-firebase-6102ef4eca08


dans le code sailtrack.py les valeurs xxxxx des 2 lignes suivantes doivent donc être changées par vos propres valeurs.

cred = credentials.Certificate('xxxx')

firebase_admin.initialize_app(cred, {'databaseURL':"xxxx"})

Vous devez aussi installer les bibliothéques suivantes:
serial, pynmea2, datetime, calendar, time, sys, os, datetime, firebase_admin

Le but est que vous ayez votre propre base firebase que vous pourez gérer SOUS VOTRE PROPRE RESPONSABILITE pour votre propre application de tracking

# Si vous n'utilisez pas ces sources Github

Une image de la carte SD utilisable sur un Raspberry PI permet d'utiliser directement l'application SailTrack sur une base de données "RealTime Database" Firebase existante sans aucune installation et configuration de Firebase. Cette image de l'application sailTrack sur RaspBerry est disponible en contactant le concepteur et developpeur de cette application : yves.curel@gmail.com
Indiquez dans votre email quel raspberry vous utilisez ainsi que le nom de votre voilier et le nom de votre projet de navigation.
Pré requis indispensable vous devez avoir installé le GPS BN 220 sur votre Raspberry:  3 connections: +5v du GPS vers +5v du raspBerry, - du GPS vers - du RaspBerry , TX du GPS vers RX du RaspBerry.
