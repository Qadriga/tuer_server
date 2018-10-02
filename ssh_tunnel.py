"""
this module establishes a ssh tunnel to the server an tells the other side to forward it
"""
from sshtunnel import SSHTunnelForwarder, create_logger
from threading import  Thread
from time import  sleep, time
import logging
from configLoader import ProjectConfiguration as PC

TUNNEL = None

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class SSHTunnelWrapper(Thread):
    def __init__(self):
        Thread.__init__(self)  # call super constructor
        self.running = True
        start_point = time()
        self.tunnel = SSHTunnelForwarder(
            ssh_address_or_host=(PC.getSSHRemotename(),22), # connect to Remote on ssh default port 
            # TODO: integare it into the condif
            ssh_username=PC.getSSHUsername(),
            #ssh_password='',
            ssh_pkey=PC.getSSHkeyfilepath(),
            remote_bind_address=(PC.getSSHTunnelname(), 3306),  # connect to mysql default port
            set_keepalive=15,  # send keep alive messages to held the connection open
            local_bind_address=('0.0.0.0', 3307), # bind ssh port on all local interfaces
            logger=create_logger(loglevel=logging.DEBUG)
        )
        self.tunnel.start()
        end_point = time()
        print (end_point - start_point)
        self.start()

    def run(self):
        self.tunnel.start()
        while(self.running):
            if(self.tunnel.check_tunnels()):
                self.tunnel.restart()
            sleep(1)
        self.tunnel.stop()

    def stop(self):
        self.running = False

    def restart(self):
        self.tunnel.restart()

if __name__ =="__main__":
    import sys
    var = SSHTunnelWrapper()
    if sys.version_info[0] < 3:
        raw_input("Press the Any Key")
    else:
        input("Press the Any Key")
    var.stop()
