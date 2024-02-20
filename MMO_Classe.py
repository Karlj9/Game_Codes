#====================================| Parent Class |====================================#
class MMO:
    def __init__(self):
        self.players = 1                                # initialise dans self le nombre de vie
        self.Health()                                   # lie la vie aux personnages 
        self.Fight()                                    # lie les degat aux personnages
        # en mettant les methodes directement dans la classe initiale je n'ai pas besoins de les rappelers a la fin du code
        # en effet en appelant la classe, je les appellerai egalement 
    def Health(self):
        self.n_lifes = 5
        self.n_HP = 1000
        print("Health Point = 1000")
    def Fight(self):
        self.n_DPS = 100
#===================================| Child 1 Class |====================================#
class Hunter(MMO):                                      # Dans la nouvelle classe, j'appel la classe "MMO" afin de recuperer ses attribus (heritage de classes)
    #print("HUNTER")                                    # je renvoie le nom de la classe
    #pass                                               # on utilise pass si la classe est similaire en tout point
    def __init__(self):
        super().__init__()                              # cela permet de changer la classe parent depuis la classe enfant
        self.__Power = 1                                # ne mettant deux underscore [_] l'information de "Power" est privee
    def armor (self):
        resistance = My_character.n_HP * 2.5            # je recupere la vie en faisant "My_character.n_HP" et je la multiplie pour avoir l'armure    
        print("Armor = ", resistance)                   # renvoie l'armure du personnage
    def DPS (self):
        Damage = My_character.n_DPS * 1.5               # je recupere les DPS en faisant "My_character.n_DPS" et je les multiplie
        print("Damage = ", Damage)                      # renvoie les degats q'uinflige le personnage
#===================================| Child 2 Class |====================================#
class Mage(MMO):                                        # Dans la nouvelle classe, j'appel la classe "MMO" afin de recuperer ses attribus (heritage de classes)
    #print("MAGE")                                      # je renvoie le nom de la classe
    def __init__(self):
        super().__init__()                              # cela permet de changer la classe parent depuis la classe enfant
        self.__Power = 1                                # ne mettant deux underscore [_] l'information de "Power" est privee
    def armor (self):
        resistance = My_character.n_HP * 1.5            # je recupere la vie en faisant "My_character.n_HP" et je la multiplie pour avoir l'armure    
        print("Armor = ", resistance)                   # renvoie l'armure du personnage
    def DPS (self):
        Damage = My_character.n_DPS * 2                 # je recupere les DPS en faisant "My_character.n_DPS" et je les multiplie
        print("Damage = ", Damage)                      # renvoie les degats q'uinflige le personnage
#===================================| Child 3 Class |====================================#
class Warrior(MMO):                                     # Dans la nouvelle classe, j'appel la classe "MMO" afin de recuperer ses attribus (heritage de classes)
    #print("WARRIOR")                                   # je renvoie le nom de la classe
    def __init__(self):
        super().__init__()                              # cela permet de changer la classe parent depuis la classe enfant
        self.__Power = 2                                # ne mettant deux underscore [_] l'information de "Power" est privee
    def armor (self):
        resistance = My_character.n_HP * 4.5            # je recupere la vie en faisant "My_character.n_HP" et je la multiplie pour avoir l'armure    
        print("Armor = ", resistance)                   # renvoie l'armure du personnage
    def DPS (self):
        Damage = My_character.n_DPS * 0.75              # je recupere les DPS en faisant "My_character.n_DPS" et je les multiplie      
        print("Damage = ", Damage)                      # renvoie les degats q'uinflige le personnage
#===================================| Child 4 Class |====================================#
class Thief(MMO):                                       # Dans la nouvelle classe, j'appel la classe "MMO" afin de recuperer ses attribus (heritage de classes)
    #print("Thief")                                     # je renvoie le nom de la classe
    def __init__(self):
        super().__init__()                              # cela permet de changer la classe parent depuis la classe enfant
        self.__Power = 2                                # ne mettant deux underscore [_] l'information de "Power" est privee
    def armor (self):
        resistance = My_character.n_HP * 0.4            # je recupere la vie en faisant "My_character.n_HP" et je la multiplie pour avoir l'armure    
        print("Armor = ", resistance)                   # renvoie l'armure du personnage
    def DPS (self):
        Damage = My_character.n_DPS * 0.75              # je recupere les DPS en faisant "My_character.n_DPS" et je les multiplie      
        print("Damage = ", Damage)                      # renvoie les degats q'uinflige le personnage
#===================================| Player Choice |====================================#
def Player_choice():
    print ("1 = Hunter")
    print ("2 = Mage")
    print ("3 = Warrior")
    print ("4 = Theif")
    infoClass = []                                      # je cree une liste dans laquelle je mettrai la valeur entree par le joueur
    n_Class = input ("Put the number of the class : ")  # le joueur rentre un nombre (en l'occurence 1 | 2 | 3 )
    infoClass.append(n_Class)                           # ajoute la reponse du joueur a la liste
    for i in infoClass:
        if i == '1':
            print ("You chose HUNTER class")
            #My_character = Hunter()
        elif i == '2':
            print ("You chose MAGE class")
            #My_character = Mage()
        elif i == '3':
            print ("You chose WARRIOR class")
            #My_character = Warrior()
        elif i == '4':
            print ("You chose Thief class")
            #My_character = Thief()
        else:
            print ("wrong number in input")
            Player_choice()
    
#My_character = Hunter()                                # liaison de mon personnage a la classe MMO
#My_character.Health()                                  # donne a l'objet "My_character" la methode "Health"
#My_character.Fight()                                   # donne a l'objet "My_character" la methode "Fight"
#My_character.armor()                                   # donne a l'objet "My_character" la methode "armor"
#My_character.DPS()                                     # donne a l'objet "My_character" la methode "DPS"
#print(My_character.players)                            # ainsi je lie le personnage au nombre de vie de la classe
#print(My_character._Hunter__Power)
Player_choice()
