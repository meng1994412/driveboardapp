import driveboard
import time

def control(decision):
    seekrate_ = 6000
    driveboard.feedrate(seekrate_)
    driveboard.intensity(0.0)
    if decision == "left":
        driveboard.move(-10.0, 0)
        time.sleep(0.1)
    elif decision == "right":
        driveboard.move(10.0, 0)
        time.sleep(0.1)
    elif decision == "top":
        driveboard.move(0, -10.0)
        time.sleep(0.1)
    elif decision == "bot":
        driveboard.move(0, 10.0)
        time.sleep(0.1)
    elif decision == "quit":
        driveboard.absolute()
        driveboard.air_off()
        driveboard.feedrate(seekrate_)
        driveboard.intensity(0.0)
        time.sleep(0.1)
        driveboard.move(0, 0, 0)
        time.sleep(0.1)
    elif decision == "run":
        path = [[[0, 0], [0, 0]],[[30.0, 30.0], [30.0, 60.0], [60.0, 60.0], [60.0, 30.0], [30.0, 30.0]]]

        # if driveboard.status()['ready']:
        driveboard.intensity(0.0)
        driveboard.air_on()
        seekrate_ = 6000
        feedrate_ = 2000
        intensity_ = 100.0
        for polyline in path:
            if len(polyline) > 0:
                driveboard.feedrate(seekrate_)
                driveboard.intensity(0.0)
                driveboard.move(polyline[0][0], polyline[0][1])
                if len(polyline) > 1:
                    driveboard.feedrate(feedrate_)
                    driveboard.intensity(intensity_)
                    for i in range(1, len(polyline)):
                        driveboard.move(polyline[i][0], polyline[i][1])
                        time.sleep(0.08)

        driveboard.air_off()
        driveboard.feedrate(seekrate_)
        driveboard.intensity(0.0)
        time.sleep(0.1)
        driveboard.move(0, 0, 0)
        time.sleep(0.1)

# if __name__ == "__main__":
#     driveboard.connect()
#
#     driveboard.intensity(0.0)
#     driveboard.air_on()
#     seekrate_ = 6000
#     feedrate_ = 2000
#     intensity_ = 100.0
#     driveboard.relative()
#
#     driveboard.feedrate(seekrate_)
#     driveboard.intensity(0.0)
#     driveboard.move(50, 50)
#     time.sleep(2)
#
#     control("left")
#     control("bot")
#
#     driveboard.close()
