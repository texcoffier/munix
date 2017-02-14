.. -*- mode: rst; mode: iimage -*-

.. role:: rawhtml(raw)
   :format: html

:rawhtml:`<link rel="stylesheet" href="munix.css" type="text/css">`

======================================
MUNIX : MOOC UNIX
======================================

Proposition pour Unix :
 * au S2, pas le S1, le choc serait trop rude.
 * 3 crédits.
 * Horaire libre. Etalé sur tout le semestre.
 * Un seul cours de présentation.
 * Pas de TD en présentiel.
 * L'apprentissage est fait via un cours/TD/TP intégré avec QUENLIG.
 * Autant de séances de TP que les étudiants veulent. Présence non obligatoire.
   Les étudiants s'autoévaluent.
 * Pas de note de contrôle continue, un examen final et une deuxième session.

=============================================================================
                                      PROGRAMME
=============================================================================

Décomposé en 6 parties.

Certaines parties ont moins de connaissances théoriques mais
nécessitent plus de pratique.

-------------------------
1 : Le système de fichier
-------------------------

Intro : Pourquoi ce cours. Histoire. Comment accéder à unix et au shell.

Concepts : hiérarchie, répertoire, fichier, chemin, répertoire courant

Commandes :

   * Navigation : cd, pwd, ls

   * Fichier : cp, rm, mv, ln, mkdir

   * Transformation : wc, sort, gzip, gunzip, iconv?, convert?, avconv?
   
   * Affichage : cat, less, tail, zcat, diff

   * Pratique : date, man, du, df, tar

Notion d'option de commande (et de paramètre d'option ?)

Edition de l'historique avec les touches curseurs.
   
Et la complétion de commande.


----------------------------------
2 : Variables, patterns et boucles
----------------------------------

Builtin : echo

Les variables. HOME, PATH, PS1, remplacement $(...)

L'échappement : guillemet, cote, backslash

Les patterns.

L'enchainement de commandes avec ';' et '&&'

La boucle 'for'


----------------------------------------
3 : Redirections, expressions régulières
----------------------------------------

Les redirections dans les fichiers (pas le pipe). /dev/null

Les expressions régulières.

Les commandes : grep, sed, (awk???)

Expressions régulières dans vi, emacs, en Javascript, Python, C ?

La boucle 'while'. 'read' et 'test'


---------------------------
4 : Scripts et processus
---------------------------

Concepts : Processus et pipeline
commandes : kill, killall, ps, pstree, top, free

Groupement de commandes avec ( )

Lancements de batch : &, ^Z, bg, nohup

Editeur de texte : donner les liens vers les tutoriaux. En imposer un ?

Script : argument, commentaire, exit, $?, export

Le 'if'

Commandes : find, xarg, ulimit


---------------------------
5 : Système et réseaux
---------------------------

+-------------------------------------+-----------------------------+
|Concepts                             |Commandes                    |
+=====================================+=============================+
|Utilisateur, groupe, droits          |chown, chgrp, chmod          |
+-------------------------------------+-----------------------------+
|Périphérique, disque, TTY, liaison   |mount, sshfs, récupérer      |
|série, clavier, souris, écran        |les fichiers perdus          |
+-------------------------------------+-----------------------------+
|Client, serveur, nom machine, adresse|ssh, scp, rsync, wget,       |
|IP, clefs privés/publiques           |sendmail                     |
+-------------------------------------+-----------------------------+
|Kernel. Distribution. Paquet         |apt, virtualbox, installation|
+-------------------------------------+-----------------------------+
|Multifenêtrage, window manager,      |                             |
|émulateur de terminaux               |                             |
+-------------------------------------+-----------------------------+


-------------------------------
6 : Outils de développement
-------------------------------

La notion de compilation séparée.

Le Makefile

La commande patch.

La notion de gestionnaire de version. GIT ? Forge UCBL (mercurial) ?

Exemples de tests de régressions en shell.

Outils de profiling. Commandes : time, prof

Les analyseurs de qualité de code source (lint)

valgrind ?


=============================================================================
INSTALLER LE QUESTIONNAIRE SUR SA MACHINE
=============================================================================

Prérequis :
  * Demander l'accès aux dépôts.
  * Python3
  * nodejs accessible sous le nom 'node'

Récupération des sources dans le répertoire QUENLIG
à partir des 3 dépôts GIT : ::

  (
  set -e # Arrêt si erreur
  DEPOT=ssh://pedagolinux.univ-lyon1.fr/home/tpetu/INF2011L
  git clone $DEPOT/QUENLIG
  cd QUENLIG
  mkdir Students
  git clone $DEPOT/QUENLIG-Questions
  mv QUENLIG-Questions/* QUENLIG-Questions/.??* Questions
  rmdir QUENLIG-Questions
  cd Questions/MUNIX1
  git clone $DEPOT/MUNIX
  cd MUNIX
  make # Traduction Python→JS, tests de régression
  )

Création et lancement d'une session de test en arrière plan
pour le module 1 : ::

  cd QUENLIG
  ANNEE=2015
  SEMESTRE=1
  MODULE=1
  ADMIN="thierry.excoffier amelie.cordier"
  Questions/MUNIX1/create "$ANNEE"s"$SEMESTRE"m"$MODULE" "$ADMIN"

Si l'URL publique n'est pas en *.univ-lyon1.fr* alors CAS va refuser
d'accepter la connexion. Il faut donc se connecter en invité : ::

  http://127.0.0.1:42421/guestToto   # 42422 pour le module 2...

On peut mettre *guestToto* en *admin*, mais ce n'est pas recommandé
car n'importe qui pourrait faire tourner du code sur votre machine.

Commandes de base : ::

  ./main.py                      # Liste les options et les sessions
  ./main.py MUNIX2015s1m1 stop   # Arrête la session indiquée
  ./main.py MUNIX2015s1m1 start  # Démarre la session

Pour faire des questions, ou vous partez de questions existantes
ou bien vous lisez la documentation :
http://perso.univ-lyon1.fr/thierry.excoffier/QUENLIG/en.html#question_creation


