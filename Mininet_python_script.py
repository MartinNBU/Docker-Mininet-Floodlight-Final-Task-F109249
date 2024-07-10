from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class LinearTopo(Topo):
    def build(self):
        # Adding switches
        switches = []
        for i in range(419):
            switch = self.addSwitch(f's{i+1}', protocols='OpenFlow13')
            switches.append(switch)

        # Adding hosts
        hosts = []
        for i in range(19):
            host = self.addHost(f'h{i+1}')
            hosts.append(host)

        # Creating links
        # Link each host to the first 19 switches
        for i in range(19):
            self.addLink(hosts[i], switches[i])

        # Link switches in a linear topology
        for i in range(418):
            self.addLink(switches[i], switches[i+1])

def run():
    topo = LinearTopo()
    net = Mininet(topo=topo, switch=OVSKernelSwitch, build=False)

    # Adding the remote controller
    c0 = net.addController(name='c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    net.build()
    net.start()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()

