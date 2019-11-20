#!/usr/bin/python3


import time
from SX127x.LoRa import *
#from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config import BOARD

BOARD.setup()
BOARD.reset()
#parser = LoRaArgumentParser("Lora tester")


def init(verbose=False):
    #super(mylora, self).__init__(verbose)
    LoRa.set_mode(MODE.SLEEP)
    LoRa.set_dio_mapping([0] * 6)
def on_rx_done(data):
     BOARD.led_on()
     #print("\nRxDone")
     LoRa.clear_irq_flags(RxDone=1)
     payload = self.read_payload(nocheck=True )# Receive INF
     print ("Receive: ")
     mens=bytes(payload).decode("utf-8",'ignore')
     mens=mens[2:-1] #to discard \x00\x00 and \x00 at the end
     print(mens)
     BOARD.led_off()
     if mens=="INF":
        print("Received data request INF")
        time.sleep(2)
        print ("Send mens: DATA RASPBERRY PI")
        LoRa.write_payload([255, 255, 0, 0, 68, 65, 84, 65, 32, 82, 65, 83, 80, 66, 69, 82, 82, 89, 32, 80, 73, 0]) # Send DATA RASPBERRY PI
        LoRa.set_mode(MODE.TX)
     time.sleep(2)
     LoRa.reset_ptr_rx()
     LoRa.set_mode(MODE.RXCONT)
def on_tx_done(self):
     print("\nTxDone")
     print(self.get_irq_flags())
def on_cad_done(self):
     print("\non_CadDone")
     print(self.get_irq_flags())
def on_rx_timeout(self):
     print("\non_RxTimeout")
     print(self.get_irq_flags())
def on_valid_header(self):
     print("\non_ValidHeader")
     print(self.get_irq_flags())
def on_payload_crc_error(self):
     print("\non_PayloadCrcError")
     print(self.get_irq_flags())

def on_fhss_change_channel(self):
     print("\non_FhssChangeChannel")
     print(self.get_irq_flags())
#  def start():
#     while True:
#         LoRa.reset_ptr_rx()
#         LoRa.set_mode(MODE.RXCONT) # Receiver mode
#         while True:
#             pass;
            

#args = parser.parse_args(lora) # configs in LoRaArgumentParser.py
LoRa=LoRa()
#     Slow+long range  Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, CRC on. 13 dBm
init(False)
#LoRa.set_pa_config(pa_select=1, max_power=21, output_power=15)
# LoRa.set_bw(BW.BW125)
# LoRa.set_coding_rate(CODING_RATE.CR4_8)
# LoRa.set_spreading_factor(12)
# LoRa.set_rx_crc(True)
# LoRa.reset_ptr_rx()
# LoRa.set_mode(MODE.RXCONT)
#lora.set_lna_gain(GAIN.G1)
#lora.set_implicit_header_mode(False)
# LoRa.set_low_data_rate_optim(True)

#  Medium Range  Defaults after init are 434.0MHz, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on 13 dBm
#lora.set_pa_config(pa_select=1)


data=[255,255,0,0,55,54,46,50,0]
assert(LoRa.get_agc_auto_on() == 1)

try:
    print("START")
    start()
    on_rx_done(data)
except KeyboardInterrupt:
    sys.stdout.flush()
    print("Exit")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("Exit")
    set_mode(MODE.SLEEP)
BOARD.teardown()
