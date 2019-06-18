import json

# Create a vector with JSON
def open_data():
    with open('dataehealth.json', 'r') as json_file:
        ehealth_data = json.load(json_file)
        if (ehealth_data == None):
            print('Error: JSON could not load ...')
        else:
           print('Sucess: data loaded!')
    return ehealth_data

# Show the data by Name
def show_data_by_name(name, json_data):
    data = []
    for i in json_data:
        data.append(i[name])
    print(data)




