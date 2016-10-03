def acceptDNSLookup():
    #Update IPtables

def acceptTCPConnection():
    #Need Sorce IP address and if its on the blacklist
    #Need to know if IP is vetted

    #If source ip is found within the IPTables
    #Then update NAT so that TCP can communicate with content/asset server
    
    #Else If not blacklisted
    #Update NAT to send to Captcha / have captcha increment.