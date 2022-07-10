#include "FastLED.h"
#include <EEPROM.h>

#define size_column 5
#define size_row 8
#define gap 3
#define curve 3
#define NUM_LEDS size_column*size_row + (size_column-1)*gap*size_row + (size_row-1)*(gap+curve)

#define DATA_PIN 6

#define X  0x000000 //Black (OFF)
#define W  0xFFFFFF //White
#define Y  0xFFFF00 //Yellow
#define G  0x008000 //Green
#define R  0xFF0000 //Red
#define B  0x0000FF //Blue
#define V  0xFF00FF //Pink
#define O  0x9400D3 //Purpol

CRGB leds[NUM_LEDS];

int potenciometro = A5;
int velocidade = 100;
int x = 0;
int minima = 0;
int maxima = 1500;
int index_row = 0;


unsigned long instanteDaContagem1 = 0;
unsigned long instanteDaContagem2 = 0;

unsigned long posicao[NUM_LEDS] = {};


void writeStringToEEPROM(int addrOffset, const String &strToWrite)
{
  byte len = strToWrite.length();
  EEPROM.write(addrOffset, len);
  for (int i = 0; i < len; i++)
  {
    EEPROM.write(addrOffset + 1 + i, strToWrite[i]);
  }
}
String readStringFromEEPROM(int addrOffset)
{
  int newStrLen = EEPROM.read(addrOffset);
  char data[newStrLen + 1];
  for (int i = 0; i < newStrLen; i++)
  {
    data[i] = EEPROM.read(addrOffset + 1 + i);
  }
  data[newStrLen] = '\ 0'; // !!! NOTE !!! Remove the space between the slash "/" and "0" (I've added a space because otherwise there is a display bug)
  return String(data);
}


void setup() {

  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  FastLED.setBrightness(80);
  Serial.begin(9600);
  Serial.setTimeout(10);
  
  String retrievedString = readStringFromEEPROM(0);
  Serial.print("The String we read from EEPROM: ");
  Serial.println(retrievedString);

  pinMode(potenciometro, INPUT);

  for (int i = 0; i < NUM_LEDS; i++) {
    posicao[i] = W;
  }
  FastLED.show();
}

void loop() {

  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = posicao[i];
  }

  if (Serial.available() > 0) {
    String texto = Serial.readStringUntil('\n');
    texto.trim();
   
    writeStringToEEPROM(0, texto);
    /*
      if (texto.substring(0, 6) == "minima:") {
      minima = texto.substring(7);
      Serial.println("Minima recebido: " + minima);
      }
      if (texto.substring(0, 6) == "maxima:") {
      maxima = texto.substring(7);
      Serial.println("Maxima recebido: " + maxima);
      }
    */
    
    if (texto.substring(0, 8) == "posicao:") {
      memset(posicao, W, sizeof(posicao));
      String posicao_text = texto.substring(8);
      
      Serial.println("posicao:" + posicao_text);
      int posicao_len = posicao_text.length();

      int index_leds = 0;
      for (int i = 0; i < posicao_len; i++) {

        char letra = texto.charAt(8 + i);
        Serial.println(letra);

        if (letra == 'X') {
          posicao[index_leds] = X;
        }
        else if (letra == 'W') {
          posicao[index_leds] = W;
        }
        else if (letra == 'Y') {
          posicao[index_leds] = Y;
        }
        else if (letra == 'G') {
          posicao[index_leds] = G;
        }
        else if (letra == 'R') {
          posicao[index_leds] = R;
        }
        else if (letra == 'B') {
          posicao[index_leds] = B;
        }
        else if (letra == 'O') {
          posicao[index_leds] = O;
        }
        index_leds = index_leds + gap+1;
        if ((i + 1) % size_column == 0) {
          index_leds = index_leds + curve;
        }
      }
    }
  }

  unsigned long instanteAtual = millis();

  if (instanteAtual > instanteDaContagem2 + velocidade) {
    FastLED.clear();
    if (index_row > NUM_LEDS) {
      index_row = 0;
    }
    else {

      for (int i = 0; i < size_column; i++) {
        if (i + index_row < NUM_LEDS) {
          leds[i + index_row] = posicao[i + index_row];
        }
        index_row = index_row + gap;
        if ((i + 1) % size_column == 0) {
          index_row = index_row + curve;
        }
      }
      index_row = index_row + size_column;
      FastLED.show();
    }
    instanteDaContagem2 = instanteAtual;
  }

  if (instanteAtual > instanteDaContagem1 + 50) {
    int valorLido = analogRead(potenciometro);
    int valorFinal = map(valorLido, 0, 1023, minima, maxima);
    velocidade = valorFinal;
    //Serial.println(velocidade);
    instanteDaContagem1 = instanteAtual;
  }
}
