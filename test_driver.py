import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

socket.send(b"test")
message = socket.recv()
print(message)