import time, subprocess

timeLeft = 30
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)