import logging
import os

from kalliope.core.NeuronModule import NeuronModule
logging.basicConfig()
logger = logging.getLogger("kalliope")

class Shutdown (NeuronModule):
    def __init__(self, **kwargs):
        super(Shutdown, self).__init__(**kwargs)
        os.system('sudo halt')