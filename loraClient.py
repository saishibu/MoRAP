#!/usr/bin/python3

import time
from SX127x.LoRa import *
from SX127x.board_config import BOARD

BOARD.setup()
BOARD.reset()
class mylora(LoRa):
  def __init__(self, verbose=False):
    super(mylora, self).__init__(verbose)
    self.set_mode(MODE.SLEEP)
    self.set_dio_mapping([0] * 6)
    
