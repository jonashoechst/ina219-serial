#undef __APPLE__

#include <Adafruit_INA219.h>
#include <Arduino.h>

#define INTERVAL_MS 100

Adafruit_INA219 ina219;

void setup() {
    Serial.begin(115200);
    Serial.println("ms,shunt_mV,bus_V,current_mA,power_mW");

    ina219.begin();
}

unsigned long time_ms;
float shunt_mV;
float bus_V;
float current_mA;
float power_mW;

void loop() {
    time_ms = millis();
    shunt_mV = ina219.getShuntVoltage_mV();
    bus_V = ina219.getBusVoltage_V();
    current_mA = ina219.getCurrent_mA();
    power_mW = ina219.getPower_mW();

    Serial.printf("%lu,%5.3f,%f,%f,%f\n", time_ms, shunt_mV, bus_V, current_mA,
                  power_mW);

    delay((time_ms + INTERVAL_MS) - millis());
}