# VULTR
## Example
```python
from vultr import Vultr
client = Vultr("API_KEY")
print(client.account.info())
```

## Methods
| Name | Description |
|:--------------|:----------------------------------|
| `account.info` | Retrieve information about the current account.
| `app.list` | Retrieve a list of available applications. These refer to applications that can be launched when creating a Vultr VPS.
| `auth.info` | Retrieve information about the current API key.
| `backup.list` | List all backups on the current account.
| `baremetal.app_change` | Reinstalls the bare metal server to a different Vultr one-click application. All data will be permanently lost.
| `baremetal.app_change_list` | Retrieves a list of Vultr one-click applications to which a bare metal server can be changed. Always check against this list before trying to switch applications because it is not possible to switch between every application combination.
| `baremetal.bandwidth` | Get the bandwidth used by a bare metal server.
| `baremetal.create` | Create a new bare metal server. You will start being billed for this immediately. The response only contains the SUBID for the new machine.
| `baremetal.destroy` | Destroy (delete) a bare metal server. All data will be permanently lost, and the IP address will be released. There is no going back from this call.
| `baremetal.get_app_info` | Retrieves the application information for a bare metal server.
| `baremetal.get_user_data` | Retrieves the (base64 encoded) user-data for this subscription.
| `baremetal.halt` | Halt a bare metal server. This is a hard power off, meaning that the power to the machine is severed. The data on the machine will not be modified, and you will still be billed for the machine. To completely delete a machine, see v1/baremetal/destroy.
| `baremetal.ipv6_enable` | Enables IPv6 networking on a bare metal server by assigning an IPv6 subnet to it. The server will not be rebooted when the subnet is assigned. It is possible to check whether or not IPv6 networking has been enabled with v1/baremetal/list_ipv6.
| `baremetal.label_set` | Set the label of a bare metal server.
| `baremetal.list` | List all bare metal servers on the current account. This includes both pending and active servers.
| `baremetal.list_ipv4` | List the IPv4 information of a bare metal server. IP information is only available for bare metal servers in the &quot;active&quot; state.
| `baremetal.list_ipv6` | List the IPv6 information of a bare metal server. IP information is only available for bare metal servers in the &quot;active&quot; state. If the bare metal server does not have IPv6 enabled, then an empty array is returned.
| `baremetal.os_change` | Changes the bare metal server to a different operating system. All data will be permanently lost.
| `baremetal.os_change_list` | Retrieves a list of operating systems to which a bare metal server can be changed. Always check against this list before trying to switch operating systems because it is not possible to switch between every operating system combination.
| `baremetal.reboot` | Reboot a bare metal server. This is a hard reboot, which means that the server is powered off, then back on.
| `baremetal.reinstall` | Reinstall the operating system on a bare metal server. All data will be permanently lost, but the IP address will remain the same. There is no going back from this call.
| `baremetal.set_user_data` | Sets the user-data for this subscription. User-data is a generic data store, which some provisioning tools and cloud operating systems use as a configuration file. It is generally consumed only once after an instance has been launched, but individual needs may vary.
| `baremetal.tag_set` | Set the tag of a bare metal server.
| `block.attach` | Attach a block storage subscription to a VPS subscription. The instance will be restarted. The block storage volume must not be attached to any other VPS subscriptions for this to work.
| `block.create` | Create a block storage subscription.
| `block.delete` | Delete a block storage subscription.  All data will be permanently lost. There is no going back from this call.
| `block.detach` | Detach a block storage subscription from the currently attached instance. The instance will be restarted.
| `block.label_set` | Set the label of a block storage subscription.
| `block.list` | Retrieve a list of any active block storage subscriptions on this account.
| `block.resize` | Resize the block storage volume to a new size.
| `dns.create_domain` | Create a domain name in DNS.
| `dns.create_record` | Add a DNS record.
| `dns.delete_domain` | Delete a domain name and all associated records.
| `dns.delete_record` | Delete an individual DNS record.
| `dns.dnssec_enable` | Enable or disable DNSSEC for a domain.
| `dns.dnssec_info` | Get the DNSSEC keys (if enabled) for a domain.
| `dns.list` | List all domains associated with the current account.
| `dns.records` | List all the records associated with a particular domain.
| `dns.soa_info` | Get the SOA record information for a domain.
| `dns.soa_update` | Update the SOA record information for a domain.
| `dns.update_record` | Update a DNS record.
| `firewall.group_create` | Create a new firewall group on the current account.
| `firewall.group_delete` | Delete a firewall group. Use this function with caution because the firewall group being deleted will be detached from all servers. This can result in open ports accessible to the internet.
| `firewall.group_list` | List all firewall groups on the current account.
| `firewall.group_set_description` | Change the description on a firewall group.
| `firewall.rule_create` | Create a rule in a firewall group.
| `firewall.rule_delete` | Delete a rule in a firewall group.
| `firewall.rule_list` | List the rules in a firewall group.
| `iso.create_from_url` | Create a new ISO image on the current account. The ISO image will be downloaded from a given URL. Download status can be checked with the v1/iso/list call.
| `iso.destroy` | Destroy (delete) an ISO image. There is no going back from this call.
| `iso.list` | List all ISOs currently available on this account.
| `iso.list_public` | List public ISOs offered in the Vultr ISO library.
| `loadbalancer.conf_info` | 
| `loadbalancer.create` | Create a load balancer subscription.
| `loadbalancer.destroy` | Destroy a load balancer subscription. All data will be permanently lost. Web traffic passing through the load balancer will be abruptly terminated. There is no going back from this call.
| `loadbalancer.forward_rule_create` | Create a new forwarding rule.
| `loadbalancer.forward_rule_delete` | Remove a forwarding rule.
| `loadbalancer.forward_rule_list` | List the forwarding rules of a load balancer subscription.
| `loadbalancer.generic_info` | Retrieve the generic configuration of a load balancer subscription.
| `loadbalancer.generic_update` | Update the generic configuration of a load balancer subscription.
| `loadbalancer.health_check_info` | Retrieve the health checking configuration of a load balancer subscription.
| `loadbalancer.health_check_update` | Update the health checking configuration of a load balancer subscription.
| `loadbalancer.instance_attach` | Attach an instance to a load balancer subscription.
| `loadbalancer.instance_detach` | Detach an instance to a load balancer subscription.
| `loadbalancer.instance_list` | List the instances attached to a load balancer subscription.
| `loadbalancer.label_set` | Set the label of a load balancer subscription.
| `loadbalancer.list` | List all load balancer subscriptions on the current account. This includes both pending and active subscriptions.
| `loadbalancer.ssl_add` | Add a SSL certificate to a load balancer.
| `loadbalancer.ssl_info` | Retrieve whether or not your load balancer subscription has an SSL cert attached.
| `loadbalancer.ssl_remove` | Remove a SSL certificate to a load balancer.
| `network.create` | Create a new private network. A private network can only be used at the location for which it was created.
| `network.destroy` | Destroy (delete) a private network. Before destroying, a network must be disabled from all instances. See /v1/server/private_network_disable.
| `network.list` | List all private networks on the current account.
| `objectstorage.create` | Create an object storage subscription.
| `objectstorage.destroy` | Destroy an object storage subscription. All objects will be permanently deleted. There is no going back from this call.
| `objectstorage.label_set` | Set the label of an object storage subscription.
| `objectstorage.list` | List all object storage subscriptions on the current account. This includes both pending and active subscriptions.
| `objectstorage.list_cluster` | List object storage clusters.
| `objectstorage.s3key_regenerate` | Regenerate the S3 API keys of an object storage subscription.
| `os.list` | Retrieve a list of available operating systems.  If the &quot;windows&quot; flag is true, a Windows license will be included with the instance, which will increase the cost.
| `plans.list` | Retrieve a list of all active plans. Plans that are no longer available will not be shown.
| `plans.list_baremetal` | Retrieve a list of all active bare metal plans. Plans that are no longer available will not be shown.
| `plans.list_vc2` | Retrieve a list of all active vc2 plans. Plans that are no longer available will not be shown.
| `plans.list_vc2z` | Retrieve a list of all active high frequency CPU plans. Plans that are no longer available will not be shown.
| `plans.list_vdc2` | Retrieve a list of all active vdc2 plans. Plans that are no longer available will not be shown.
| `regions.availability` | Retrieve a list of the VPSPLANIDs currently available in this location.
| `regions.availability_baremetal` | Retrieve a list of the METALPLANIDs currently available in this location.
| `regions.availability_vc2` | Retrieve a list of the vc2 VPSPLANIDs currently available in this location.
| `regions.availability_vdc2` | Retrieve a list of the vdc2 VPSPLANIDs currently available in this location.
| `regions.list` | Retrieve a list of all active regions. Note that just because a region is listed here, does not mean that there is room for new servers.
| `reservedip.attach` | Attach a reserved IP to an existing subscription.
| `reservedip.convert` | Convert an existing IP on a subscription to a reserved IP. Returns the SUBID of the newly created reserved IP.
| `reservedip.create` | Create a new reserved IP. Reserved IPs can only be used within the same datacenter for which they were created.
| `reservedip.destroy` | Remove a reserved IP from your account. After making this call, you will not be able to recover the IP address.
| `reservedip.detach` | Detach a reserved IP from an existing subscription.
| `reservedip.list` | List all the active reserved IPs on this account. The &quot;subnet_size&quot; field is the size of the network assigned to this subscription. This will typically be a /64 for IPv6, or a /32 for IPv4.
| `server.app_change` | Changes the virtual machine to a different application. All data will be permanently lost.
| `server.app_change_list` | Retrieves a list of applications to which a virtual machine can be changed. Always check against this list before trying to switch applications because it is not possible to switch between every application combination.
| `server.backup_disable` | Disables automatic backups on a server. Once disabled, backups can only be enabled again by customer support.
| `server.backup_enable` | Enables automatic backups on a server.
| `server.backup_get_schedule` | Retrieves the backup schedule for a server. All time values are in UTC.
| `server.backup_set_schedule` | Sets the backup schedule for a server. All time values are in UTC.
| `server.bandwidth` | Get the bandwidth used by a virtual machine.
| `server.create` | Create a new virtual machine. You will start being billed for this immediately. The response only contains the SUBID for the new machine.
| `server.create_ipv4` | Add a new IPv4 address to a server. You will start being billed for this immediately. The server will be rebooted unless you specify otherwise. You must reboot the server before the IPv4 address can be configured.
| `server.destroy` | Destroy (delete) a virtual machine. All data will be permanently lost, and the IP address will be released. There is no going back from this call.
| `server.destroy_ipv4` | Removes a secondary IPv4 address from a server. Your server will be hard-restarted. We suggest halting the machine gracefully before removing IPs.
| `server.firewall_group_set` | Set, change, or remove the firewall group currently applied to a server.
| `server.get_app_info` | Retrieves the application information for this subscription.
| `server.get_user_data` | Retrieves the (base64 encoded) user-data for this subscription.
| `server.halt` | Halt a virtual machine. This is a hard power off (basically, unplugging the machine). The data on the machine will not be modified, and you will still be billed for the machine. To completely delete a machine, see v1/server/destroy.
| `server.ipv6_enable` | Enables IPv6 networking on a server by assigning an IPv6 subnet to it. The server will be automatically rebooted to complete the request. No action occurs if IPv6 networking was already enabled. It is possible to check whether or not IPv6 networking has been enabled with v1/server/list_ipv6.
| `server.iso_attach` | Attach an ISO and reboot the server.
| `server.iso_detach` | Detach the currently mounted ISO and reboot the server.
| `server.iso_status` | Retrieve the current ISO state for a given subscription. The returned state may be one of: ready | isomounting | isomounted. ISOID will only be set when the mounted ISO exists in your library ( see /v1/iso/list ). Otherwise, it will read &quot;0&quot;.
| `server.label_set` | Set the label of a virtual machine.
| `server.list` | List all active or pending virtual machines on the current account.
| `server.list_ipv4` | List the IPv4 information of a virtual machine. IP information is only available for virtual machines in the &quot;active&quot; state.
| `server.list_ipv6` | List the IPv6 information of a virtual machine. IP information is only available for virtual machines in the &quot;active&quot; state. If the virtual machine does not have IPv6 enabled, then an empty array is returned.
| `server.neighbors` | Determine what other subscriptions are hosted on the same physical host as a given subscription.
| `server.os_change` | Changes the virtual machine to a different operating system. All data will be permanently lost.
| `server.os_change_list` | Retrieves a list of operating systems to which a virtual machine can be changed. Always check against this list before trying to switch operating systems because it is not possible to switch between every operating system combination.
| `server.private_network_disable` | Removes a private network from a server. The server will be automatically rebooted to complete the request.
| `server.private_network_enable` | Enables private networking on a server. The server will be automatically rebooted to complete the request. No action occurs if private networking was already enabled. It is possible to check whether or not private networking has been enabled with v1/server/list_ipv4.
| `server.private_networks` | List private networks attached to a particular server.
| `server.reboot` | Reboot a virtual machine. This is a hard reboot (basically, unplugging the machine).
| `server.reinstall` | Reinstall the operating system on a virtual machine. All data will be permanently lost, but the IP address will remain the same. There is no going back from this call.
| `server.restore_backup` | Restore the specified backup to the virtual machine. Any data already on the virtual machine will be lost.
| `server.restore_snapshot` | Restore the specified snapshot to the virtual machine. Any data already on the virtual machine will be lost.
| `server.reverse_default_ipv4` | Set a reverse DNS entry for an IPv4 address of a virtual machine to the original setting. Upon success, DNS changes may take 6-12 hours to become active.
| `server.reverse_delete_ipv6` | Remove a reverse DNS entry for an IPv6 address of a virtual machine. Upon success, DNS changes may take 6-12 hours to become active.
| `server.reverse_list_ipv6` | List the IPv6 reverse DNS entries of a virtual machine. Reverse DNS entries are only available for virtual machines in the &quot;active&quot; state. If the virtual machine does not have IPv6 enabled, then an empty array is returned.
| `server.reverse_set_ipv4` | Set a reverse DNS entry for an IPv4 address of a virtual machine. Upon success, DNS changes may take 6-12 hours to become active.
| `server.reverse_set_ipv6` | Set a reverse DNS entry for an IPv6 address of a virtual machine. Upon success, DNS changes may take 6-12 hours to become active.
| `server.set_user_data` | Sets the user-data for this subscription. User-data is a generic data store, which some provisioning tools and cloud operating systems use as a configuration file. It is generally consumed only once after an instance has been launched, but individual needs may vary.
| `server.start` | Start a virtual machine. If the machine is already running, it will be restarted.
| `server.tag_set` | Set the tag of a virtual machine.
| `server.upgrade_plan` | Upgrade the plan of a virtual machine. The virtual machine will be rebooted upon a successful upgrade.
| `server.upgrade_plan_list` | Retrieve a list of the VPSPLANIDs for which a virtual machine can be upgraded. An empty response array means that there are currently no upgrades available.
| `snapshot.create` | Create a snapshot from an existing virtual machine.  The virtual machine does not need to be stopped.
| `snapshot.create_from_url` | Create a new snapshot on the current account. The snapshot will be downloaded from a given URL. Download status can be checked with the v1/snapshot/list call.
| `snapshot.destroy` | Destroy (delete) a snapshot. There is no going back from this call.
| `snapshot.list` | List all snapshots on the current account.
| `sshkey.create` | Create a new SSH Key.
| `sshkey.destroy` | Remove a SSH key.  Note that this will not remove the key from any machines that already have it.
| `sshkey.list` | List all the SSH keys on the current account.
| `sshkey.update` | Update an existing SSH Key. Note that this will only update newly installed machines. The key will not be updated on any existing machines.
| `startupscript.create` | Create a startup script.
| `startupscript.destroy` | Remove a startup script.
| `startupscript.list` | List all startup scripts on the current account. Scripts of type &quot;boot&quot; are executed by the server&#039;s operating system on the first boot. Scripts of type &quot;pxe&quot; are executed by iPXE when the server itself starts up.
| `startupscript.update` | Update an existing startup script.
| `user.create` | Create a new user.
| `user.delete` | Delete a user.
| `user.list` | Retrieve a list of any users associated with this account.
| `user.update` | Update the details for a user.
