import driveboard, time
import sys

def control_move(path):
    print(path)

    seekrate_ = 6000
    feedrate_ = 2000
    intensity_ = 100.0
    driveboard.absolute()
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
