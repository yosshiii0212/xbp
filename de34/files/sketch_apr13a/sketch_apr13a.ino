const int stepPin = 9;
const int dirPin = 8;
const int sensorPin = A0;

int sensorValue = 0;
int threshold = 800;  // ←ここは実際に調整する

bool stopped = false;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  digitalWrite(dirPin, HIGH); // 回転方向固定

  Serial.begin(6000);
}

void loop() {
  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);

  if (!stopped) {
    // 回転処理
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(800);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(750);

    // センサー判定
    if (sensorValue > threshold) {
      stopped = true;

      // 徐々に止める（ルーレット感）
      for (int d = 800; d < 3000; d += 50) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(d);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(d);
      }
    }
  }
}