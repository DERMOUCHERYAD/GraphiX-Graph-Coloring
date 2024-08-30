# GraphiX
GraphiX est une application de coloration de graphes qui permet de visualiser et de résoudre le problème de coloration de graphes en utilisant la logique propositionnelle .

Vous avez déjà téléchargé le fichier ProjetColorationINF402.zip et vous l'avez extrait sur votre machine, vous pouvez maintenant ouvrir ce projet dans PyCharm ou Visuel Studio 

## Installation de l'environnement:
1. Assurez-vous d'avoir Python 3 installé sur votre système.
 Si ce n'est pas le cas, vous pouvez le télécharger :

# Windows : 
 * 64 bits: https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
 * 32 bits: https://www.python.org/ftp/python/3.12.3/python-3.12.3.exe

Suivre les étapes de l'installeur. S'assurer que l'option "Ajouter à la variable d'environnement PATH" est bien coché
###### Notez que Python 3.12.3 ne peut pas être utilisé sur Windows 7 ou version antérieure

# Linux: 
Sur la plupart des distributions Linux, Python est généralement déjà préinstallé.
Dans un terminal:
sudo apt install python3
vous pouvez consulter cette page pour l'utilisation de Python sur les plateformes Unix: https://docs.python.org/fr/3/using/unix.html

# MacOS: 
 https://www.python.org/downloads/release/python-3123/

## Utilisation:
2. Il est possible d'utiliser le code de ce projet de deux façons.
# Utilisation non-interactive
Dans un terminal:
    se mettre dans le chemin correct:./ProjetColorationINF402/ProjetColorationINF402/
    # Pour Linux:
    python3 interface.py

    # Pour Windows/MacOS
    python interface.py

# Utilisation d'un IDE
Vous pouvez travailler avec un IDE pour rendre plus facile la prise en main et production de code. Vous pouvez choisir votre IDE préféré.
Par exemple: 
  # Pycharm
 -Windows : https://www.jetbrains.com/fr-fr/pycharm/download/?section=windows
 -Linux : https://www.jetbrains.com/fr-fr/pycharm/download/?section=linux
 -MacOS:https://www.jetbrains.com/fr-fr/pycharm/download/?section=macos

  # Visuel Studio Code :
  -Windows: https://code.visualstudio.com/docs/?dv=win64user
  -Linux: https://code.visualstudio.com/docs/?dv=linux64_deb
  -MacOs: https://code.visualstudio.com/docs/setup/mac

  # Configuration
  Pour faire la liaison entre PyCharm et Python merci de regarder cette vidéo 
:https://www.youtube.com/watch?v=lMRKY3wjcrE en Francais
:https://www.youtube.com/watch?v=sLcLE0zJWuA en Anglais

# Exécution et Compilation :
1-Lancez PyCharm.
Dans l'écran de bienvenue, sélectionnez "Open" (Ouvrir).
Naviguez jusqu'à l'emplacement où vous avez extrait le fichier .zip de votre projet 
Sélectionnez le dossier racine du projet "ProjetColorationINF402" et cliquez sur "OK".

2-Une fois votre projet ouvert, PyCharm  proposera d'installer les dépendances nécessaires. Suivez les instructions pour les  installer.

3-Ensuite, accédez à "File" (Fichier) > "Settings" (Paramètres) > "Project: [ProjetColorationINF402]" > "Python Interpreter" (Interpréteur Python), et chercher 
les bibliothèque tkinter,draw,PIL,math,pysat, python-sat ,matplotlib,networkx  et installer les 
Si votre interpréteur Python n'est pas déjà configuré, cliquez sur l'icône d'engrenage et sélectionnez "Add" (Ajouter) pour ajouter un nouvel interpréteur Python.
Choisissez l'interpréteur Python que vous avez téléchargé et installé précédemment sur votre machine.

Sur Vs code : 
ouvrer le terminal pour installer les bibliothèques utilisées:
pip install tkinter
pip intall math
pip install matplotlib
pip install networkx 
pip install pysat 

Choisir Open puis OpenFile puis selectionner le dossier ProjetColorationINF402 .
pour le SATsolver on a utiliser Glucose3 de pysat.solvers

4-Ouvrez le fichier interface.py dans l'explorateur de fichiers de PyCharm/Vscode
5-Cliquez avec le bouton droit sur le fichier 'interface.py' et sélectionnez "Run" (Exécuter) ou utilisez le boutton au haut à droite associé pour lancer l'application.

# Utilisation de Graphix : 
1-cliquer sur start pour demarrer le jeux
2-Vous pouvez créer votre propre graph et choisir le nombre de couleurs que vous voulez ou de choisir un graphe parmi 8 choix et le nombre de couleurs que vous souhaiter utiliser.
3- Vous pouvez toujours revenir en arrière ou quitter complétement l'application.


