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
            bg_color = "red"
            bg_image_url = "https://checkin.fusionarena.ch/assets/equipment-adventure-de.png"
        else:
            # dies ist ein vertikales Bild
            # tvrs plakat als hintergrund
            bg_color = "blue"
            bg_image_url = "https://checkin.fusionarena.ch/assets/poster/tikal.png"

    # API ref
    # https://www.remove.bg/api#api-reference
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={
            'image_file': open('images/' + f, 'rb')
        },
        data={
            'size': 'preview',
            'bg_image_url': bg_image_url,
            # 'bg_color': 'FFFFFF', # you can only use 1 bg_parameter per request
            'format': 'png'
        },
        headers={'X-Api-Key': 'upJTVS9JT2StBJCm3KdBBzJ7'},
        ###

        # Account is currently not linked with credit card, only 50 images are free per month
        # Update api key or omit it from git when deploying production version

        ###
    )

    """
    # required for debugging
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    """

    if response.status_code == requests.codes.ok:
        path_processed = 'images_processed/' + f
        with open(path_processed, 'wb') as out:
            out.write(response.content)
            print("")
            print(path_processed + ": DONE")
    else:
        print("Error:", response.status_code, response.text)
