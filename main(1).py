def couleur(nom_fichier):
 
    fichier=open(nom_fichier,'r')   
    liste=0                          
    for elt in fichier:  
        if elt =='bleu':
              liste = liste +1

    fichier.close()                 
    return liste                      
 
f='ou_est_charlieV2_ANSI.csv'       
liste=couleur(f)           
