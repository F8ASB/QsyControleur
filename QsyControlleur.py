#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import  os

'''
                   > QsyControlleur.py <

Programme de gestion de QSY Salon
Ce script permet lorsque qu'il est integré dans CRON de gerer un QSY
programmé. Avant d'effectuer le QSY ce script controle que le relais
n'est pas en émission afin d'éviter de couper un QSO
73 & 88 de F8ASB & F8ASB Junior

Plus d'info: F8ASB.COM

'''

##############
# PARAMETRES #
##############

#Entrer le GPIO de la detection PTT
gpio="gpio18"

#Entrer le temps entre les test en s
timetest=10

#Chemin du script à lancer
Script_Path="/etc/spotnik/restart.bav"


while True:

    fichier = open("/sys/class/gpio/"+gpio+"/value", "r")
    etat = fichier.read()

    print ("Etat GPIO: "+etat)

    if etat == "0\n":
        print ('\x1b[1;37;40m'+"+++++++++++" +'\x1b[0m')
        print ('\x1b[1;37;40m'+"+ PTT OFF +" +'\x1b[0m')
        print ('\x1b[1;37;40m'+"+++++++++++" +'\x1b[0m')

        print ('\x1b[3;31;42m'+"lancement QSY " +'\x1b[0m')
        os.system (Script_Path)
        break
    else:
        print ('\x1b[5;37;41m'+"     +++++++++++     " +'\x1b[0m')
        print ('\x1b[5;37;41m'+"     + PTT ON  +     " +'\x1b[0m')
        print ('\x1b[5;37;41m'+"     +++++++++++     " +'\x1b[0m')
        print ('\x1b[6;31;47m'+"Nouveau test dans "+str(timetest)+"s" +'\x1b[0m')
        time.sleep(timetest)
