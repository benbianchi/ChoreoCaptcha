from netfilterqueue import NetfilterQueue
import iptables
# Other imports?

def acceptDNSLookup():
    #If (blacklistContains(source IP address)):
        #Drop the request by just returning.
    #Else:
        #Call (whitelistClient(source IP address)).
        #Return the current web server name resolution to the client.

def acceptTCPConnection(): # Does this have to be separate for incoming and outgoing messages? Is this separate from sending/receiving messages? 
    #If blacklistContains(source IP address):
        #Drop the request by just returning.
    
    #If (!isValidDestinationAddress(destination IP address)):
        #Drop the request by just returning. (Should we keep track of incorrect requests like this, for future blacklisting?)
    
    #If (whitelistContains(source IP address)):
        #Call routeToWebServer() and return.
        #Update NAT so that TCP can communicate with content/asset server. <--I think the above line should be used instead of this line.
    #Else:
        #Call routeToCAPTCHAServer() and return.
        #Update NAT to send to Captcha / have captcha increment. <--I think the above line should be used instead of this line.
        
def whitelistClient(IPAddress):
    #Add the given IP address to the NAT iptables as an acceptable source IP address.

def unWhitelistClient(IPAddress):
    #Remove the given IP address from the NAT iptables as an acceptable source IP address.

def blacklistClient(IPAddress):
    #Add the given IP address to the user space blacklist.

def unBlacklistClient(IPAddress):
    #Remove the given IP address from the user space blacklist.

def routeToCAPTCHAServer(): #Not sure if we need this function.
    #Translates the relevant address(es) and routes the client traffic to the CAPTCHA server.
    
def routeToWebServer(): #Not sure if we need this function.
    #Translates the relevant address(es) and routes the client traffic to the web server.
    
def blacklistContains(IPAddress):
    #Returns whether the blacklist contains the given IP address.
    
def isValidDestinationAddress(IPAddress):
    #Returns whether the given IP address is an accepted external IP address for the web server.
    
def whitelistContains(IPAddress):
    #Returns whether the given client IP address is whitelisted, i.e. included in the NAT iptables.
    
def fluxExternalAddresses():
    #Do something similar to what I have on the NAT/iptables document in Google Drive.
    
#Do we need anything else?
    # We will have to work with zone files when setting up our bind9 server.
    # We will also eventually use netfilterqueue to catch the incoming TCP and/or UDP messages.
