# LittleFather
LittleFather est un outil modulable d'osint automatisé. Il vient de la même base que le projet [LittleBrother](https://github.com/lulz3xploit/LittleBrother) de Ownes1s (voir le [discord](https://discord.gg/uFtSud) dédié).

Sa principale force est son coté modulaire. Autrement dit, il suffit d'écrire un module ou une commande et de l'ajouter dans le dossier correspondant pour pouvoir l'exploiter.

### Modules annexes
Les modules nécessaires ansi que leurs versions respectives sont dans le fichier requirements.txt, et dont voici la liste:
- selenium
- terminaltables
- urllib3

Il faut également installer [geckodriver](https://github.com/mozilla/geckodriver/releases) à la racine du projet pour le bon fonctionnement de selenium. Il est important (sinon ça ne fonctionne pas) de le renommer `geckodriver` SANS extension.
