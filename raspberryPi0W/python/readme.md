L'application ne fonctionnera pas tant que vous n'aurez pas créé votre propre base firebase gratuite 
voir documentation firebase pour creation d'une database "RealTime Database"
https://www.youtube.com/watch?v=qKxisFLQRpQ

ainsi que la clef privée d'accès à cette base 
voir documentation pour la creation de clef privée permettant d'activer l'accès à la base avec la bibliothèque firebase_admin
https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/

https://firebase.google.com/docs/database/admin/start?hl=fr

https://medium.com/theleanprogrammer/connecting-firebase-6102ef4eca08


dans le code sailtrack.py les valeurs xxxxx des 2 lignes suivantes doivent donc être changées par vos propres valeurs.

cred = credentials.Certificate('xxxx')

firebase_admin.initialize_app(cred, {'databaseURL':"xxxx"})

Le but est que vous ayez votre propre base firebase que vous pourez gérer pour votre propre application de tracking


