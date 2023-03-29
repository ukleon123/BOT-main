import socket;
class port_Check:
   def __init__(self, host, port):
      self.__host = host
      self.__port = port
   def check_port(self):
      try:
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         result = sock.connect_ex((self.__host, self.__port))
         if result == 0:
            return 1
         else:
            return 0
      except:
         return 'error'