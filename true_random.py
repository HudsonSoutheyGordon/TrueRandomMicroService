import zmq
from rand_api_call import generate_random

_debug_flag = True

#setup connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")



while(True):
    message = socket.recv()     # Any response is acceptable to trigger call.
    if _debug_flag:
        rand_bits = '0100010010011010101100101101010010010100101111000010100100101101011111101110111101101010111110010100010110101000000010111101010111001001010110100111011110010011001000000100101100101101110110000111101111010100000100011011000110000101000110010110000011011000'
    else:
        rand_bits = generate_random()

    socket.send(rand_bits.encode())


