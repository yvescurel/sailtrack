# SailTrack
projet de tracking au large en voilier

Avec l'avènement de Starlink et donc l'utilisation d'internet haut débit au large (où que l'on soit en mer dans le monde), en voilier on peut dès maintenant utiliser un tracker GPS couplé au réseau internet de notre voilier. 

Ce tracker GPS permet de partager nos trajets de voyage en temps réel sur internet avec des personnes qui nous suivent. Idéal pour un long voyage en toute sécurité et par exemple pour le suivi sur internet par nos amis lors d'une transatlantique.

Exemple de suivi avec cette application de tracking SailTrack équipant un voilier ayant fait une transatlantique:

https://sailing-track.web.app/carte.html?user=leden&id=caraibe24


Technologie utilisée
RaspBerry PI 0 + GPS 5v (type BN220 utilisant des trames NMEA0183) relié au Raspberry + Micro écran tactile avec stylet et clavier virtuel nous permettant de saisir les paramètres personnalisant notre tracking.

Pourquoi un raspberry pi 0? Ses avantages : tout petit, prix dérisoire, nombreux ports de communication pouvant dialoguer avec les instruments de bord et ouvert sur connexion internet.

Côté Raspberry PI OW langage utilisé python permettant de communiquer avec le GPS et une base Google Firebase "RealTime Database" sur internet où sont stockées nos positions GPS qui alimentent une application Web classique (Html + Javascript)

Voir les fonctionnalités :
https://sailing-track.web.app/

Pré requis pour faire fonctionner cette application de tracking: 
Achat d'un raspberryPI O W (30€ sur Amazon) et d'un GPS BN 220 (25€ sur Amazon)

Si on est informaticien ou motivé pour apprendre Firebase et utiliser l'application SailTrack sur son RaspBerry PI O W : installer et configurer sa propre database et web application Firebase puis utiliser les sources fournies ici.

Si on veut simplement utiliser l'application de tracking sur son RaspBerry PI OW:  utiliser une image du système et de l'application de tracking fournie par le concepteur de cette application copiable sur carte SD de 32 Go du RaspBerry PI O W.

Une image de la carte SD utilisable sur un Raspberry PI0W permet d'utiliser directement l'application SailTrack sur une base de données "RealTime Database" et l'application web Firebase existante sans aucune installation et configuration de Firebase. Cette image de l'application sailTrack sur RaspBerry est disponible en contactant le concepteur et developpeur de cette application : yves.curel@gmail.com





