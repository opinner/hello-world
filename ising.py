import numpy as np
import matplotlib.pyplot as plt


def create_lattice(n,m):
    """erstellt ein 2D gitter mit n Reihen und m Spalten"""
    #lattice = np.ones((n,m), dtype = np.int8 )
    lattice = np.random.choice((-1,1), size = (n,m))
    return lattice



def print_lattice(lattice):
    """gibt das Gitter aus"""
    print(lattice,"\n")




def naive_hamiltonian(lattice,J):
    """Berechnet den Hamiltonian des Gitters lattice bei manuell eingerichteten Randbedingungen"""


    # Erstellt das Gitter auf dem gerechnet wird 
    calc_lattice= lattice


    #Erstellen der periodischen Randbedingungen:
    #Fügt die oberste Reihe unten an
    calc_lattice = np.append(calc_lattice,[lattice[0]], axis = 0)
    #Fügt die unterste Reihe oben an
    calc_lattice = np.append([lattice[-1]],calc_lattice, axis = 0)
    # Fügt die linke Seite rechts an
    calc_lattice  = np.concatenate((calc_lattice,np.atleast_2d(calc_lattice[:,0]).T),axis = 1)
    # Fügt die rechte Seite (des Origialgitters, hier also die 2. von rechts) links an
    calc_lattice  = np.concatenate((np.atleast_2d(calc_lattice[:,-2]).T, calc_lattice),axis = 1)


    #Setzt die Ecken zur Übersicht auf 0
    calc_lattice[0,0]= 0
    calc_lattice[0,-1]= 0
    calc_lattice[-1,0]= 0
    calc_lattice[-1,-1]= 0


    # Berechnung der Summe über die nächsten Nachbarn
    count = 0
    energy = 0
    dim_org = np.shape(lattice)
    dim = np.shape(calc_lattice)

    # Schleife läuft nur über die originale Gittergröße m,n 
    for row in range(1,dim[0]-1):               
        for column in range(1,dim[1]-1):
            energy += calc_lattice[row,column]*calc_lattice[row,column+1]
            energy += calc_lattice[row,column]*calc_lattice[row,column-1]
            energy += calc_lattice[row,column]*calc_lattice[row+1,column]
            energy += calc_lattice[row,column]*calc_lattice[row-1,column]
            count += 1

            #print (row, column, sep =",", end = " ")

    if count != dim_org[0]*dim_org[1]:
        print("Error, Hamiltonian isnt computed on the original lattice")
    
    print("H =",-J*energy)




def visualize(lattice, colour = None):
    """ gibt das Gitter als Grafik aus. colour bestimmt die cmap"""
    plt.imshow(lattice, interpolation = "none", origin = "upper", cmap = colour)
    plt.title("Ising model lattice")    
    #plt.colorbar(orientation='vertical')
    plt.show()



lattice = create_lattice(20,20)
print_lattice(lattice)
naive_hamiltonian(lattice,1)
visualize(lattice)

