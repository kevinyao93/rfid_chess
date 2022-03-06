#include <SPI.h>
#include <MFRC522.h>
#define RST_PIN 49
#define SS_PIN_1 29
#define SS_PIN_2 37
#define SS_PIN_3 33
#define SS_PIN_4 35
#define SS_PIN_5 43
#define SS_PIN_6 31    
#define SS_PIN_7 41
#define SS_PIN_8 53
#define SS_PIN_9 39

byte ssPins[] = {SS_PIN_1, SS_PIN_2, SS_PIN_3, SS_PIN_4, SS_PIN_5, SS_PIN_6, SS_PIN_7, SS_PIN_8, SS_PIN_9};

byte readedCard[9][4];
MFRC522 mfrc522[9];

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  Serial.begin(115200);
  SPI.begin();
  for (uint8_t reader = 0; reader < 9; reader++) {
    mfrc522[reader].PCD_Init(ssPins[reader], RST_PIN);
  }
  pinMode(RST_PIN, OUTPUT);
  digitalWrite(RST_PIN, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  String output_arr = "";
  for (uint8_t reader = 0; reader < 9; reader++){
    if(getRFID(reader)) {
      output_arr.concat(printUID(readedCard[reader]));
    } else {
      output_arr.concat("0");
    }
    if (reader < 9) {
      output_arr.concat(",");
    }
  }
  Serial.println(output_arr);
}

String printUID(byte *buffer){
  String id = "";
  for (byte i = 0; i < 4; i++) {
    id.concat(buffer[i] < 0x10 ? " 0" : " ");
    id.concat(String(buffer[i], HEX));
  }
  return id;
}

bool getRFID(byte readern)
{
  bool isPICCpresent = false;
  digitalWrite(RST_PIN, HIGH);   // Get RC522 reader out of hard low power mode
  mfrc522[readern].PCD_Init();   // Init the reader

  if (mfrc522[readern].PICC_IsNewCardPresent() && mfrc522[readern].PICC_ReadCardSerial())
    {
     memcpy(readedCard[readern], mfrc522[readern].uid.uidByte, 4); 
     isPICCpresent = true;
    }
  mfrc522[readern].PICC_HaltA();
  mfrc522[readern].PCD_StopCrypto1();
  digitalWrite(RST_PIN, LOW);    // return to hard low power mode
  return isPICCpresent;          // returns TRUE if PICC is detected, false if not
}
