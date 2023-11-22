# Elements nécessaires à l'utilisation du modèle pré-entrainé two_classes_model.pkl 

def label_func(fname):
    # Liste des classes appartenant à "zones naturelles"
    nature_classes = ['Forest', 'River', 'AnnualCrop', 'HerbaceousVegetation', 'PermanentCrop', 'SeaLake', 'Pasture']
    # Vérifie si le nom du fichier contient l'une des classes de nature
    if any(nc in fname.name for nc in nature_classes):
        return 'Nature'
    else:
        return 'Human'
    