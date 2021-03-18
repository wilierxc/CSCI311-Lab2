from http.server import BaseHTTPRequestHandler, HTTPServer      #python 3
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  #python 2

import os
from subprocess import Popen, PIPE
from MimeTypes import guess_type  #put MimeTypes.py in same folder as BasicServer.py

hostName = "localhost"
serverPort = 8000

#this is where the server looks for files requested by the browser
root = "/Users/carmenwang/Desktop/CSCI311/Lab2/"   #or wherever you want
os.chdir(root) #change to the html root directory
   
class textserver(BaseHTTPRequestHandler):


   def do_GET(self):          #this function responds to GET requests


      print(self.headers)
      path = self.path
      if path == "/": path = path + "index.html"
      filename = root+path
      
      #can we open the file?
      if(os.path.isfile(filename)):  #yes we can
         f=open(filename,"rb")       #open the file
         data=f.read()               #and read its contents

         #send the HTTP status message to the browser
         self.send_response(200)
         self.send_header("Content-type",guess_type(self.path)[0])
         self.end_headers()

         #now send the data
         self.wfile.write(data)

      else:                         #no we can't                
         self.send_response(404)    #let the browser know
         self.send_header("Content-type","text/html")
         self.end_headers()
    
   def do_POST(self): #POST always passes variables to a script
       print("Got POST") 
   def do_HEAD(self):
       print("Got HEAD")
       notImplemented(self)           
   def do_PUT(self):
       print("GOT PUT");
       notImplemented(self)
   def do_UPDATE(self):
       notImplemented(self)
   def do_DELETE(self):
       notImplemented(self)
   def do_CONNECT(self):
       notImplemented(self)
   def do_OPTIONS(self):
       notImplemented(self)
   def do_TRACE(self):
       notImplemented(self)
   def do_PATCH(self):
       notImplemented(self)

def notImplemented(self):
    self.send_response(501)    #501 Not Implemented
    self.send_header("Content-type","text/html")
    self.end_headers()
    
#only run the server if this module was called from the command line.
#python makes the name different if this module is called by another module.
if __name__ == "__main__":    

    #Start the server. Functions from class BasicServer will handle
    #requests from browsers

    webServer = HTTPServer((hostName, serverPort), textserver)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")       
