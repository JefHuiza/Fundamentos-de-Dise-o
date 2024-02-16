// Definir los pines para el caudalímetro y la alarma
#define CAUDALIMETRO_PIN 2
#define ALARMA_PIN 8
int valvula = 9;
bool fuga = false;

// Definir el umbral de flujo para detectar una fuga
// Este valor debería ser ajustado según las especificaciones del caudalímetro y las condiciones de la tubería

// Variable para almacenar el estado anterior del caudalímetro
volatile unsigned int flujo_anterior = 0;

void setup() {
  // Inicializar el caudalímetro y la alarma
  Serial.begin(9600);d:\Descargas\el-guardián-del-agua_-sistema-de-detección-de-fugas-y-consumo-portenta-h7-v4\firmware-arduino-portenta-h7.ino.bin
  pinMode(CAUDALIMETRO_PIN, INPUT);
  pinMode(ALARMA_PIN, OUTPUT);
  digitalWrite(ALARMA_PIN, LOW); // Apagar la alarma inicialmente
  pinMode(valvula, OUTPUT);
  // Adjuntar la interrupción al pin del caudalímetro
  attachInterrupt(digitalPinToInterrupt(CAUDALIMETRO_PIN), leerFlujo, RISING);
}

void loop() {
  // No se necesita hacer nada en el bucle principal, la detección de fugas se maneja en la interrupción
}

// Función de interrupción para leer el flujo del caudalímetro
void leerFlujo() {
  unsigned int flujo_actual = pulseIn(CAUDALIMETRO_PIN, HIGH); // Medir la duración del pulso del caudalímetro
  if (!fuga){
  if (flujo_actual < 38000 && flujo_actual >= 36000) {
    // Si el flujo actual está por debajo del umbral y el flujo anterior estaba por encima del umbral, activar la alarma
    digitalWrite(valvula, HIGH);
    digitalWrite(ALARMA_PIN, HIGH);
    Serial.println("¡Fuga detectada!");
    delay(500000);
    digitalWrite(ALARMA_PIN, LOW);

    
    fuga = true;
  } else {
    // Si no se detecta una fuga, asegúrate de que la alarma esté apagada
    digitalWrite(valvula, LOW);
    Serial.println("¡Fuga no!");

  }
  Serial.println(flujo_actual);
  flujo_anterior = flujo_actual; // Actualizar el valor del flujo anterior
  }
  }
