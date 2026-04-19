#include <Adafruit_NeoPixel.h>
#define PIN        9 // 信号用のピンを指定
#define NUMPIXELS 5 // LEDの数を指定
int brightness=50;//明るさ

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin(); // NeoPixel出力ピンの初期化
  pixels.setBrightness(brightness);
}

void loop() {
  pixels.clear(); // すべてのLEDの色を0にセット

  for(int i=0; i<NUMPIXELS; i++) {
    int r = random(256);
    int g = random(256);
    int b = random(256);
    pixels.setPixelColor(i, pixels.Color(r, g, b));
    pixels.show();
    delay(70);
  }
}
