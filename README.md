# rfid_chess
 
## 3d Printed parts
### 4x corner.stl
### 4x edge.stl
### 1x center.stl
### 1x boxes.stl
### 2x King.stl
### 2x Queen.stl
### 2x Roco2.stl

## Arduino Hardware
### Connect Arduino Mega to breadboard, and all 9 RFID sensors
### Add stickers to bottom of 3D printed chess pieces

## Arduino Code
### Refractor Arduino code, condense all of the sensors (Send rfid and sensor id)

Output -> to python
3x3 matrix of rfid's
[[rfid][rfid][rfid]]
[[rfid][rfid][rfid]]
[[rfid][rfid][rfid]]


## Python Visualization Code
### Take in sensor id and rfid code, map each code to the corresponding piece/object
### Display a simple visual matrix for the chessboard and chess pieces
class chess_piece:
    rfid - designation
    description - (K1, K2, Q1, Q2, R1, R2)
    image - ""

Read function
Input 
[[rfid][rfid][rfid]]
[[rfid][rfid][rfid]]
[[rfid][rfid][rfid]]

Output 
[[chess object][chess object][chess object]]
[[chess object][chess object][chess object]]
[[chess object][chess object][chess object]]



## 