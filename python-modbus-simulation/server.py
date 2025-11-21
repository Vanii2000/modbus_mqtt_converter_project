import time
import threading
import pymodbus
from datetime import datetime

from pymodbus.datastore import (
    ModbusSlaveContext,
    ModbusServerContext,
    ModbusSequentialDataBlock,
)
from pymodbus.server.sync import StartTcpServer

store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(1, [0,0,0,0])
)
context = ModbusServerContext(slaves=store, single=True)

def set_registers():
    now = datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second
    timestamp = int(now.timestamp())

    vals = context[0x00].getValues(3, 0, count=3)   # FC=3, holding regs
    new_vals = [(hour & 0xFFFF), (minute & 0xFFFF), (second & 0xFFFF), (timestamp & 0xFFFF)]
    context[0x00].setValues(3, 0, new_vals)
    return new_vals

def updater_thread():
    while True:
        set_registers()
        time.sleep(1)

if __name__ == "__main__":
    print(f"PyModbus {pymodbus.__version__} sync server on 0.0.0.0:502")
    threading.Thread(target=updater_thread, daemon=True).start()
    StartTcpServer(context=context, address=("0.0.0.0", 502))
