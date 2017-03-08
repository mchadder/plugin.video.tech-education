import xbmcplugin, xbmcgui, xbmcaddon, urlparse, sys

def addLink(name, url):
  li = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
  li.setProperty("IsPlayable", "true")
  li.setInfo(type="Video", infoLabels={"Title":name})
  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=li, isFolder=False)
    
def addDir(name,path):
  u=sys.argv[0]+"?path=%s"%(path)
  li=xbmcgui.ListItem(name, iconImage="DefaultFolder.png")
  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=li,isFolder=True)

def add_video(title, id):
  url = "plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=%s"%(id)
  addLink(title,  url)

try:
  params = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)
  path = params['path'][0]
except:
  path = '/'

try:
  if path == '/':
     for key,label in { "CEH":"Certified Ethical Hacker",
                        "PYTHON": "Python",
                        "NETWORKING":"Networking",
                        "NGINX":"Nginx",
                        "JAVASCRIPT":"Javascript",
                        "MONGODB":"MongoDB",
                        "CRYPTO":"Cryptography and Hashing",
                        "NODEJS":"Node.js",
                        "ORACLE": "Oracle",
                        "LINUX":"Linux",
                        "GIT":"Git",
                        "DOCKER":"Docker"
                      }.items():
       addDir(label, key)
  elif path == "NGINX":
     add_video("Load Balancing with Nginx", "SpL_hJNUNEI")
     add_video("Load Balancing and static caching", "FJrs0Ar9asY")
     add_video("Making HTTPS faster with nginx", "iHxD-G0YjiU")
     add_video("Set up HTTPS on nginx", "D2P5cRMi0fQ")
     add_video("5 things you didn't know that NGINX could do", "7Y7ORypoHhE")
     add_video("A security shield for your applications", "nVrwJEWjtSY")
     add_video("NGINX + HTTPS 101 - The basics","dsTub1_4Upg")
  elif path == "DOCKER":
     add_video("Basics of Docker Run command", "yrE2vJDcFVM")
     add_video("Building Docker images using Dockerfile", "6nJu1oDxYvc")
  elif path == "ORACLE":
     add_video("ORDS 3.0 - OAUTH 2.0 Security", "BAC_UqlNzvg")
  elif path == "GIT":
     add_video("Git Tutorials - 1. Setting up and doing a commit", "j1oFazXrzN4")
     add_video("Git Tutorials - 2. Adding a remote repository", "KDt01U859Ik")
     add_video("Git Tutorials - 3. Branching and merging", "uR-9NGrpU-c")
     add_video("Git Tutorials - 4. More Branching", "Luo-xKWD6aw")
     add_video("Git Tutorials - 5. The .gitignore file", "aj8ifYrzGas")
     add_video("How to use Git - add, commit, push, pull, status", "DQUcmNO4diQ")
  elif path == "CRYPTO_GORDON":
     add_video("ITS335 - Passwords, Hashes and Salts", "M7SWzGi0a50")
     add_video("ITS335 - Salts, Passwords and Rainbow Table Attack", "GT_qgImaUS4")
     add_video("CSS441 - Overview and Applications of Public Key Crypto", "gWMYfdkRL3w")
     add_video("CSS441 - Public Key Crypto with RSA", "t4E-dYLBfsM")
     add_video("CSS441 - Cryptographic Hash Functions", "qL8HSt7NWT0")
     add_video("CSS441 - Message Authentication Codes (MACs)", "VTRwZcEtzEo")
     add_video("CSS322 - Hash Functions and Digital Signatures", "CElDACNB-6Y")
     add_video("CSS322 - Collision Resistance and Birthday Paradox", "_JBkw60KPqw")
     add_video("CSS322 - Introduction to Block and Stream Ciphers and DES", "Lh4r8QkFiF0")
  elif path == "CRYPTO_BONEH":
     add_video("Dan Boneh - 2.1 - One-Time Pads", "aMvSvR_NZJE")
     add_video("Dan Boneh - 2.2 - Stream ciphers and PRGs", "NjedHm04ETM")
     add_video("Dan Boneh - 3.1 - Block Ciphers", "vE0h8NCpuQs")
     add_video("Dan Boneh - 3.2 - DES", "UgFoqxKY7cY")
     add_video("Dan Boneh - 3.3 - Exhaustive Search Attacks on DES", "k9LF5O5CCQk")
     add_video("Dan Boneh - 3.5 - AES (Rijndael)", "J10GALwsPYM")
     add_video("Dan Boneh - 3.6 - Block Ciphers from PRGs", "HAqWzQKJPfA")
     add_video("Dan Boneh - 4.1 - PRPs and PRFs", "mM0zbKtvKSA")
     add_video("Dan Boneh - 4.2 - One Time Keys", "s1FOX7B6er8")
     add_video("Dan Boneh - 4.3 - Security for Many-Time Keys", "32R4mRVCA3s")
     add_video("Dan Boneh - 4.4 - CBC", "JNsUrOVQKpE")
     add_video("Dan Boneh - 5.1 - Message Authentication Codes (MACs)","n3qlrMsUzLw")
     add_video("Dan Boneh - 5.2 - MACs based on PRFs","ZZE_kAb-x0o")
     add_video("Dan Boneh - 5.3 - CBC-MAC and NMAC", "Nv7TxoxubWY")
     add_video("Dan Boneh - 5.4 - MAC padding", "EPZ9vr5hteM")
     add_video("Dan Boneh - 6.2 - Generic Birthday Attack", "ZZovSCFZffM")
     add_video("Dan Boneh - 6.3 - Merkle-Damgard Paradigm", "m4NhtUoADfE")
     add_video("Dan Boneh - 6.4 - Constructing Compression Functions", "dw2rMiYp3Go")
     add_video("Dan Boneh - 6.5 - HMAC", "9vUBVRnLwJE")
     add_video("Dan Boneh - 7.5 - Case Study - TLS", "dBpVfO3yixA")
     add_video("Dan Boneh - 8.1 - Key Derivation Functions", "ZorKf6IaP0Q")
     add_video("Dan Boneh - 9.1 - Trusted 3rd Parties", "cmrqdC3c6Tg")
     add_video("Dan Boneh - 9.2 - Merkle Puzzles", "wRBkzEX-4Qo")
     add_video("Dan Boneh - 9.3 - Diffie-Hellman Protocol", "3gfrL5-G3qc")
     add_video("Dan Boneh - 9.4 - Public Key Encryption", "Jd4cew9k_Ow")      
  elif path == "CRYPTO_HASH":
     add_video("Hash Functions And You - PyCon 2015", "IGwNQfjLTp0")
     add_video("Keyed-Hash MAC (HMAC)", "BjInMA-b8ZE")
     add_video("BLAKE / SHA-3 Proposal Visualisation", "bc-lu8uyivk")
     add_video("PBKDF2", "OXT8xqWww6U")
     add_video("SCrypt", "TkWAgeSYL_Q")
  elif path == "CRYPTO":
     addDir("Hash Functions", "CRYPTO_HASH")
     addDir("Steven Gordon - Lectures", "CRYPTO_GORDON")
     addDir("Dan Boneh - Lectures", "CRYPTO_BONEH")     
     add_video("CompTIA+ Digital Signatures", "7gZefMlLpV4")
     add_video("How BitCoin works in 5 minutes", "l9jOJk30eQs")
     add_video("Symmetric and Asymmetric Cryptography - Overview", "8sufUTAdXCs")
     add_video("Overview of PKI concepts", "QCvHWA7qQNI")
     add_video("Diffie-Hellman Key Exchange", "YEBfamv-_do")
     add_video("Elliptic Curve Diffie-Hellman", "F3zzNa42-tQ")
     add_video("How SSL works (with HTTPS example)", "iQsKdtjwtYI")
     add_video("SQRL - Steve Gibson - Digicert Summit 2014", "CviwNXAH1lk")
  elif path == "CEH":
     add_video("Buffer Overflow Attacks", "iZTilLGAcFQ")
     add_video("How Kerberos Works", "kp5d8Yv3-0c")
     add_video("OWASP - XSS", "1eQd7GCOpp4")
     add_video("CSRF Explained", "vrjgD0azkCw")
     add_video("SSL and the future of authenticity - Moxie Marlinspike", "Z7Wl2FW2TcA")
  elif path == "NETWORKING":
     add_video("Network Layers - OSI, TCP/IP Models - Part 1", "SII38b0RJr8")
     add_video("Network Layers - OSI, TCP/IP Models - Part 2", "W74H0FVXY_w")
     add_video("Network Layers - OSI, TCP/IP Models - Part 3", "BplNYiUV5kU")
     add_video("TCP/IP and Subnet Masking", "EkNq4TrHP_U")
     add_video("DNS Resolution - Step by Step", "3EvjwlQ43_4")
     add_video("DNS Records", "alumRsTngjI")
     add_video("Understanding Switches and Hubs", "9yYqNqTNnqI")
     add_video("Understanding SOHO Routers", "w44J7CN26Ig")
     add_video("CompTIA+ - Intro to SANs", "4RsLUTJ_Qtk")
     add_video("NAS and SAN Introduction", "csdJFazj3h0")
     add_video("VPNs", "q4P4BjjXghQ")
     add_video("Wireless Bridges for Networking", "7nTgQQbF9zo")
     add_video("Black Ops of TCP/IP - Dan Kaminsky - DEFCON 19", "U3o7DhL9gI4")
  elif path == "PYTHON":
     add_video("Google Python Course 1.1 - Introduction and Strings", "tKTZoB2Vjuk")
     add_video("Google Python Course 1.2 - Lists, Sorting and Tuples", "EPYupizJYQI")
     add_video("Google Python Course 1.3 - Dicts and Files", "haycL41dAhg")
     add_video("Google Python Course 2.1 - Regular Expressions", "kWyoYtvJpe4")
     add_video("Google Python Course 2.2 - Utilities: OS and Commands", "uKZ8GBKmeDM")
     add_video("Google Python Course 2.3 - Utilities: URLs and HTTP, Exceptions", "Nn2KQmVF5Og")
     add_video("Google Python Course 2.4 - Closing Thoughts", "IcteAbMC1Ok")
     add_video("Python 3 Tutorial - Classes", "Beu5_JZEWsI")
     add_video("Comprehensions", "pShL9DCSIUw")
     add_video("Loop like a native: while,for,iterators,generators..", "EnSu9hHGq5o")
     add_video("Sockets - Binding and Listening", "Q1a12QFq3os")
     add_video("Sockets - Client/Server System", "WrtebUkUssc")
     add_video("The Observer Pattern in Python", "87MNuBgeg34")
     add_video("Python 3 - Multithreading", "6eqC1WTlIqc")
     add_video("Embracing the GIL - David Beazley", "fwzPF2JLoeU")
     add_video("Is your REST API RESTful?","pZYRC8IbCwk")
  elif path == "JAVASCRIPT":
     add_video("Introduction to JavaScript and Browser DOM", "ljNi8nS5TtQ")
     add_video("Javascript Closures", "R_ZvxMyFSCU")
     add_video("Javascript: Getting Closure (IIFEs/Closures)", "KRm-h6vcpxs")
     add_video("Definitive Guide to Object-Oriented Javascript", "PMfcsYzj-9M")
     add_video("JSON-LD basics", "vioCbTo3C-4")
     add_video("(Semi-)Automating Javascript Refactoring", "eS51T1hT9Z0")
     add_video("Teasers : The basics of scope", "ZoFlcv2ByBo")
     add_video("Teasers : Keeping track of \"this\"", "JduQUNn7L4w")
     add_video("Teasers : What is an Object?", "8iXoWC9XcU8")
  elif path == "NODEJS":
     add_video("Introduction to Node.js with Ryan Dahl", "jo_B4LTHi3I")  
     add_video("Node.js - Javascript on the server (Google Techtalk)", "F6k8lTrAE2g")
  elif path == "MONGODB":
     add_video("MongoDB - Not just about Big Data", "b1BZ9YFsd2o")
     add_video("Introduction to MongoDB", "xOLwqUbpxGQ")
     add_video("Building Applications with MongoDB", "UNYSTA4tMVY")
     add_video("MongoDB Schema Design", "PIWVFUtBV1Q")
  elif path == "LINUX":
     add_video("Introduction to Docker", "Q5POuMHxW-0")
     add_video("Configuring GRUB", "osEemMXKjFM")
     add_video("How to CHROOT on Linux", "N87m6fxO5a8")
     add_video("How to compile a kernel on Debian Linux", "KRCfkahi2HQ")
     add_video("Creating a filesystem using Debootstrap", "L_r3z3402do")
     add_video("Creating a CHROOT JAIL in Ubuntu - Part 1", "XTyY3in5r6Q")
     add_video("Creating a CHROOT JAIL in Ubuntu - Part 2", "VfyvF1cnYdE")
     add_video("Creating a CHROOT JAIL in Ubuntu - Part 3", "m_XAI8KhPd4")
except Exception as e:
  addDir("%s"%e,"")

xbmcplugin.endOfDirectory(int(sys.argv[1]))
