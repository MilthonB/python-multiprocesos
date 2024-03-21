from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# from pathlib import Path

def main():
    autorizer =  DummyAuthorizer()
    
    autorizer.add_user(username='uranaibaba',password='roshi',homedir='C:/TEST-FTP',msg_login='Login successful',msg_quit='Goodbye', perm='elradfmwMT')
    
    handler = FTPHandler
    handler.authorizer =  autorizer
    
    handler.banner = ' FTPS - ready running... '
    
    addres = ('127.0.0.1', 2121)
    server = FTPServer( addres, handler=handler )
    
    server.max_cons =256
    server.max_cons_per_ip = 5
    
    server.serve_forever()
    
    
if __name__ == '__main__':
    main()
    