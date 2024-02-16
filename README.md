# Miller-RabinM1
DM Cryptographie S8 M1 Miller Rabin 

Auteur : GEORGEL Mathis et SCHLESINGER Joseph

# Présentation
Ce programme est un DM de cryptographie de M1. Il a pour but de tester la primalité d'un nombre donné en utilisant le test de Miller-Rabin. Il est possible de tester la primalité de nombre allant jusqu'à 4096 bits.

# Utilisation
Pour lancer le programme sans modification, il suffit de lancer la commande suivante dans le terminal:
```make main```

Si on souhaite lancer le programme sans lancer Eval 4096 etc, il suffit de lancer la commande suivante dans le terminal:
```make {chiffre}```
où {chiffre} est le chiffre que l'on souhaite tester.
(1 : 128, 2 : 128-256, 3 : 128-256-512, 4 : 128-256-512-1024, 5 : 128-256-512-1024-2048, 6 : 128-256-512-1024-2048-4096)

Exemple:
```make 3``` pour tester la primalité d'un nombre de 128, 256 ou 512 bits.

# Nettoyage
Pour nettoyer le fichier d'exécution, il suffit de lancer la commande suivante dans le terminal:
```make clean```

# Remarques
Pour clone et lancer le programme, il suffit de lancer les commandes suivantes dans le terminal:
```
git clone https://github.com/mathis-grgl/Miller-RabinM1.git
cd Miller-RabinM1
make main```