__title__ = "SACNR Monitor Python API - Example"
__author__ = "PBomb"

__purpose__ = "Demostrates the SACNRMonitor module"
__copyright__ = "Copyright (C) 2013 PBomb"
__credits__ = ["Blacklite", "SACNR Team"]
__version__ = "1.0"
__date__ = "29-01-2013"

import SACNRMonitor

#[COMMENT] All 'sancrServer' are correct

#[TIP] Any numeric parameter (ServerID or Port), can be either string or integer.

sacnrServer = SACNRMonitor.SACNRMonitor("216.245.210.235", 7777)
sacnrServer = SACNRMonitor.SACNRMonitor("216.245.210.235", "7777")
                                        
sacnrServer = SACNRMonitor.SACNRMonitor("server.sacnr.com", 7777)
sacnrServer = SACNRMonitor.SACNRMonitor("server.sacnr.com", "7777")

sacnrServer = SACNRMonitor.SACNRMonitor(53484)
sacnrServer = SACNRMonitor.SACNRMonitor("53484")



if SACNRMonitor.check_api_status(): # Checks if SACNR Monitor API is online or offline. The return to this function is Boolean (True/False).
    print "SACNR Monitor API is online"

    #[NOTE] All API Query Functions (all the functions below) return a dictionary object. Within
    #       the dictionary, are 2 keys that will vertify the requested query. These are...
    #
    #       => 'response'         - Boolean - Returns True if request is successful or False if not successful.    
    #       => 'response_message' - String  - Will display the success/error message. 

    print sacnrServer.get_info() # Returns Server Information
    
    print sacnrServer.get_players() # Returns Player Information (Player Name and Player Score)

    print sacnrServer.get_query() # Returns Detailed Player Information (Player Name, Player Score, Player Ping, Player ID)
    
    print sacnrServer.get_ad() #Returns Ad Information

else:
    print "SACNR Monitor API is offline"
  
