#include "HX711.h"

HX711 scale;

void setup() {
  Serial.begin(38400);
  // parameter "gain" is ommited; the default value 128 is used by the library
  // HX711.DOUT  - pin #A1
  // HX711.PD_SCK - pin #A0
  scale.begin(A1, A0);
}

void loop() {
  Serial.println(scale.read_average(5));

}
