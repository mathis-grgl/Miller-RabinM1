import secrets
import matplotlib.pyplot as plt
import sys



# Question 3
'''Implémentez la fonction Decomp() qui prend en entrée n et renvoie s et d tel que
n - 1 = 2sd avec d impair. Testez-la sur 10000 valeurs différentes.'''
def Decomp(n):

    # On affecte à s la valeur de 0 et à d la valeur de n - 1
    s = 0
    d = n - 1

    # Tant que d est divisible par 2, on incrémente s et on divise d par 2
    while d % 2 == 0:
        s += 1
        d //= 2

    return s, d

# Pour bit allant de 0 à 10000
for bit in range(10000):

    # On génère une valeur aléatoire entre 0 et 2000000 et impair !
    n = secrets.randbelow(1000000) * 2 + 1 

    # On utilise la fonction Decomp pour obtenir s et d
    s, d = Decomp(n)

    # On vérifie si la condition est bien respectée (n - 1 = 2^s * d avec d impair) pour les 10000 valeurs
    assert (n - 1) == (2 ** s) * d, f"Échec pour n = {n}"





# Question 4
'''Implémentez la fonction ExpMod(). Testez-la sur 10000 valeurs différentes.'''
def ExpMod(n, a, t):
    # On affecte à resultat la valeur de 1
    resultat = 1

    # On convertit t en binaire
    t_binaire = bin(t)[2:]

    # On parcourt chaque bit de t_binaire
    for t_bit in t_binaire:

        # On met à jour le résultat
        resultat = (resultat * resultat) % n

        # Si le bit est égal à 1
        if t_bit == '1':
            # On met à jour le résultat
            resultat = (resultat * a) % n

    # On renvoie le résultat
    return resultat

# Pour bit allant de 0 à 10000
for bit in range(10000):

    # On génère une valeur aléatoire entre 0 et 10000
    a = secrets.randbelow(100000)
    t = secrets.randbelow(100000)
    n = secrets.randbelow(100000)

    # On utilise la fonction ExpMod
    f = ExpMod(n, a, t)

    # On vérifie si la condition est bien respectée (a ** t % n == f) pour les 10000 valeurs
    assert f == pow(a, t, n), f"Échec pour a = {a}, t = {t} et n = {n}"





# Question 5
'''Impl ́ementez le test complet de Miller-Rabin MillerRabin() qui prend en entrée n et un nombre d'itérations du test cpt. 
Cette fonction répète le test d ́ecrit à la Section 2.2 cpt fois et renvoie ensuite '0' si le nombre est composé et '1' si le nombre est probablement premier.'''

def MillerRabin(n, cpt):
    for j in range(cpt):
        # Etape 1 : n −1 = 2sd avec d impair
        s, d = Decomp(n)  

        # Etape 2 : 1 < a < n - 1 au hasard
        a = secrets.randbelow(n-2) + 2

        # Etape 3 : a^d mod n = 1 ou a^d mod n = -1 on s'arrête
        resultat = ExpMod(n, a, d)

        if resultat == 1 or resultat == - 1:
            return 1 # n est sûrement premier

        # Etape 4 : Pour t_bit allant de 1 jusqu’à s on calcule a^d2i mod n
        for t_bit in range (1, s + 1):
            resultat = ExpMod(n, a, d * 2**t_bit)
            if resultat == -1:
                return 1 # n est sûrement premier
            elif resultat == 1:
                return 0 # n est composé
        
        # Etape 5 : Fin de la boucle et que a^d2s !≡ 1 (mod n), on conclut que n est composé, comme d’après le test de Fermat
        return 0 # n est composé
    





# Question 6. 
'''Utilisez votre fonction pour tester les 3 nombres suivants ( ́ecrits en hexadécimal).
Dites si chaque nombre est pseudo-premier ou composé avec cpt = 20.'''

# n1 est une chaîne de caractères représentant un nombre en hexadécimal
n1  = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF"
# On convertit n1 en entier hexadécimal
n1 = int(n1, 16)
# On utilise la fonction MillerRabin pour tester n1 avec cpt = 20 et on affiche le résultat
print ("n1 (768 bits) =", MillerRabin(n1, 20))

# n2 est une chaîne de caractères représentant un nombre en hexadécimal
n2 = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEC4FFFFFDAF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000002D9AB"
# On convertit n2 en entier hexadécimal
n2 = int(n2, 16)
# On utilise la fonction MillerRabin pour tester n2 avec cpt = 20 et on affiche le résultat
print ("n2 (768 bits) =", MillerRabin(n2, 20))

# n3 est une chaîne de caractères représentant un nombre en hexadécimal
n3 = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF"
# On convertit n3 en entier hexadécimal
n3 = int(n3, 16)
# On utilise la fonction MillerRabin pour tester n3 avec cpt = 20 et on affiche le résultat
print ("n3 (1024 bits) =", MillerRabin(n3, 20))




# Question 7
'''Ecrivez une fonction Eval() qui prend en entr ́ee une taille en bits resultat, le compteur cpt et
donne en sortie le nombre d'itérations qu'il a fallu répéter avant de trouver un nombre probablement
premier.'''

def Eval(resultat, cpt):
    # On initialise le compteur à 0
    compteur = 0
    
    # On génère un nombre aléatoire de resultat bits
    n = secrets.randbits(resultat)

    # Tant que le nombre n est composé, on incrémente le compteur et on génère un nouveau nombre aléatoire
    while MillerRabin(n, cpt) == 0 :
        compteur = compteur + 1
        n = secrets.randbits(resultat)

    # On renvoie le compteur
    return compteur




# Question 8
'''Pour tester votre fonction Eval(), répétez 100 fois la fonction pour les valeurs de resultat
suivantes : 128, 256, 512, 1024, 2048 et 4096. Faites un graphique avec en abscisse la taille en bits du
nombre et en ordonnée la moyenne sur les 100 tests de la valeur de Compteur.'''

# On crée une liste tailles_bits contenant les valeurs 128
tailles_bits = [128]

# Vérifier s'il y a un paramètre en exécutant le programme (1 : 128, 2 : 128-256, 3 : 128-256-512, 4 : 128-256-512-1024, 5 : 128-256-512-1024-2048, 6 : 128-256-512-1024-2048-4096)
if len(sys.argv) == 2:

    # On ajoute les différentes valeurs à la liste tailles_bits en fonction du paramètre
    for i in range(int(sys.argv[1])-1):
        tailles_bits.append(tailles_bits[-1] * 2)

# Sinon, on ajoute les valeurs 256, 512, 1024, 2048 et 4096 à la liste tailles_bits
else:
    tailles_bits = [128, 256, 512, 1024, 2048, 4096]

print(tailles_bits)

# On crée une liste moyennes pour stocker les moyennes des 100 tests
moyennes = []

# Pour chaque taille de bits dans tailles_bits
for taille in tailles_bits:

    # On crée une liste compteurs pour stocker les valeurs de compteur
    compteurs = []

    # On répète 100 fois la fonction Eval pour chaque taille de bits
    for t_bit in range(100):

        # On ajoute le résultat de la fonction Eval à la liste compteurs
        compteurs.append(Eval(taille, 20))
        #print("Eval", t_bit, "pour", taille, "bits terminé.")

    # On calcule la moyenne des 100 tests
    moyenne_compteur = sum(compteurs) / 100

    # On ajoute la moyenne à la liste moyennes
    moyennes.append(moyenne_compteur)

    # On affiche la moyenne
    print("Moyenne pour", taille, "bits :", moyenne_compteur)

    # On affiche la liste des compteurs
    print("Liste des compteurs pour", taille, "bits :", compteurs)

# On crée un graphe avec en abscisse la taille en bits du nombre et en ordonnée la moyenne sur les 100 tests de la valeur de Compteur
plt.plot(tailles_bits, moyennes, marker='o')

# On ajoute un nom à l'axe des abscisses
plt.xlabel('Taille en bits du nombre')

# On ajoute un nom à l'axe des ordonnées
plt.ylabel('Moyenne du nombre de répétitions')

# On ajoute un titre au graphe
plt.title('Moyenne du nombre de répétitions en fonction de la taille du nombre')

# On affiche le graphe
plt.show()

