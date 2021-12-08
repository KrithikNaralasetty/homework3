from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."

    def __init__( self ):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__( self )

	# Add hosts
    hosts = []
    for i in range(8):
        s = "host"+str(i+1)
        hosts.append(self.addHost(s))
    
    # Add switches
    switches = []
    for i in range(7):
        s = "switch"+str(i+1)
        switches.append(self.addSwitch(s))
	
    # Add links
    self.addLink(hosts[0],switches[2])
    self.addLink(hosts[1],switches[2])
    self.addLink(hosts[2],switches[3])
    self.addLink(hosts[3],switches[3])
    self.addLink(hosts[4],switches[5])
    self.addLink(hosts[5],switches[5])
    self.addLink(hosts[6],switches[6])
    self.addLink(hosts[7],switches[6])
    self.addLink(switches[2],switches[1])
    self.addLink(switches[3],switches[1])
    self.addLink(switches[5],switches[4])
    self.addLink(switches[6],switches[4])
    self.addLink(switches[1],switches[0])
    self.addLink(switches[4],switches[0])

topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }