import serial
import time

rfid2des = {
    "fc 87 a1 5a": "R1",
    "5c 26 a1 5a": "R2",
    "7c 01 a1 5a": "K1",
    "9c bf 92 5a": "K2",
    "dc e2 8b 5a": "Q1",
    "3c a1 92 5a": "Q2",
}

board_mapping = [
    [],
    [5, 1, 4],
    [2, 0, 3],
]
class chess_piece:
    def __init__(self,rfid):
        self.rfid = rfid
        self.description = rfid2des[rfid]
        self.image = ""


def read_input(input):
    output = [[None for _ in range(3)] for _ in range(3)]
    ls = input.split(",")
    for i in range(len(output)):
        for j in range(len(output[0])):
            output[i][j] = chess_piece(ls[i*3+j])
    return output

    

arduino = serial.Serial(port='/dev/cu.usbmodem144201', baudrate=115200, timeout=.1)
def write_read():
    time.sleep(0.05)
    data = arduino.readline().decode()
    return data
while True:
    value = write_read()
    print(value) # printing the value

# print(read_input("7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A,7C 01 A1 5A"))

from PIL import Image, ImageFont, ImageDraw

im = Image.new('RGB', (300,300), (255,255,255))
dr = ImageDraw.Draw(im)
        # dr.rectangle(((0+(j)*100,0+(j)*100),(100+(j)*100, 100+(j)*100)), fill="blue", outline = "black")
for i in range(0,3):
    for j in range(0,3):
        # print([(0+i*100,0+j*100),(100+i*100,100+j*100)])
        dr.rectangle([(0+j*100,0+i*100),(100+j*100,100+i*100)], fill="white", outline = "black")
        img = Image.open("ChessSet.jpeg")
        img.thumbnail((100,100))
        im.paste(im=img,box=(0+j*100,0+i*100))
im.show()