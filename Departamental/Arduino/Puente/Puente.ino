int motorENA = 4;
int motorIN1 = 5;
int motorIN2 = 6;
int sensorPIR = 7;
int sensorLDR = A0;
int pinRelevador = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(motorIN1, OUTPUT);
  pinMode(motorIN2, OUTPUT);
  pinMode(pinRelevador, OUTPUT);
  pinMode(sensorPIR, INPUT_PULLUP);
}

int valorPIR;
int valorLDR;

void loop() {
  // put your main code here, to run repeatedly:
  valorPIR = digitalRead(sensorPIR);
  if(valorPIR > 100) {
    int valorModulo = valorPIR % 3;
    if (valorModulo == 0) {
      Serial.println("Detenerse");
      digitalWrite(motorIN1, LOW);
      digitalWrite(motorIN2, LOW);
      analogWrite(motorENA, 0);
    } else if (valorModulo == 1) {
      Serial.println("Girar Izquierda");
      digitalWrite(motorIN1, LOW);
      digitalWrite(motorIN2, HIGH);
      analogWrite(motorENA, 255);
    } else if (valorModulo == 2) {
      Serial.println("Girar Derecha");
      digitalWrite(motorIN1, HIGH);
      digitalWrite(motorIN2, LOW);
      analogWrite(motorENA, 255);
    }
  }
  
  valorLDR = analogRead(sensorLDR);
  if(valorLDR > 500) {
    digitalWrite(pinRelevador, valorLDR);
    Serial.println("Estado : " + String(valorLDR));
  }

  delay(2000);
}
