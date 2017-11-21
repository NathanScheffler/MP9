# Magic Motion
Mini-Projet 9 - Alarme par wifi (Raspberry Pi)

## Description 
Ce mini-projet a été réalisé par @NathanScheffler et @ValentinRacat

Une Raspberry Pi munit d'un capteur de proximité (PIR) doit pouvoir alarmer l'utilisateur du système d'une intrusion dans une salle.

Le système, lorsqu'il détecte une présence, alerte par wifi le serveur et allume son alarme (LED + Buzzer). Le serveur de son côté doit pouvoir traiter l'information et calculer la présence théorique de l'intrus avant de l'envoyer sur une base de donnée MySQL.

Un site web servira d'intermédiaire à distance entre l'utilisateur et la salle. Il comprendra un historique et l'état actuel du capteur ainsi que la présence possible d'un individu.

## Matériel
- Raspberry Pi 3 Model B
- Grove LED Socket Kit (Rouge)
- Grove Buzzer
- DFRobot PIR Motion sensor
- Ordinateur sous Windows (Serveur MySQL + Web) 
