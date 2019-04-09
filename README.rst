.. raw:: html

  <p align="center">
    <h1 align="center">How Hot is the IU School of Informatics? A Temperature Sensing Study</h1>

    <h3 align="center">🔥🔥🔥</h3>
  </p>
  <p align="center">
    <img src="https://github.com/batflyer/Informatics-Temperature-Study/blob/master/docs/image/redboard/redboard.jpg" width="50%" />
  </p>

What are some of the challenges of sensing temperature in both indoor and
outdoor environments? We will attempt to peer into some of the challenges
over the next five steps. Each step will involve recording the temperature
while either performing an activity or going to a location around the Informatics Building.

This short study was proposed by Rob M. Long for a Methods Activity as part of
`Professor James Clawson's <https://jamesclawson.com/>`_ *"Field Deployments"*
course.

Instructions
------------

**First Run:**

Manually record the start and end time for each event.

1. *ProHealth Office:*

  * Let the sensor collect data for five minutes while sitting at your desk.
  * Copy and paste your data.

2. *Outside:*

  * Exit Informatics East through the north-east connector space door.
  * Walk around the building (moving left through the parking lot) and stop in the courtyard.
  * Sit at a bench for three minutes.
  * Walk inside, stop recording, and copy and paste your data.

3. *A Classroom:*

  * Find an empty classroom. Record the room temperature for one minute.
  * Turn off the lights in the room for two minutes.
  * Turn the lights back on and continue recording for one more minute.
  * Stop recording, copy and paste your data.

4. *The Break Room:*

  * Turn on the sensor and record for one minute.
  * Place the sensor inside the fridge (or freezer) for three minutes.
  * Remove the sensor, copy and paste your data.

5. *The Random Walk:*

  * Start recording from the Informatics East Lobby.
  * Walk around the building for about five minutes, record where you go.

**Second Run:**

Repeat steps 2 & 3. This time: increase the delay time to ten seconds.

.. code-block:: C

  void loop() {
    // --snip--
    delay(10000);
    startTime += 10;
  }

Methods
-------

This activity requires a
`"SparkFun Digital Temperature Sensor Breakout TMP102" <https://www.sparkfun.com/products/13314>`_
for measuring temperature, a `"SparkFun RedBoard" <https://www.sparkfun.com/products/13975>`_,
a breadboard, and a five wires.

One limitation is that all results are printed to the Serial Monitor. This
means that a laptop will need to be carried to provide power and collect
results.

The following schematic shows how to wire the sensor to the board.

.. raw:: html

  <img src="https://github.com/batflyer/Informatics-Temperature-Study/blob/master/docs/svg/schematic.svg?sanitize=true" />

The wires do not need to be the exact same colors. The labels are included so
they can match the colors used here:

.. raw:: html

  <p align="center">
    <img width="40%" src="https://github.com/batflyer/Informatics-Temperature-Study/blob/master/docs/image/redboard/board.jpg" /> <img width="40%" src="https://github.com/batflyer/Informatics-Temperature-Study/blob/master/docs/image/redboard/sensor.jpg" />
  </p>

Results
-------

Data are contained in the ``data/`` directory, split into ``data1.txt`` and
``data2.txt``. The first contains steps 1-5, and the second contains steps
2-3 when they were repeated with higher delay time.

``data1.txt`` uses a 2-second delay time. ``data2.txt`` uses a 10-second
delay time.

``src/plot_data.py`` can be used to plot temperature vs. an integer.

* The integers displayed on the x-axis represent the number of seconds after
  ``12:00:02`` for the first set, and the number of seconds after ``12:31:30``
  for the second set.
* Since the temperatures and the dynamics were more of interest than the
  actual times, the timestamps are left in the raw form.
* The y-axis represents the temperature in degrees Fahrenheit, and the label
  specifies which activity the temperatures correspond to.

.. raw:: html

  <p align="center">
    <img src="https://github.com/batflyer/Informatics-Temperature-Study/blob/master/docs/image/temperature_graphs.png" />
  </p>
