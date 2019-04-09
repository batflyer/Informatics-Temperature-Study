// Copyright © 2019 Alexander L. Hayes
// MIT License

/*****
========
main.ino
========

Alexander L. Hayes (https://hayesall.com/)

This is the main file that Experiments 1 & 2 were ran for Rob Long's
"Temperature Sensing with Arduino" activity.

Data are printed to the Serial Monitor, and will maintain a format
similar to the following:

.. code-block:: csv

  Time,TemperatureF
  0,73.06
  2,73.18
  4,73.18
  5,73.18

For an example, refer to the contents of the ``data/`` directory.
******/

#include "Wire.h"
#include "SparkFunTMP102.h"

TMP102 sensor0(0x48);
int startTime = 0;

void setup() {
	Serial.begin(9600);
	sensor0.begin();
	sensor0.setConversionRate(0);

	Serial.println("Time,TemperatureF");
}

void loop() {

	float temperature;

	sensor0.wakeup();
	temperature = sensor0.readTempF();

	Serial.print(startTime);
	Serial.print(",");
	Serial.println(temperature);

	sensor0.sleep();

	delay(2000);
	startTime += 2;
}
