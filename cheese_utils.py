import os
from simple_image_download import simple_image_download as simp
from functools import partial
from multiprocessing import Pool
fromages_francais = ['Abondance', 'Banon', 'Beaufort', 'Bleu d\'Auvergne', 'Bleu de Bresse', 'Bleu des Causses', 'Bleu du Vercors-Sassenage', 'Boursault', 'Boursin', 'Brie', 'Brillat-Savarin', 'Camembert', 'Cancoillotte', 'Cantal', 'Caprice des Dieux', 'Chaource', 'Chavignol', 'Comté', 'Coulommiers', 'Crottin de Chavignol', 'Curé Nantais', 'Edam', 'Emmental', 'Époisses', 'Etorki', 'Fédou', 'Fol Épi', 'Fourme d\'Ambert', 'Fourme de Montbrison', 'Gaperon', 'Gouda', 'Grebeye', 'Gruyère', 'Laguiole', 'Langres', 'Livarot', 'Mâconnais', 'Maredsous', 'Maroilles', 'Mont d\'Or', 'Morbier', 'Munster', 'Neufchâtel', 'Ossau-Iraty', 'Parmesan', 'Pélardon', 'Petit-Suisse', 'Picodon', 'Pont-l\'Évêque', 'Pouligny-Saint-Pierre', 'Pyramide', 'Reblochon',
                     'Red Leicester', 'Rocamadour', 'Roquefort', 'Saint Agur', 'Saint-Félicien', 'Saint-Marcellin', 'Saint-Nectaire', 'Saint-Paulin', 'Sainte-Maure de Touraine', 'Salers', 'Selles-sur-Cher', 'Stilton', 'Taleggio', 'Tamie', 'Tête de Moine', 'Tomme de Chèvre', 'Tomme de Savoie', 'Tomme des Pyrénées', 'Trappe d\'Échourgnac', 'Valençay', 'Vieux-Boulogne', 'Vieux-Lille', 'Reblochon', 'Cîteaux', 'Mimolette', 'Brocciu', 'Pavé d\'Affinois', 'Leerdammer', 'Curé Nantais', 'Pavé de Jadis', 'Fondue savoyarde', 'Raclette', 'Comté Fort Saint Antoine', 'Comté Extra Vieux', 'Comté Saint Antoine', 'Comté Premier Cru', 'Beaufort d\'été', 'Beaufort d\'hiver', 'Roquefort Carles', 'Roquefort Société', 'Roquefort Papillon', 'Roquefort Gabriel Coulet']


DB_DIR = "db"


def download_cheese(name, limit=20):
    response = simp.simple_image_download
    # add 'fromage' to the search query but not to the folder name (+ 'fromage' is not a valid folder name)
    response().download(name + "_fromage", limit)

    # remove _fromage from the folder name
    os.rename(os.path.join('simple_images', name + "_fromage"),
              os.path.join('simple_images', name))


def download_cheese_parallel(fromage):
    # remove accents and capital letters
    fromage = fromage.lower()
    fromage = fromage.replace(" ", "-")
    fromage = fromage.replace("é", "e")
    fromage = fromage.replace("è", "e")
    fromage = fromage.replace("ê", "e")
    fromage = fromage.replace("à", "a")
    fromage = fromage.replace("â", "a")
    fromage = fromage.replace("î", "i")
    fromage = fromage.replace("ï", "i")
    fromage = fromage.replace("ô", "o")
    fromage = fromage.replace("û", "u")

    # check if the folder exists
    if not os.path.exists(os.path.join(DB_DIR, fromage)):
        os.makedirs(os.path.join(DB_DIR, fromage))
        print("Created folder for", fromage)

    download_cheese(fromage, 100)


if __name__ == "__main__":
    # create the db folder
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        print("Created db folder")

    # download the images
    with Pool(20) as p:
        p.map(download_cheese_parallel, fromages_francais)
