L'application ne fonctionnera pas tant que vous n'aurez pas créé votre propre base firebase gratuite ici par exemple: "https://sailing-track-default-rtdb.firebaseio.com"
ainsi que la clef privée d'accès à cette base generée ici dans le fichier sailing-track-pkey.json
voir documentation firebase pour creation d'une database "RealTime Database"
https://www.youtube.com/watch?v=qKxisFLQRpQ
voir documentation pour la creation de clef privée permettant d'activer l'accès à la base avec la bibliothèque firebase_admin

Exemple 
# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/pi/sailtrack/sailing-track-pkey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {'databaseURL': "https://sailing-track-default-rtdb.firebaseio.com"})
