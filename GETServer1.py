
from http.server import BaseHTTPRequestHandler, HTTPServer      #python 3
from MimeTypes import guess_type  #put MimeTypes.py in same folder as the server
from http import cookies
import os
import xmlDBr3 as xmldb
import requests

db = xmldb.xmldb()

hostName = "localhost"
serverPort = 8000

#this is where the server looks for files requested by the browser
root = "."   
os.chdir(root) #change to the html root directory
   
class server(BaseHTTPRequestHandler):

   def do_GET(self):          #this function responds to GET requests
      print(self.path)
      uri = self.path
      if uri == '/': uri = "/index.html"
      db.load("users.xml")  #load user list
      emark_right = uri.rfind('=')  #position of '=' char from right
      emark_left = uri.find('=')  #position of '=' char from left
      andmark = uri.rfind('&')      #position of '&' char
      print("emark_left is {}, andmark is {}, emark_right is {}".format(emark_left,andmark,emark_right))
      path = uri 
      if emark_right == -1:    
        theme = ""
        username = ""
      else:     
        theme = uri[emark_right+1:]    #everything after the '='
        username = uri[emark_left+1:andmark]   #everything between the $ and the =
        newuser = {"name":username,"background":theme} # deal with database #
        key = db.add(newuser)
        cookie = cookies.SimpleCookie()
        cookie['key'] = key
        db.save("users.xml")

      # **************** the URI is actually a URL ***************
      print(username)
      if path == "/": path = path + "/index.html"
      if theme == "light": path = "/pages/text_only1.html"
      if theme == "dark": path = "/pages/text_only1_black.html"
      filename = root+path


      #can we open the file?
      if(os.path.isfile(filename)):  #yes we can
         f=open(filename,"rb")       #open the file
         data=f.read()               #and read its contents

         #send the HTTP status message to the browser
         self.send_response(200)
         self.send_header("Content-type",guess_type(self.path)[0])
         self.send_header("Set-Cookie", cookie.output(header=''))    
         self.end_headers()

         #now send the data
         self.wfile.write(data)

      else:                         #no we can't                
         self.send_response(404)    #let the browser know
         self.send_header("Content-type","text/html")
         self.end_headers()
     

   def do_HEAD(self):    notImplemented(self)
   def do_POST(self):    notImplemented(self)
   def do_PUT(self):     notImplemented(self)
   def do_POST(self):    notImplemented(self)
   def do_UPDATE(self):  notImplemented(self)
   def do_DELETE(self):  notImplemented(self)
   def do_CONNECT(self): notImplemented(self)
   def do_OPTIONS(self): notImplemented(self)
   def do_TRACE(self):   notImplemented(self)
   def do_PATCH(self):   notImplemented(self)

def notImplemented(self):
    self.send_response(501)    #501 Not Implemented
    self.send_header("Content-type","text/html")
    self.end_headers()
    
       
#only run the server if this module was called from the command line.
#python makes the name different if this module is called by another module.
if __name__ == "__main__":    

    webServer = HTTPServer((hostName, serverPort), server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")       
