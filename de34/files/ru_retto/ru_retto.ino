const int cdsPin = A0;      
const int stepPin = 9;     
const int dirPin = 8;      

const int threshold = 760; 

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int lightValue = analogRead(cdsPin);

  if (lightValue < threshold) {
    // 1. 暗い間は通常速度で回転
    while (analogRead(cdsPin) < threshold) {
      stepMotor(1000); 
    }

    // 2. 長い時間をかけて減速（スローダウン）
    Serial.println("Long slowing down...");
    
    // speed（待ち時間）を 1000 から 8000 まで、10ずつじわじわ増やす
    // この数値を大きくするほど、停止までの時間が長くなります
    for (int speed = 1000; speed < 8000; speed += 10) {
      stepMotor(speed); 
    }
    
    Serial.println("Complete stop.");
  }
  
  delay(100);
}

void stepMotor(int delayTime) {
  digitalWrite(dirPin, HIGH);
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(delayTime);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(delayTime);
}