import os
import cv2
import cv2.aruco as aruco
import random


def detect_marker(path_to_image):
    image = cv2.imread(path_to_image)
    filename = os.path.basename(path_to_image)

    # Wähle ein ArUco-Dictionary aus
    # Wir verwenden aktuell: PREDEFINED_DICTIONARY_NAME = aruco.DICT_4X4_50
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    parameters.adaptiveThreshWinSizeMin = 3
    parameters.adaptiveThreshWinSizeMax = 23
    parameters.adaptiveThreshWinSizeStep = 10
    corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict, parameters=parameters)

    # Überprüfe, ob Marker gefunden wurden
    if ids is not None:
        print(f"Gefundene Marker-IDs: {ids.flatten()}")

        # Zeichne die Marker-Ränder und IDs auf das Bild
        aruco.drawDetectedMarkers(image, corners, ids)

        # Zeige das Ergebnis
        cv2.imshow("Detected ArUco Markers", image)
        # cv2.imwrite("output/filename", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Keine ArUco-Marker gefunden.")
        # return False

    return random.choice([1, 5])  # Aktuell gibt es 5 courts
    # return court


def determine_court(ids):
    # effektive business logik
    if ids in [1, 2, 3, 4, 5]:
        court = "left"
    elif ids in [6, 7, 8, 9, 10]:
        court = "right"
    # Discuss naming schema for multiple FA locations
    return {
        "location": {
            "locationId": 1,
            "locationName": "Zürich"
        },
        "court": {
            "courtId": 1,
            "courtName": "left"
        }
    }


def get_original_datetime(photo):
    return 1


print(detect_marker("training/input/galgenen3.jpeg"))
