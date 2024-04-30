import serial

ser = serial.Serial('COM3',9600)

while True:
    line = ser.readline().decode().strip()

    values = line.split(",")

    humidity = int(values[0])
    temp = int(values[1])


    print("Temp :", temp)
    print("Humidity :", humidity)


























