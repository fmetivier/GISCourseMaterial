import pandas as pd
import matplotlib.pyplot as plt

def use_pandas(fname='/home/metivier/Téléchargements/L1819.csv'):

    df = pd.read_csv(fname)
    
    # nombre d'etudiant.e.s par annee et par genre
    print( df.groupby(['Genre','Annee']).count()['N'] )
    
    # export de ce nombre vers un tableau pour analyse graphique
    listeGenre = df.groupby(['Genre','Annee']).count()['N'] .tolist()
    
    print(listeGenre)
    
    
def use_classical(fname='/home/metivier/Téléchargements/L1819.csv'):

    f = open(fname,'r')
    entete = f.readline()
    lines = f.readlines()
    f.close()

    ngenre = [0,0] # premiere valeur = femmes, seconde valeur = hommes
    for line in lines:
        d=line.split(',')
        if 'Mme' in d[1]:
            ngenre[0] += 1
        else:
            ngenre[1] += 1
            
    print ( 'Femmes: %i,\nHommes %i' % (ngenre[0],ngenre[1]) )
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.pie(ngenre, labels = ['Femmes','Hommes'])
    
    plt.show()
    


# nous verrons cette commande la prochaine fois.
if __name__ == '__main__':    
    use_pandas()    
    use_classical()
