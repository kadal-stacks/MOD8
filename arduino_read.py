import serial
import csv
import time
import os

port = '/dev/serial0'
baud = ...
filename = '/home/raspi5/....csv'
os.makedirs(os.path.dirname(filename), exist_ok=True)

ser = serial.Serial(port, baud, timeout=1)
time.sleep(2)  
ser.write(b'...')
print("Arduino ADC Start")

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ADC Value"])
    print(f"Logging to {filename}. Press Ctrl+C to stop.")

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='replace').strip()
                if line:
                    writer.writerow([line])
                    file.flush()
                    print(line)
            time.sleep(0.05)

    except KeyboardInterrupt:
        ser.write(b'...')
        time.sleep(0.5)
        print("Arduino ADC Stop")
    finally:
        ser.close()
