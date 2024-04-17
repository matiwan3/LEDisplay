import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the LED panel
# Modify these pin numbers based on your actual connections
A, B, C, D = 23, 24, 25, 8
CLK, LAT, OE, R1, G1, B1, R2, G2, B2 = 11, 10, 9, 17, 22, 27, 5, 6, 13

# Set up GPIO pins
GPIO.setup([A, B, C, D, CLK, LAT, OE, R1, G1, B1, R2, G2, B2], GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all_leds():
    GPIO.output(LAT, GPIO.LOW)  # Pull latch low
    GPIO.output(OE, GPIO.LOW)   # Enable output (active low)

    # Shift in zeros to turn off all LEDs
    for _ in range(32 * 64):
        GPIO.output(CLK, GPIO.HIGH)
        GPIO.output(CLK, GPIO.LOW)

    GPIO.output(LAT, GPIO.HIGH)  # Pulse the latch to commit the data
    GPIO.output(LAT, GPIO.LOW)

# Turn off all LEDs
turn_off_all_leds()

# Cleanup GPIO
GPIO.cleanup()
