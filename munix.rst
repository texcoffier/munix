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
 * Autant de séances de TP que les étudiants veulent. Présence non obligatoire.

6 examens de 25 minutes à passer quand les étudiants le veulent :
   * Le premier examen, avant la semaine 4
   * Le deuxième avant la semaine 6
   * ...
   * Le sixième avant la semaine 14

Soit 2h30 d'examen pour l'UE (actuellement 3*5 + 2*45 + 90 = 195 = 3h15)


Chaque semaine 5 créneaux d'1h30 (un par jour). Sur chaque créneau :
   * une salle de TP pour ceux qui veulent travailler en groupe
     ou bien venir discuter avec un enseignant.

   * une salle d'examen permettant de faire passer 45 examens par créneau.

Coût :
  * 12 semaines * 5 créneaux 1h30 * 2 enseignants = 180 heures eq TD
  * Droit de tirage : 30h par groupe
  * Il faut donc 6 groupes pour équilibrer (6*36 = 216 étudiants)
  * Maximum d'examen passable : 45 * 5 * 12 = 2700 (/6) soit 450 étudiants
    si l'on est à flux tendu. On peut prendre une salle plus grande.


L'apprentissage est fait via un cours/TD/TP intégré avec QUENLIG.
  * Le TP prévient quand l'étudiant a les connaissances suffisantes
    pour passer l'examen.
  * L'étudiant peut continuer à s'entrainer jusqu'à épuisement des questions.
  * L'étudiant n'est pas forcé de faire le TP pour passer l'examen.
    Mais on ne peut passer l'examen qu'une seule fois.

Utilisation d'unix pour ceux qui ne l'ont pas chez eux :
   * Via le navigateur web : http://bellard.org/jslinux/
   * Via putty : sur linuxetu.univ-lyon1.fr puis pedagolinux.univ-lyon1.fr
   * Via un live CD : il faut graver un CD et on a plus accès à windows
   * Via une machine virtuelle : c'est plus compliqué à lancer.
   * Via cygwin : c'est pas sous unix :-(
   * Via son téléphone android (c'est dangereux)

=============================================================================
                                      PROGRAMME
=============================================================================

Décomposé en 6 parties pour les 6 examens.

Certaines parties ont moins de connaissances théoriques mais
nécessitent plus de pratique.

----------------------
Le système de fichier
----------------------

Intro : Pourquoi ce cours. Histoire. Comment accéder à unix et au shell.

Concepts : hiérarchie, répertoire, fichier, chemin, répertoire courant

Ccommandes :

   * Navigation : cd, pwd, ls

   * Manipulation : cp, rm, mv, ln, mkdir, gzip, iconv, convert?, avconv?

   * Affichage : cat, zcat, more, sort, du

   * Autre : date, man

Notion d'option de commande (et de paramètre d'option ?)

Edition de l'historique avec les touches curseurs.
   
Et la complétion de commande.


----------------------------------
Variables, patterns et boucles
----------------------------------

Les variables. HOME, PATH, PS1, remplacement $(...)

L'échappement : guillemet, cote, backslash

Les patterns.

L'enchainement de commandes avec ';' et '&&'

La boucle for.

La boucle 'while' et le 'read'


------------------------------------
Redirections, expressions régulières
------------------------------------

Les redirections dans les fichiers (pas le pipe).

Les expressions régulières.

Les commandes : grep, sed, echo, awk

Expressions régulières dans vi, emacs, en Javascript, Python, C ?


------------------------
Scripts et processus
------------------------

Concepts : Processus et pipeline
commandes : kill, killall, ps, pstree, top, free

Groupement de commandes avec ( )

Lancements de batch : &, ^Z, bg, nohup

Editeur de texte : donner les liens vers les tutoriaux. En imposer un ?

Script : argument, commentaire, exit, $?, export

Le 'if'

Commandes : test, expr, ulimit


---------------------------
Système et réseaux
---------------------------

Concepts : utilisateur, groupe, droits
Commandes : chown, chgrp, chmod

Concepts : Périphérique, disque, TTY, liaison série, clavier, souris, écran
Commandes : mount, df, find, tar, sshfs, récupérer les fichiers perdus.

Concepts : client, serveur, nom machine, adresse IP, clefs privés/publiques
Commandes : ssh, scp, rsync, wget, sendmail

Les impressions

Concepts : Kernel. Distribution. Paquet.
Commandes : apt-get ? virtualbox ? Installation ?

Concepts : Multifenêtrage, window manager, émulateur de terminaux
Commandes : ??????


-----------------------
Outils de développement
-----------------------

La notion de compilation séparée.

Le Makefile

Les commandes diff et patch.

La notion de gestionnaire de version. GIT ? Forge UCBL (mercurial) ?

Exemples de tests de régressions en shell.

Outils de profiling. Commandes : time, prof

Les analyseurs de qualité de code source (lint)

valgrind ?


=============================================================================

Cette version montre plus de choses, mais ira moins dans les détails
et les cas tordus.

En moins par rapport à l'actuel :
   * Internationalisation.
   * Préférences
