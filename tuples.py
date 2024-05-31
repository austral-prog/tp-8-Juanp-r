def get_coordinate(record):
    return str(record[1])

def convert_coordinate(coordinate):
    cord=str(coordinate[0]),str(coordinate[1])
    return cord
def create_record(azara_record, rui_record):
    if rui_record[1]== get_coordinate(azara_record):
        data=(azara_record[0],azara_record[1],rui_record[0],rui_record[1],rui_record[2])
        return data
    return "not a match"
