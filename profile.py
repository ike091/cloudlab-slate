"""Spins up nodes for installing a SLATE cluster.

Instructions:
Wait for the profile instance to start, and then follow instructions on the SLATE website for cluster install.
"""

import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.emulab as emulab
import geni.rspec.igext as igext

# define some constants
CENTOS7_IMG = 'urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD'

# the number of extra public ip addresses to allocate
NUM_IP_ADDRESSES = 2

# create a portal context, needed to define parameters
pc = portal.Context()

# create a Request object to start building RSpec
request = pc.makeRequestRSpec()

# create a node
node = request.RawPC('node1')

node.disk_image = CENTOS7_IMG

# request a pool of dynamic publically routable ip addresses
address_pool = igext.AddressPool('address_pool', NUM_IP_ADDRESSES)
address_pool.component_manager_id = ('urn:publicid:IDN+utah.cloudlab.us+authority+cm')
request.addResource(address_pool)

# output RSpec
pc.printRequestRSpec(request)

