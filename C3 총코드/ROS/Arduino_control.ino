#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define fanPin 7
#define ledPin 2

#define NUMPIXELS 16
Adafruit_NeoPixel pixels(NUMPIXELS, ledPin, NEO_GRB + NEO_KHZ800);

#define DELAYVAL 10

void setup() {

  Serial.begin(9600);


#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
  pixels.begin();


  Serial.flush();
  pinMode(fanPin, OUTPUT);
}

void loop() {

  while(Serial.available() > 0){
    char rp_return = Serial.read();

    // pm > 150 => RED
    if (rp_return == '0'){
      pixels.clear();
    
      for(int i=0; i<NUMPIXELS; i++) {
        pixels.setPixelColor(i, pixels.Color(100, 0, 0));
        pixels.show();
        delay(DELAYVAL);
      }
      
      digitalWrite(fanPin, HIGH);
    }

    // pm < 30 => GREEN
    else if(rp_return == '1'){
      pixels.clear();
    
      for(int i=0; i<NUMPIXELS; i++) {
        pixels.setPixelColor(i, pixels.Color(0, 100, 0));
        pixels.show();
        delay(DELAYVAL);
      }

      digitalWrite(fanPin, LOW);
    }

    // 30 < pm < 150 => YELLOW
    else if(rp_return == '2'){
      pixels.clear();
    
      for(int i=0; i<NUMPIXELS; i++) {
        pixels.setPixelColor(i, pixels.Color(100, 100, 0));
        pixels.show();
        delay(DELAYVAL);
      }
    
      digitalWrite(fanPin, HIGH);
    }

  }

}