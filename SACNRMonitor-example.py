import SACNRMonitor

# All 'sancrServer' below are correct uses and suitable for the SACNRMonitor module
sacnrServer = SACNRMonitor.SACNRMonitor("216.245.210.235", 7777)
sacnrServer = SACNRMonitor.SACNRMonitor("216.245.210.235", "7777")
                                        
sacnrServer = SACNRMonitor.SACNRMonitor("server.sacnr.com", 7777)
sacnrServer = SACNRMonitor.SACNRMonitor("server.sacnr.com", "7777")

sacnrServer = SACNRMonitor.SACNRMonitor(53484)
sacnrServer = SACNRMonitor.SACNRMonitor("53484")


# Checks if SACNR Monitor API is online
if SACNRMonitor.check_api_status():
    print("SACNR Monitor API is online")
    print()

    #Prints all actions from SACNR Monitor for the specified server

    # Returns Server Information
    print(sacnrServer.get_info())

    # Returns a List of dictionaries holding individual player information (Player Name, ID, ping and Player Score)
    print(sacnrServer.get_players())

    # Returns a List of dictionaries holding information about how many players were online at a certain time
    print(sacnrServer.get_query())

    #Returns Ad Information
    print(sacnrServer.get_ad())
else:
    print("SACNR Monitor API is offline")

