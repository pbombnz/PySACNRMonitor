import urllib.request
import json
from socket import gethostbyname

query_url = 'http://monitor.sacnr.com/api/?'


class SACNRMonitor(object):
    def __init__(self, *args):
        """ Initialises a SACNRMonitor Object """

        self.serverID = None
        self.ip = None
        self.port = None

        if len(args) == 1:  # Server ID
            self.serverID = int(args[0])
        elif len(args) == 2:  # IP & Port
            self.ip = gethostbyname(args[0])
            self.port = int(args[1])
        else:  # Neither Server ID or IP/Port
            raise RuntimeError("Incorrect Usage. Please look at the documentation in the python source.")
            
    def get_info(self):
        """ Returns general info from the requested sa-mp server """  
        return self.get_data("info")

    def get_players(self):
        """ Returns player data from the requested sa-mp server """  
        return self.get_data("players")

    def get_query(self):
        """ Returns query data from the requested sa-mp server """  
        return self.get_data("query")
    
    def get_ad(self):
        """ Returns ad data from the requested sa-mp server """  
        return self.get_data("ad")

    def get_data(self, action):
        """
            Requests the specified data from the from sa-mp server. The method will then parse the data into JSON
            for easy access. If a case where the data wasn't reachable for whatever reason, an IOError is raised.

            :param action: A string the sent to SACNR Monitor that tells us what data we want from the server.
            :return: A dictionary or a list containing the requested data
        """

        # Creates a url based on either Server ID or Server IP/Port with the correct action parameter
        if self.serverID:
            request_url = "{0}ServerID={1}&Action={2}&Format=JSON".format(str(query_url),
                                                                          str(self.serverID),
                                                                          str(action))
        else: 
            request_url = "{0}IP={1}&Port={2}&Action={3}&Format=JSON".format(str(query_url),
                                                                             str(self.ip),
                                                                             str(self.port),
                                                                             str(action))

        # Connects to the request url
        try:
            url = urllib.request.urlopen(request_url)
            response = url.read().decode()
            url.close()
        except:
            # Failure to connect to the request url
            raise IOError('Could not connect to SACNR Monitor API.')

        # Checking if the server doesnt exist or is not in the database OR has 'annouce=0' in server.cfg
        if response == "Unknown Server ID":
            return IOError('Unknown Server ID.')

        # Parse the HTML source into JSON data
        data = json.loads(response)
        return data


def check_api_status():        
    """
        Checks if the API is currently available or not
        :return: Returns True, if the API is available, otherwise returns False
    """
    try:
        urllib.request.urlopen(query_url).close()
        return True
    except IOError:
        return False