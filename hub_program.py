# this is the main python file for the hub
from hub import light_matrix, runloop, motor, port

async def main():
    # write your code here
    await motor.run_for_degrees(port.A, 2160, 1080)

runloop.run(main())