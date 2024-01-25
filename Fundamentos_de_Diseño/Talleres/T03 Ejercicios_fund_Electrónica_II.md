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

### **Implementacion del codigo de inicio, conoce el kit**

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


<table style="width: 100%;">
    <tr>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/6e471378-b1a1-4f09-b406-7ed1496d9497" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/c096ac67-c91e-4c43-95f2-16387252dcfb" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
    </tr>
    <tr>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/920b02f7-0772-40e9-85c7-de02e03f0cae" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/ab3a5944-a45a-43f8-9177-873931537b03" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
    </tr>
</table>

**Análisis del resultado:**

<p align="justify">
En dicho ejercicio, lo primero que hicimos fue calcular la resistencia equivalente de manera manual. El resultado fue de 6.6 kΩ, con un valor de 10 kΩ de cada resistencia. Para comparar experimentalmente este resultado, utilizamos un multímetro. El valor obtenido con el multímetro fue de 6.58 kΩ. Por lo tanto, el margen de error es mínimo, de solo 0.02.
</p>

## **Ejercicios nivel  gato 😺**
<table style="width: 100%;">
    <tr>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/f6b045f9-4c19-49c6-a3c3-d3308396b94f" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/2e989a4b-50b1-40e6-bd10-c8e90caa5fc0" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
    </tr>
    <tr>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/cbbe6959-0eb6-400b-b8a8-0324a7c8a4aa" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/05cb33c8-646d-425d-8b66-5e268450554d" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
    </tr>
</table>


**Análisis del resultado:**

<p align="justify">
En dicho ejercicio, se realiza el mismo paso de calcular la resistencia equivalente de manera manual. El resultado fue de 4 kΩ, con un valor de 10 kΩ  de cada resistencia. Para comparar experimentalmente este resultado, utilizamos un multímetro. El valor obtenido con el multímetro fue de 3.924 kΩ. Por lo tanto, el margen de error es mínimo, de solo 0.076.
</p>

## **Ejercicio nivel dragón 🐉**
<table style="width: 100%;">
    <tr>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/152218004/6d683bd7-2c16-4ea8-ad87-bef2b73d7f8f" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/592b2cc9-07b3-472e-a38e-84124a647a7b" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
    </tr>
    <tr>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/67383995-3202-4d2e-9f1d-c5de07df4851" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
        <td style="border: 0px solid #ddd; padding: 3px; text-align: center;">
            <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/f4fe402d-27a8-44c5-b75a-2b0323e470f6" alt="" style="width: 100%; display: block; margin: auto;">
        </td>
    </tr>
</table>


**Análisis del resultado:** 
  
<p align="justif">
En dicho ejercicio, se realiza el mismo paso de calcular la resistencia equivalente de manera manual. El resultado fue de 6.6 kΩ, con un valor de 10 kΩ de cada resistencia. Para comparar experimentalmente este resultado, utilizamos un multímetro. El valor obtenido con el multímetro fue de 6.56 kΩ. Por lo tanto, el margen de error es mínimo, de solo 0.04.
</p>

## **3.2 Circuitos utiles**

**Circuito Divisor de Tensión**
Es un circuito sencillo donde se aplica laley de Ohm, para obtener el voltaje desalida (Vout) reducido en una resistencia.

##  **Primer experimento:**
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/522c7fff-1649-4bf2-87ea-3d283847cef7" width="650px"/>
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/dcf54982-fb7d-4599-8a1a-bfc9e6e8155d" width="300px"/>
</div>

 <p align="center">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/21a2d018-e6b6-4578-81d5-83fefec5875e" alt="Texto Alternativo" width="95%">
</p>

## **Segundo experimento:**

<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/522c7fff-1649-4bf2-87ea-3d283847cef7" width="650px"/>
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/57588192-0016-4237-96ee-bb0aa61db4c9" width="300px"/>
</div>

<p align="center">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/151795724/e869407d-ad67-4893-9ec9-1050bfc78fd5" alt="Texto Alternativo" width="95%">
</p>

**Análisis de resultados del experimento 1 y 2:**
<p align="justify">
En el primer experimento, de acuerdo a la relación de R1 y R2 de 3.54, nos salió teóricamente que R1 debería ser 3.5 kΩ para obtener un vout de 1.1 V. En el cual, después de crear una resistencia que se acercara a dicho valor para reemplazar a R1 y se obtuviera 1.1 V, se realizó una prueba con el multímetro dando como resultado experimental de 1.13 V. Lo que significa que existe una pequeña diferencia de 0.02.
Asimismo, después de tantos intentos, tratamos de realizar otro circuito que cumpliera lo mencionado de aproximarse a 1.1 V de vout. En el cual nos salió una diferencia de -0.006, siendo un error menor a diferencia de otro (valor experimental es 1.094). Sin embargo, en dicho experimento hemos realizado un cambio de la relación que existe entre R1 y R2 para que nos saliera dicho resultado. Lo que significa que estos resultados pueden depender mucho de la relación que existen entre R1 y R2 para obtener un vout deseado.
</p>

## **4. CONCLUSIÓN**

<p align="justify">
En conclusión, el presente laboratorio fue muy importante para nosotros, ya que nos permitió aprender nuevos conceptos de la electrónica que nos servirán como base para crear nuestro prototipo final en nuestro proyecto. En los experimentos, creamos circuitos en el protoboard, lo que requirió de los conceptos aprendidos en el curso de física para ingeniería 3 frente al tema de circuitos. Todos los objetivos del laboratorio se lograron exitosamente.
</p>

