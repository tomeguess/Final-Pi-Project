# a file that allows the gui to store different plant information 
# and allows the user to permanently add a plant to the list

# Dictionary to store plant information
plants= {}

def changePlant(plants):

    # Ask user for the plant name
    plantName = input("Enter the name of the plant you would like to use: ")

    # Check if the plant already exists in the dictionary
    if plantName in plants:
        return plants
    else:
        # Ask for ideal temperature, soil moisture level, and humidity
        idealTemperature = input("Enter the ideal temperature for the plant: ")
        soilMoisture = input("Enter the ideal soil moisture level for the plant: ")
        idealHumidity = input("Enter the ideal humidity for the plant: ")

        # Store plant information in the dictionary
        plants[plantName] = {'idealTemperature': idealTemperature,
                             'soilMoisture': soilMoisture,
                             'humidity': idealHumidity}
        return plants


