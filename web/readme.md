Le fichier de configuration key.js est ici volontairement non fourni, il contient les variables d'initialisation de l'application avec la structure suivante:
var firebaseConfig = {
    apiKey: "xxxx",
    authDomain: "xxxx",
    databaseURL: "xxxx",
    projectId: "xxxx",
    storageBucket: "xxxx",
    messagingSenderId: "xxxx",
    appId: "xxxx",
    measurementId: "xxxx"
};

Cette variable firebaseConfig est ensuite appelée à l'initialisation de chaque page: carte.html, journal.html, modif.html, supp.html
vous devez donc creer un fichier key.js avec la structure definie ci dessus et les xxxx rempacées par vos propres variables.

C'est a vous de creer vos propres clefs liées à votre application web ainsi que votre database Firebase (utilisée aussi par le programme d'alimentation en Python)
Le but est que vous ayez votre propre base firebase et application web que vous pourez gérer SOUS VOTRE PROPRE RESPONSABILITE pour votre propre application de tracking.

Tuto Firebase web application : https://www.youtube.com/watch?v=pP7quzFmWBY

A noter qu'ici via cette application web on stocke aussi des images accompagnant le trajet et donc on utilise Firebase Storage. (Au moment de l'upload vers Firebase Storage, ces images sont reduites systematiquement à une dimension de 800px afin de ne pas trop surcharger Firebase Storage).

Tuto Firebase Storage:  https://www.youtube.com/watch?v=-IFRVMEhZDc

Une image de la carte SD utilisable sur un Raspberry PI0W permet d'utiliser directement l'application SailTrack sur une base de données "RealTime Database" et l'application web Firebase existante sans aucune installation et configuration de Firebase. Cette image de l'application sailTrack sur RaspBerry est disponible en contactant le concepteur et developpeur de cette application : yves.curel@gmail.com






