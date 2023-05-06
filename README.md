# OrgasmTracker

OrgasmTracker is a project for monitoring and tracking physiological reactions during orgasm using a Raspberry Pi, various sensors, and actuators. This project aims to collect data to better understand the physiological mechanisms involved during orgasm, explore the potential for personalized sexual health and wellness applications, and create interactive experiences using actuators that respond to sensor data.

## Sensors and Components

The following sensors are used to track physiological variables during orgasm:

1. Heart rate
   - Sensor: Pulse Sensor Amped
   - Components: Dupont Cables (female-female)
   - Measurement locations: Wrist, fingertips, or earlobe

2. Body temperature
   - Sensor: DS18B20
   - Components: Dupont Cables (female-female), Pull-up resistor (4.7 kΩ)
   - Measurement locations: Skin (arm, leg, forehead, neck) or mucous membranes (entrance of the vagina)

3. Skin conductance
   - Sensor: Grove GSR
   - Components: Dupont Cables (female-female), Analog-to-digital converter (ADC) - ADS1115
   - Measurement locations: Fingers, palms, or soles (areas with high concentration of sweat glands)

4. Muscle tension
   - Sensor: MyoWare Muscle Sensor
   - Components: Dupont Cables (female-female), Analog-to-digital converter (ADC) - ADS1115
   - Measurement locations: Pelvic muscles, abdominal muscles, thigh muscles (adductors), buttocks (glutes), calves

5. Blood flow
   - Sensor: Doppler ultrasound sensor (dedicated for measuring blood flow)
   - Components: Dupont Cables (female-female)
   - Measurement locations: Near genitalia, breasts, or other areas where increased blood flow is expected during orgasm

6. Anal contraction measurement
   - Sensor: Pressure sensor (stainless steel, output signal type: Analog sensor, Accuracy: 1%FS, thread: G1/4")
   - Components: Dupont Cables (female-female)
   - Measurement locations: Inside the anal canal (with the subject's consent and proper sterilization of the sensor)

## Raspberry Pi GPIO Pin Connections

The sensors are connected to the Raspberry Pi using GPIO pins. The specific pin connections for each sensor are detailed in the project documentation.

## Actuators

Actuators are used to create an interactive experience based on the data collected from the sensors. Examples of actuators that can be used in this project include vibrators, electrostimulation devices, and other devices that can provide tactile feedback or stimulation. The actuators can be controlled using the Raspberry Pi, with their behavior determined by the sensor data.

## Data Collection and Analysis

The OrgasmTracker collects data from each sensor during the course of an orgasm. This data can be stored locally on the Raspberry Pi or transmitted to a remote server for further analysis. By examining the collected data, researchers and individuals can gain insights into the physiological processes occurring during orgasm and potentially develop personalized, data-driven sexual experiences using the actuators.
