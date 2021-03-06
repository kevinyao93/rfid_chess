import serial
import time

from multiprocessing import Process, Manager, Pool
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np

class ChessPiece:
    def __init__(self,rfid, description, image):
        self.rfid = rfid
        self.description = description
        self.image = image

rfid2des = {
    "fc 87 a1 5a": ChessPiece("fc 87 a1 5a", "R1", "images/rook_1.png"),#
    "5c 26 a1 5a": ChessPiece("5c 26 a1 5a", "R2", "images/rook_2.png"),#
    "7c 01 a1 5a": ChessPiece("7c 01 a1 5a", "K1", "images/white_king_1.png"),#"K1",
    "9c bf 92 5a": ChessPiece("9c bf 92 5a", "K2", "images/white_king_2.png"),#"K2",
    "dc e2 8b 5a": ChessPiece("dc e2 8b 5a", "Q1", "images/queen_1.png"),#"Q1",
    "3c a1 92 5a": ChessPiece("3c a1 92 5a", "Q2", "images/queen_2.png"),#"Q2",
}


def concat_vh(list_2d):
    
      # return final image
    return cv2.vconcat([cv2.hconcat(list_h) 
                        for list_h in list_2d])
      

def write_read():
    arduino = serial.Serial(port='/dev/cu.usbmodem144201', baudrate=115200, timeout=.1)
    while True:
        data = arduino.readline().decode()
        board_layout = []
        if len(data) > 1:
            data_array = data.split(',')
            board_layout.append(data_array[0: 3])
            board_layout.append(data_array[3: 6])
            board_layout.append(data_array[6: 9])

            blank_image = np.full([200, 200, 3], 255, dtype=np.uint8)    
            rect = cv2.rectangle(blank_image, (0, 0), (200, 200), (0, 0, 0), 5)
            images = [[rect for _ in range(3)] for _ in range(3)]

            for i in range(0,3):
                for j in range(0,3):
                    rfid = board_layout[i][j].lstrip(' ')
                    if rfid == '0':
                        images[i][j] = rect
                    else:
                        chess_piece = rfid2des[rfid]
                        bordersize = 11
                        im = cv2.imread(chess_piece.image)
                        row, col = im.shape[:2]
                        bottom = im[row-2:row, 0:col]
                        mean = cv2.mean(bottom)[0]
                        border = cv2.copyMakeBorder(
                            im,
                            top=bordersize,
                            bottom=bordersize,
                            left=bordersize,
                            right=bordersize,
                            borderType=cv2.BORDER_CONSTANT,
                            value=[0, 0, 0, 0]
                        )
                        section = cv2.resize(border, (200, 200))
                        images[i][j] = section
            
            img_tile = concat_vh(images)
            cv2.imshow('image', img_tile)
            cv2.waitKey(1)

if __name__ == "__main__":
    write_read()

