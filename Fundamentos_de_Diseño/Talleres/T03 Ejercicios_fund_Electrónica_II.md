# **🔌 GUÍA N° 4 – EJERCICIOS DE FUNDAMENTOS DE ELECTRÓNICA II⚡** 


##  **1.	MATERIALES Y EQUIPOS 🔎**
- Arduino MKR WiFi 1010
- MKR ioT Carrier
- Módulo Sensor PIR HC-SR501
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/d7dfd454-1959-446f-856f-e0c864d58831" width="200px"/>
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/57b79b31-1503-4609-a39e-f0110b7583ba" width="200px"/>
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/396a10e8-a4a6-4841-b3af-150e245c2099" width="200px"/>
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/ea2c22cc-a651-4332-a26f-b81d5f194868" width="200px"/>
</div>

##  **2.  TEORÍA FUNDAMENTAL 🔎**
<p align="justify">
El Internet de las cosas (IoT) se ha convertido en un catalizador del cambio en la era digital, mejorando nuestra vida diaria con dispositivos inteligentes y conectados; cambiando la forma en que interactuamos con el entorno. Permite conectar objetos físicos con capacidades de comunicación y sensores para crear redes más inteligentes que no solo simplifican las tareas sino que también abren más oportunidades de innovación y eficiencia.
</p>

###  **Importancia del internet de las cosas:**

- *Automatización de procesos:* La capacidad del IoT para automatizar procesos es fundamental, puede liberar tiempo y recursos humanos para iniciativas más estratégicas y creativas.
 
- *Monitoreo remoto:* IoT proporciona información instantánea para tomar decisiones informadas.
 
- *Análisis de decisiones preciso:* IoT no sólo recopila datos sino que también proporciona análisis en profundidad. 
 
- *ahorrar recursos:* Optimizar el uso de recursos como la energía y los materiales es una contribución importante del IoT. 
 
- *Mejorar la seguridad:* el IoT desempeña un papel fundamental a la hora de permitir un control y una protección más eficaces de los dispositivos conectados.


##  **3.	DESARROLLO DE LAS ACTIVIDADES 🔎**

### **Implementación del código de inicio, conoce el kit**

- _**Descripción de la actividad:**_

<p align="justify">
En esta actividad, vamos a realizar la implementación del codigo incial del kit, el cual se base en poder ejercutar correctamente un código correctamente en arduino, el cual permitira obtener la humedad y la temperatura del ambiente y mostrarlo en la pantalla del MKR Iot Carrier, intercalando entre humedad y temperatura al presionar un determinado boton táctil.
</p>

- _**Implementación del código**_
<p align="justify">
Para ejecutar el codigo utilizamos el aplicativo arduino IDE, y lo primero que hicimos fue la instalación de la librería Arduino_MKRIoTCarrier, y posteriormente las incluimos en el código con la siguiente linea de código:</p>

```cpp
#include <AirQualityClass.h>
#include <Arduino_MKRIoTCarrier.h>
#include <Arduino_MKRIoTCarrier_Buzzer.h>
#include <Arduino_MKRIoTCarrier_Qtouch.h>
#include <Arduino_MKRIoTCarrier_Relay.h>
#include <EnvClass.h>
#include <IMUClass.h>
#include <MKRIoTCarrierDefines.h>
#include <PressureClass.h>
```
<p align="justify">
Definimos las variables que se utilizarán, temperature, humidity y carrier, e inicializamos las variables</p>

```cpp
MKRIoTCarrier carrier;
float temperature = 0;
float humidity = 0;
void setup() {
  Serial.begin(9600);
  //Wait to open the Serial monitor to start the program and see details on errors
  
 
  //Set if it has the Enclosure mounted
  CARRIER_CASE = true;
  //Initialize the IoTSK carrier and output any errors in the serial monitor
  carrier.begin();
}
```
<p align="justify">
Creamos las funciones printHumidity() y printTemperature(), en las cuales se define el color de fondo de la pantalla, el color de la fuente, y se imprimirán los datos de temperatura (grados célcius) y humedad (porcentage) en la pantalla</p>

```cpp
void printTemperature() {
  //configuring display, setting background color, text size and text color
  carrier.display.fillScreen(ST77XX_RED); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(6); //large sized text
 
  carrier.display.setCursor(30, 50); //sets position for printing (x and y)
  carrier.display.print("Temp: ");
  carrier.display.setTextSize(4); //decreasing text size
  carrier.display.setCursor(40, 120); //sets new position for printing (x and y)
  carrier.display.print(temperature);
  carrier.display.print(" C");
}
 
void printHumidity() {
  //configuring display, setting background color, text size and text color
  carrier.display.fillScreen(ST77XX_BLUE); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(2); //medium sized text
 
  carrier.display.setCursor(20, 110); //sets position for printing (x and y)
  carrier.display.print("Humi: ");
  carrier.display.print(humidity);
  carrier.display.println(" %");
}
```
<p align="justify">
Por último, en el loop se realiza la lectura de la temperatura y humedad, se genera una impresión en la terminal y en base al boton táctil que presiones cambiará entre humedad y temperatura</p>

```cpp
void loop() {
  // read the sensor values
  temperature = carrier.Env.readTemperature();
  humidity = carrier.Env.readHumidity();
 
  //Update touch buttons
  carrier.Buttons.update();
 
  // print each of the sensor values
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" Â°C");
 
  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");
 
  //function to print out values
  if (carrier.Buttons.onTouchDown(TOUCH0)) {
    printTemperature();
  }
 
  if (carrier.Buttons.onTouchDown(TOUCH3)) {
    printHumidity();
  }
```
- _**Evidencia de desarrollo**_
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/29d9a31f-62f4-44ef-b64c-3bf1b5236a25" width="400px"/>
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/4a2e2200-0305-490e-8779-f8aad7847995" width="400px"/>
</div>

### **Implementación de código para cambiar la escala de la temperatura**

- _**Descripción de la actividad:**_
<p align="justify">
Se harán modificaciones al código anterior para que al momento de hacer click en boton táctil relacionado a la temperatura se cambie la escala de medición de la temperatura, entre celsius, fahrenheit y kelvin.
</p>

- _**Cambios en el código**_
<p align="justify">
Se añadira la variable count que perimirira realizar el cambio en la escala de medición
</p>

```cpp
int count = 0;
```
<p align="justify">
Para realizar el cambio añadiremos condicionales if, elif y else dentro de la función printTemperature(), donde estableceremos, en caso de que count sea 0, este en escala celsius, en caso count sea 1, la escala sea fahrenheit, y en caso no sea ninguno, la escala sea kelvin.
</p>

```cpp
void printTemperature() {
  //configuring display, setting background color, text size and text color
  if (count == 0) {
  carrier.display.fillScreen(ST77XX_RED); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(6); //large sized text
 
  carrier.display.setCursor(30, 50); //sets position for printing (x and y)
  carrier.display.print("Temp: ");
  carrier.display.setTextSize(4); //decreasing text size
  carrier.display.setCursor(40, 120); //sets new position for printing (x and y)
  carrier.display.print(temperature);
  carrier.display.print(" C");
  count++;
  } else if (count == 1){
  carrier.display.fillScreen(ST77XX_RED); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(6); //large sized text
 
  carrier.display.setCursor(30, 50); //sets position for printing (x and y)
  carrier.display.print("Temp: ");
  carrier.display.setTextSize(4); //decreasing text size
  carrier.display.setCursor(40, 120); //sets new position for printing (x and y)
  carrier.display.print(temperature*1.8 + 32);
  carrier.display.print(" F");
  count++;
  } else {
  carrier.display.fillScreen(ST77XX_RED); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(6); //large sized text
 
  carrier.display.setCursor(30, 50); //sets position for printing (x and y)
  carrier.display.print("Temp: ");
  carrier.display.setTextSize(4); //decreasing text size
  carrier.display.setCursor(40, 120); //sets new position for printing (x and y)
  carrier.display.print(temperature + 273);
  carrier.display.print(" K");
  count=0;
  }
}
```

**Análisis de resultados del experimento 1 y 2:**
<p align="justify">
En el primer experimento,
</p>

## **4. CONCLUSIÓN**

<p align="justify">
En conclusión, 
</p>

