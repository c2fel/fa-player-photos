import requests
import os
from PIL import Image

files = [f for f in os.listdir("images") if os.path.isfile(os.path.join("images", f)) and f.lower().endswith('.jpeg')]

for f in files:
    # Öffne das Bild
    with Image.open("images/" + f) as img:
        # Hole die Dimensionen (Breite, Höhe)
        width, height = img.size
        if width > height:
            # dies ist ein horizontales Bild
            # nur fa roter Hintergrund
            bg_color = "#FF7A84"
            bg_image_url = ""
        else:
            # dies ist ein vertikales Bild
            # tvrs plakat als hintergrund
            bg_color = "#FFF799"
            bg_image_url = "https://checkin.fusionarena.ch/assets/poster/tikal.png"

        print(f"Breite: {width}, Höhe: {height}")

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={
            'image_file': open('images/' + f, 'rb'),
            'bg_color': bg_color,
            # 'bg_image_url': bg_image_url,
            'format': 'jpg',
            'size': 'preview'
        },
        data={'size': 'auto'},
        headers={'X-Api-Key': 'upJTVS9JT2StBJCm3KdBBzJ7'},
        ###

        # Account is currently not linked with credit card, only 50 images are free per month
        # Update api key or omit it from git when deploying production version

        ###
    )
    if response.status_code == requests.codes.ok:
        path_processed = 'images_processed/' + f
        with open(path_processed, 'wb') as out:
            out.write(response.content)
            print("")
            print(path_processed + ": DONE")
    else:
        print("Error:", response.status_code, response.text)
