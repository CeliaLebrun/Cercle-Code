Le code permet de décrire un cercle avec 50 points situés sur ce cercle.

On se place sur le plan XY. L’utilisateur définit le rayon du cercle en entrée et les coordonnées des points du cercle sont la sortie.
Ici le centre du cercle est (–r,0,0), de sorte que le premier point soit (0.0.0). On tourne ensuite dans le sens direct.
On peut vérifier que les points sont sur le cercle avec l’équation du cercle : (x-a)^2+(y-b)^2=r^2. Avec a et b le centre du cercle, ici a=-r et b=0.
On insert un intervalle régulier de valeur en divisant 2*pi par 50 de sorte à avoir 50 points équidistant. On crée une variable i qu’on incrémente de 1 à chaque boucle pour décaler nos x et y qui parcourent le cercle. Le i permet aussi de stopper la boucle.
