import xbmcplugin, xbmcgui, xbmcaddon, urlparse, sys

def addLink(name, url):
    li = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
    li.setProperty("IsPlayable", "true")
    li.setInfo(type="Video", infoLabels={"Title":name})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=li, isFolder=False)
    
def addDir(name,path,page):
    u=sys.argv[0]+"?path=%s&page=%s"%(path,str(page))
    li=xbmcgui.ListItem(name, iconImage="DefaultFolder.png")
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=li,isFolder=True)

def add_video(title, id):
  url = "plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=%s"%(id)
  addLink(title,  url)
try:
  params = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)
  path = params['path'][0]
  page = int(params['page'][0])
except:
  path = '/'
  page = 1

try:
  if path == '/':
     addDir("Certified Ethical Hacker", "CEH", 1)
     addDir("Google Python Course", "GOOGLEPYTHON", 1)
     addDir("Networking", "NETWORKING", 1)
     addDir("Hacking Concepts", "HACKCONCEPTS", 1)
     addDir("Javascript", "JAVASCRIPT", 1)
     addDir("MongoDB", "MONGODB", 1)
     addDir("Node.js", "NODEJS", 1)
     addDir("Linux", "LINUX", 1)
  elif path == "CEH":
     add_video("Symmetric and Asymmetric Cryptography - Overview", "8sufUTAdXCs")
     add_video("Password Hacking", "VoeLc5295XU")
     add_video("Password Cracking and Guessing", "16MPH7VpGTQ")
     add_video("Creating a DoS attack", "w3p8_-0u-YA")
     add_video("Network Sniffing Software Tools", "pNQdZhQ7vUo")
     add_video("Buffer Overflow Attacks", "iZTilLGAcFQ")
     add_video("Active Footprinting", "eSFt9mBlA2A")
     add_video("Passive Footprinting", "tOXDNUMoPDc")
  elif path == "HACKCONCEPTS":
     add_video("Diffie-Hellman Key Exchange", "YEBfamv-_do")
     add_video("SSL - Moxie Marlinkspike - DEFCON 19", "pDmj_xe7EIQ")
     add_video("Overview of PKI concepts", "QCvHWA7qQNI")
     add_video("SSH known_hosts", "zE7yaAEyqgk")
  elif path == "NETWORKING":
     add_video("Network Layers - OSI, TCP/IP Models - Part 1", "SII38b0RJr8")
     add_video("Network Layers - OSI, TCP/IP Models - Part 2", "W74H0FVXY_w")
     add_video("Network Layers - OSI, TCP/IP Models - Part 3", "BplNYiUV5kU")
     add_video("TCP/IP and Subnet Masking", "EkNq4TrHP_U")
     add_video("DNS Resolution - Step by Step", "3EvjwlQ43_4")
     add_video("DNS Records", "alumRsTngjI")
     add_video("Understanding Switches and Hubs", "9yYqNqTNnqI")
     add_video("Understanding SOHO Routers", "w44J7CN26Ig")
     add_video("VPNs", "q4P4BjjXghQ")
     add_video("Wireless Bridges for Networking", "7nTgQQbF9zo")
     add_video("Black Ops of TCP/IP - Dan Kaminsky - DEFCON 19", "U3o7DhL9gI4")
     add_video("Introduction to OWASP ZAProxy", "eH0RBI0nmww")
  elif path == "GOOGLEPYTHON":
     add_video("1.1 - Introduction and Strings", "tKTZoB2Vjuk")
     add_video("1.2 - Lists, Sorting and Tuples", "EPYupizJYQI")
     add_video("1.3 - Dicts and Files", "haycL41dAhg")
     add_video("2.1 - Regular Expressions", "kWyoYtvJpe4")
     add_video("2.2 - Utilities: OS and Commands", "uKZ8GBKmeDM")
     add_video("2.3 - Utilities: URLs and HTTP, Exceptions", "Nn2KQmVF5Og")
     add_video("2.4 - Closing Thoughts", "IcteAbMC1Ok")
  elif path == "JAVASCRIPT":
     add_video("Introduction to JavaScript and Browser DOM", "ljNi8nS5TtQ")
     add_video("Javascript Closures", "R_ZvxMyFSCU")
     add_video("Javascript: Getting Closure (IIFEs/Closures)", "KRm-h6vcpxs")
     add_video("Definitive Guide to Object-Oriented Javascript", "PMfcsYzj-9M")
     add_video("JSON-LD basics", "vioCbTo3C-4")
     add_video("(Semi-)Automating Javascript Refactoring", "eS51T1hT9Z0")
  elif path == "NODEJS":
     add_video("Introduction to Node.js with Ryan Dahl", "jo_B4LTHi3I")  
     add_video("Node.js - Javascript on the server (Google Techtalk)", "F6k8lTrAE2g")
  elif path == "MONGODB":
     add_video("MongoDB - Not just about Big Data", "b1BZ9YFsd2o")
     add_video("Introduction to MongoDB", "xOLwqUbpxGQ")
     add_video("Building Applications with MongoDB", "UNYSTA4tMVY")
     add_video("MongoDB Schema Design", "PIWVFUtBV1Q")
except Exception as e:
  addDir("%s"%e,"",1)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
