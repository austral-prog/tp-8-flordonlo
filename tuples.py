
def get_coordinate(record):
    treasure, cordinate = record
    return cordinate


def convert_coordinate(coordinate):
    return coordinate[0], coordinate[1]



def create_record(azara_record, rui_record):
     tesoro, coordenada= azara_record
    ubicación, coordena_da, cuadrante= rui_record
    if convert_coordinate(coordenada) == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match"
