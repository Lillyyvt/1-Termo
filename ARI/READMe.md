╔═══════════════════════════════════════╗ 
║ 🎸 AULAS DE ARQUITETURA DE IOT 🎸    ║ 
║ Arduino/C++/Python - Prática!         ║ 
╚═══════════════════════════════════════╝
## AULA 1: ARDUINO - HARDWARE BASE**
### **Objetivo**: Conhecer placa + primeiros blinks

🛠️ COMPONENTES: ├── 📟 Arduino UNO R3 ├── 🔌 Cabo USB AB ├── 💡 LED + Resistor 220Ω └── 🧵 Protoboard + Jumpers

🔌 PINOS:

Digital: 0-13

Analógico:
A0-13

PWM:
~3,5,6,9,10,11

Alimentação:
5V/3,3V/GND


# 　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

Copiar código

### **PRIMEIRO CÓDIGO - BLINK**
```cpp
// 🌟 Blink LED - Aula 1
void setup() {
  pinMode(13, OUTPUT);  // LED interno
}

void loop() {
  digitalWrite(13, HIGH);  // Liga
  delay(1000);             // 1s
  digitalWrite(13, LOW);   // Desliga
  delay(1000);
}

# 　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

#AULA 2: C++ ARDUINO - ESTRUTURAS BÁSICAS
🎷 Variáveis ​​+ Entrada/Saída
cpp

Copiar código
int sensorPin = A0;    // Pino analógico
int ledPin = 9;        // PWM
int valor = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  valor = analogRead(sensorPin);  // 0-1023
  int brilho = map(valor, 0, 1023, 0, 255);
  
  analogWrite(ledPin, brilho);
  Serial.println(valor);
  delay(100);
}

# 　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

#EstruturasDeControle
cpp

Copiar código
// IF/ELSE + FOR
void loop() {
  int temp = analogRead(A0);
  
  if(temp > 500) {
    digitalWrite(13, HIGH);  // Alerta
  } else {
    digitalWrite(13, LOW);
  }
  
  // FOR - Piscar 5x
  for(int i = 0; i < 5; i++) {
    digitalWrite(8, HIGH);
    delay(200);
    digitalWrite(8, LOW);
  }
}

#　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

#AULA 3: PYTHON - GATEWAY IoT

# pip install paho-mqtt pyserial pandas matplotlib
import paho.mqtt.client as mqtt
import serial
import json
import time
🔗 CLIENTE MQTT EM PYTHON
Python

Copiar código
# 🌡️ Leitor Serial + MQTT
import serial
import paho.mqtt.client as mqtt

arduino = serial.Serial('COM3', 9600)
client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    linha = arduino.readline().decode('utf-8')
    dados = {"temperatura": float(linha)}
    client.publish("casa/sala/temp", json.dumps(dados))
    time.sleep(1)

#　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

#AULA 4: SENSOR DHT22 - COMPLETO
C++ ARDUINO
cpp

Copiar código
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float umid = dht.readHumidity();
  
  Serial.print("T:");
  Serial.print(temp);
  Serial.print(",H:");
  Serial.println(umid);
  delay(2000);
}

#RECEPTORPYTHON
Python

Copiar código
import serial
ser = serial.Serial('COM3', 9600)

while True:
    linha = ser.readline().decode()
    if "T:" in linha:
        temp = float(linha.split("T:")[1].split(",")[0])
        print(f"🌡️ {temp:.1f}°C")

#　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

#AULA 5: NODE-RED + PAINEL DE CONTROLE

Copiar código
🔄 FLUXO NODE-RED:
📡 MQTT IN --> 🔄 Function --> 📊 Gauge
     "casa/temp"     if > 30     Temp Atual

📊 DASHBOARD:
├── 📈 Gráfico Temperatura
├── ⚡ Status Online/Offline
└── 🎚️ Controle LED Remoto

# ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

##REFERÊNCIASRÁPIDAS
cpp

Copiar código
// ARDUINO CHEAT SHEET
pinMode(pin, OUTPUT/INPUT)
digitalWrite(pin, HIGH/LOW)
analogRead(pin)     // 0-1023
analogWrite(pin, 0-255)
delay(ms)
Serial.println(valor)
Python

Copiar código
# PYTHON IOT CHEAT SHEET
import paho.mqtt.client as mqtt
client.connect("broker", 1883)
client.publish("topico", "payload")
ser = serial.Serial('COM3', 9600)
ser.readline()

╔══════════════════════════════════════╗
║   ARQUITETURA IoT - AULAS PRONTAS    ║
║  ☀️ Arduino C++ + Python Gateway ☀️ ║
║ 🎸 Hands On - Sunset Architecture 🎸║
╚══════════════════════════════════════╝