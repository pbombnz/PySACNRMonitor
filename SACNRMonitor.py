"""
    Copyright (C) 2013 PBomb
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

__title__ = "SACNR Monitor Python API"
__author__ = "PBomb"

__purpose__ = "Enables easy access to SACNR Monitor's API using HTTP protocol."
__copyright__ = "Copyright (C) 2013 PBomb"
__credits__ = ["Blacklite", "SACNR Team"]
__license__ = "GPL - http://www.gnu.org/licenses/gpl-3.0.html"
__version__ = "1.0"
__date__ = "29-01-2013"



import urllib2, json

query_url = 'http://monitor.sacnr.com/api/?'

class SACNRMonitor:
    def __init__(self, *args):
        """ Initialises a SACNRMonitor Object """
        
        if len(args) == 1: #Server ID 
            self.serverID = int(args[0])
            self.useServID = True
        elif len(args) == 2: #IP/Port
            from socket import gethostbyname
            self.ip = gethostbyname(args[0])
            self.port = int(args[1])
            self.useServID = False
        else: #Neither Server ID or IP/Port
            raise Exception("Incorrect Usage. Please look at the documentation in the python source.")
            
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
        """ Returns the specified data about the from sa-mp server """
        """ All Returns produce a dictionary containing the requested data and response fields used to show the success status"""  

        #Creates a url based on either Server ID or Server IP/Port with the correct action parameter
        if self.useServID:  
            request_url = str(query_url)+"ServerID="+str(self.serverID)+"&Action="+str(action)+"&Format=JSON"
        else: 
            request_url = str(query_url)+"IP="+str(self.ip)+"&Port="+str(self.port)+"&Action="+str(action)+"&Format=JSON"

        try:
            #Connects to the request url
            url = urllib2.urlopen(request_url)
            urlSource = url.read()
            url.close()
        except:
            #Failure connecting to the request url
            return { 'response' : False, 'response_message' : 'Could not connect to SACNR Monitor API.' }

        #The sa-mp server that was requested doesnt exist, is not in the database OR has annouce=0 in server.cfg
        if urlSource == "Unknown Server ID":
            return { 'response' : False, 'response_message' : 'Unknown Server ID.' }

        try:
            #Attempting to parse JSON data
            data = json.loads(urlSource)
            #Appends the response fields to data.
            if action == "query" or action == "players":
                data = { 'response' : True,
                         'response_message' : 'Successful.',
                         action : data
                       }
            else:
                data['response'] = True
                data['response_message'] = 'Successful.'
            return data
        except:
            #Failure at attempting to parse JSON data
            return { 'response' : False, 'response_message' : 'Unparseable Data collected.' }

def check_api_status():        
    """ Checks if API is available or not """       
    try:
        urllib2.urlopen(query_url)
        return True
    except urllib2.URLError:
        return False
