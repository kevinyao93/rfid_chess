#include <SPI.h>
#include <MFRC522.h>
#define SS_PIN 53
#define RST_PIN 49
#define SS_PIN_2 25

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522 mfrc522_2(SS_PIN_2, RST_PIN);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
  mfrc522_2.PCD_Init();
  Serial.println("RFID reading UID");
}

void loop() {
  // put your main code here, to run repeatedly:
  if(mfrc522.PICC_IsNewCardPresent()){
    Serial.println("In card present");
    if (mfrc522.PICC_ReadCardSerial()) {
      Serial.print("Tag UID:");
      for (byte i = 0; i < mfrc522.uid.size; i++){
        Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(mfrc522.uid.uidByte[i], HEX);
      }
      Serial.println();
      mfrc522.PICC_HaltA();
    }
  }
  if(mfrc522_2.PICC_IsNewCardPresent()){
    Serial.println("In card present");
    if (mfrc522_2.PICC_ReadCardSerial()) {
      Serial.print("Tag UID:");
      for (byte i = 0; i < mfrc522_2.uid.size; i++){
        Serial.print(mfrc522_2.uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(mfrc522_2.uid.uidByte[i], HEX);
      }
      Serial.println();
      mfrc522_2.PICC_HaltA();
    }
  }
}
