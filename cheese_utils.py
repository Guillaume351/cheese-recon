from simple_image_download import simple_image_download as simp  #importing the library

DB_DIR = "db"

def download_cheese(name, limit=20):
    response = simp.simple_image_download

    response().download(name, limit)

download_cheese("beaufort, fromage", 100)
download_cheese("camembert", 100)