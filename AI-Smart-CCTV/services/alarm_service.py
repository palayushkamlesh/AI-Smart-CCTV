import threading
import playsound

alarm_running = False


def play_alarm():

    global alarm_running

    if alarm_running:
        return

    alarm_running = True

    try:
        playsound.playsound("assets/alarm.mp3")
    except Exception as e:
        print(e)

    alarm_running = False


def start_alarm():

    threading.Thread(
        target=play_alarm,
        daemon=True
    ).start()