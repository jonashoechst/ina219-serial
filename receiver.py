#!/usr/bin/env python3

import time
import serial

SERIAL_PORT = "/dev/cu.SLAB_USBtoUART"
SERIAL_SPEED = 115200
OUTFILE_FORMAT = "ina219_{}.csv"


def reopen_csv():
    csv_path = f"ina219_{int(time.time())}.csv"
    return open(csv_path, "a")


csv_file = reopen_csv()

with serial.Serial(SERIAL_PORT) as s:
    s.baudrate = SERIAL_SPEED
    while True:
        line = s.readline()
        try:
            line = line.decode().strip('\n')
            print(line)
            ms, shunt_mV, bus_V, current_mA, power_mW = line.split(",")
            if not ms.isdigit():
                csv_file.close()
                csv_file = reopen_csv()

            csv_file.write(
                f"{int(ms)/1000},{shunt_mV},{bus_V},{current_mA},{power_mW}\n")
        except UnicodeDecodeError:
            print(line)
        except ValueError:
            pass
