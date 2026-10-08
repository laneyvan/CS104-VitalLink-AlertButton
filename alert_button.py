from dotenv import load_dotenv
import os
import time
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

JSON_BODY = {
    "chat_id": "CHAT_ID",
    "text": "Someone pressed the alert button!"
}

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")
button_pressed = False
try:
  while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        requests.post("https://api.telegram.org/bot8922384411:AAF9ifDaZA2kS2t6GfT4k2eWTXwh2k2AhC8/sendMessage", json=JSON_BODY)
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)
except KeyboardInterrupt:
  print("\nMonitoring stopped.")
  GPIO.cleanup()

