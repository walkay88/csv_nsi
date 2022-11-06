from pickle import APPEND #on import APPEND de la bibliotheque pickle (pour la derniere ligne) 


def tableau(nom_fichier):   #on crée la fonction tableau qui prend en parametre nom_fichier
 
    fichier=open(nom_fichier,'r')   #on definit la variable fichier pour ovrir le fichier enumérer plus tard
    liste=[]  #on créé un liste "vide"                        
    n=0   #on sit que n = 0
    for enregistrement in fichier:  #on créé une boucle qui parcourt tt les elements du fichier
        liste.append(enregistrement.split(';'))  #on dit que les ";" sont des separations entre les elements 
        n=n+1     #on dit que n = n+1 pour indiqué la nouvelle valeur de n
    liste.pop(0)  #on supprime la premiere ligne du tableau
    n=n-1   #comme precedemment
    for element in liste:     #on recréé une boucle mais pour parcourir cet fois les elements de la liste
        element[9]=int(element[9])   #et on change le type du 10e element pour passer de str a int
        supp(liste,1)   #on supprime tt la premier colonne de la liste (sexe)
   
    fichier.close()    #on fermme le fichier          
    tab=[liste,n]    #on dit que tab comprend la liste et la variable n
    return tab  #et on renvoie tab


def cherche_pays(pays,liste):   #on créé la fonction cherche_pays qui prend en parametre pays et liste 
    compt=0    #on definit la variabe compt comme nul (=0)
    for element in liste:    #on créé une boucle pour parcourir les elements de la liste
        if element[1]==pays:   #si le 2 element est le pays 
         compt=compt+1   #alors on rajoute 1 a la variable compt
    return compt    #on renvoie compt
 
def compteur(liste,po,carac):  #on créé la fontion compteur qui prend en parametre liste , po et carac
    t=0   #on definit la variable t (=0)
    for element in liste:    #on créé une boucle pour parcourir les elements de la liste
        if element[po]==carac:     #si l'elements du parametre po = carac 
            t=t+1   #alors on ajoute 1 a la variable t
    return t   #on renvoie t

def ncarac(liste,n,po):    #on créé la fontion ncarac qui prend en parametre liste , n et po
    ls=[]       #on definit une liste vide 
    for elt in liste:    #on créé une boucle pour parcourir les elements de la liste
        if elt[0]==n:   #si le premier element est egale a n 
            ls.append([elt[0],elt[po]])   #alors la variable ls apprend le premier element de la liste et l'element po
    return ls    #on renvoie ls
 
def comp(liste,carac,po):   #on créé la fontion comp qui prend en parametre liste , carac et po 
    r=0   #on definit la variable r (=0)
    if type(carac)== int:    #si le type de carac est int
        for element in liste:       #on créé une boucle pour parcourir les elements de la liste

            if element[8]>carac:  #si l'element[8] (donc le neuvieme) est supperieur a carac 
                r=r+1  #on ajoute 1 a la variable r
    else:  # sinon (si le type de carac est autre que int)
        for element in liste:  ##on recréé une boucle pour parcourir les elements de la liste
            if element[po]==carac:    #si les elements du parametre po est egale a carac
                r=r+1    #alors on 1 ajoute  a la variabler 
    return r   #on renvoi nb
 
def compte_carac(liste,colcar1,colcar2,colcar3,caracA,caracB,caracC,s):  #on créé une fonction prenant en parametre liste, colcar1, colcar2, colcar3, caracA, caracB, caracC, s
    
    nb=0   #on dit que la variable nb est egale a 0
    ls=[]   #on créé une liste nommé ls
    if type(caracA)  == int or type(caracB)  == int :   #si le type de caracA est egale a int ou si le type de caracB est egale a int
        print('true') #on 'imprime' "true"
        if type(caracA)==int:  #donc si caracA = int
                taille=caracA
                carac=caracB       #alors le taille est egale au caracA , le carac est celui du caracB et col est egale au colcar2
                col=colcar2
        elif type(caracB)==int:  #si cest le type du caracB qui est en int
                taille=caracB
                carac=caracA         #alors la taill est celui du caracB ,le carac est celui du caracA ete les col=colcar1
                col=colcar1
        for element in liste:  #on créé une boucle pour parcourir les elements de la liste
           
            if element[8]>taille and element[col]== carac :  #si le neuvieme element est supperieur a la taille et que l'element col est egale au carac 
                ls.append([element[0]])    #on apprend le premiere element a la variable ls
                nb=nb+1     #et on ajoute 1 a nb
    else: #si caracA et caracB ne sont pas en int  alors:
        if s==0:  #si s est = 0
         for element in liste:   #on recréé une boucle pour parcourir les elements de la liste
            if element[colcar1]==caracA and element[colcar2]==caracB:    #si l'element[colcar1] est egale au caracA et que l'element[colcar2] est egale au caracB
                nb=nb+1  #on ajoute 1 a la variable nb
                ls.append([element[0]])    #on aprend le premiere element a ls 
        if s==1:  #si s = 1
            for element in liste:  #on recréé une boucle pour parcourir les elements de la liste
                if element[colcar1]==caracA and element[colcar2]==caracB and element[colcar3]==caracC: #si element[colcar1] est egale au caracA et que element[colcar2] est egale zu caracB et que element[colcar3] est egale au caracC 
                    nb=nb+1  #on ajoute 1 a nb
                    ls.append([element[0]])  #on apprend le premiere element a ls
 
    return [nb,ls]  #on revoie la variable nb et la liste ls
                    
 
f='ou_est_charlieV2_ANSI (1).txt'       #on dit que f = au nom du fichier 'ou_est_charlieV2_ANSI (1).txt'
tab=tableau(f)[0]           # tab est egale a la fonction tableau (on ouvre le fichier 'ou_est_charlieV2_ANSI (1).txt')
 
print("=",cherche_pays('France',tab),"Français") #on prend la fonction cherche_pays ou on cherche le pays 'France' et on renvoie le nombre de personne qui on france en pays
print("=",cherche_pays('Belgique',tab),"Belgique")  #on prend la fonction cherche_pays ou on cherche le pays 'Belgique' et on renvoie le nombre de personne qui on Belgique en pays                           #tab = le fichier en question ('ou_est_charlieV2_ANSI (1).txt')
print("=",compteur(tab,6,'bleu'),"yeux bleus") #on prend la fonction compteur pour compter le nombre de personne ayant les yeux bleu 
 
print(ncarac(tab,'BOUDJELLEL',[1])) #on execute la  fonction ncarac pour trouver le pays assossié a BOUDJELLEL (pays=2e element donc =[1])
print(ncarac(tab,'YOOK',[6]))      #on execute encore la fonction ncarac pour trouver la couleur des yeux de YOOK
print("=",comp(tab,180,8),"individues de plus de 1.80m")  #on execute la fonction comp pour trouver les individues de plus de 1 metre 80
print("=",compte_carac(tab,1,8,0,'France',180,0,0)[0],"Fr et +1.80m")  #on execute la fonction compte__carac pour trouver combien d'individues dont francais et de plus de 1m80
print("=",compte_carac(tab,2,5,0,'brun','oui',0,0)[0],"bruns tatoué" )  #on rexecute compte_carac pour trouver le nombre de bruns tatoué 
print("=",compte_carac(tab,2,5,4,'chauve','oui','non',1)[1],"chauve,tatoué et sans barbe")  #pareil pour trouver le nombre de chauve ,tatoué et sans barbe 
 
APPEND(tab,'Nollan','france','marron','non','non','non','bleu','non',178)  #on apprend on ligne supplementaire 
 