import cv2
import numpy as np
from twilio.rest import Client
from datetime import datetime, time
import time as tm
from playsound import playsound

# Twilio credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
recipient_phone_number = 'RECIPIENT_PHONE_NUMBER'

# Function to send SMS using Twilio
def send_sms(message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

# Function to make a call using Twilio
def make_call():
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        twiml='<Response><Say>Hello! A human has been detected. Please check the camera feed.</Say></Response>',
        to=recipient_phone_number,
        from_=twilio_phone_number
    )
    print("Call placed. Please check your phone.")

# Function to detect humans using OpenCV's HOG detector
def detect_humans(frame):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    found, _ = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    return found

# Main function to control the camera and send notifications
def main():
    camera = cv2.VideoCapture(0)
    alarm_sound = "alarm.wav"

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture image")
            break

        # Detect humans in the frame
        humans = detect_humans(frame)

        # If humans are detected and it's nighttime, send an SMS, make a call, and sound the alarm
        if humans.any() and is_nighttime():
            message = "Human detected at night!"
            print(message)
            send_sms(message)
            make_call()
            playsound(alarm_sound)

        # Display the frame with detected humans
        for (x, y, w, h) in humans:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

# Function to check if it's nighttime (after 12:01 AM)
def is_nighttime():
    now = datetime.now()
    current_time = now.time()
    if current_time > time(0, 1) and current_time < time(6, 0):
        return True
    return False

if __name__ == "__main__":
    main()
