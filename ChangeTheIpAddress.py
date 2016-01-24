__author__ = 'Darpan'

import wmi

nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True);
wireless_adapter_configuration = nic_configs[0];
ip = u'192.168.14.67'
subnetmask = u'255.255.255.0'

wireless_adapter_configuration.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
print wireless_adapter_configuration;
#print nic_configs