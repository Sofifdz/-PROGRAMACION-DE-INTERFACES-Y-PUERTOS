#include "Servo.h"   

int pinServoMotor = 9;
int pinSensorPIR = 4;
Servo motorServo; 

void setup() { 
  Serial.begin(9600);
  Serial.setTimeout(10);
  motorServo.attach(pinServoMotor);
  pinMode(pinSensorPIR, INPUT_PULLUP);
}
 
int valorSensorPIR;
void loop() {
  valorSensorPIR = digitalRead(pinSensorPIR);
  if (valorSensorPIR > 100) {
    motorServo.write(valorSensorPIR);
    Serial.println("Movimiento detectado, se está moviendo el Servo");
    delay(2000);
    Serial.println("Esperando movimiento...");
  }
  delay(1000);
}
