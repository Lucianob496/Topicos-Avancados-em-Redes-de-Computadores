import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

while True:
    msg = bus.recv()
