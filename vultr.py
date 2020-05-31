import requests

class Vultr:
    HOST = "https://api.vultr.com/v1/"
    
    def __init__(self, API_KEY):
        self.session = requests.session()
        self.session.headers = {
            "API-Key": API_KEY,
        }

    def request(self, method, path, data):
        response = getattr(self.session, method)(self.HOST + path, data=data)
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def app_change_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
            APPID: "Application to use. See /v1/baremetal/app_change_list.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert APPID and isinstance(APPID, int), "APPID must be integer"
        return self.request("post", "/v1/baremetal/app_change", {"SUBID": SUBID, "APPID": APPID})

    def app_change_list_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/baremetal/app_change_list", {"SUBID": SUBID})

    def app_change_list_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/app_change_list", {"SUBID": SUBID})

    def app_change_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            APPID: "Application to use. See /v1/server/app_change_list.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert APPID and isinstance(APPID, int), "APPID must be integer"
        return self.request("post", "/v1/server/app_change", {"SUBID": SUBID, "APPID": APPID})

    def attach_block_v1(self,
            SUBID: "ID of the block storage subscription to attach",
            attach_to_SUBID: "ID of the VPS subscription to mount the block storage subscription to",
            live: "'yes' or 'no'.  If 'yes', this will be attached to the instance without a restart (requires support from the instance's operating system). (default is 'no')" = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert attach_to_SUBID and isinstance(attach_to_SUBID, int), "attach_to_SUBID must be integer"
        assert live and isinstance(live, str), "live must be string"
        return self.request("post", "/v1/block/attach", {"SUBID": SUBID, "attach_to_SUBID": attach_to_SUBID, "live": live})

    def attach_reservedip_v1(self,
            ip_address: "Reserved IP to be attached. Include the subnet size in this parameter (e.g: /32 or /64).",
            attach_SUBID: "Unique identifier of the target server.",
        ):
        assert ip_address and isinstance(ip_address, str), "ip_address must be string"
        assert attach_SUBID and isinstance(attach_SUBID, int), "attach_SUBID must be integer"
        return self.request("post", "/v1/reservedip/attach", {"ip_address": ip_address, "attach_SUBID": attach_SUBID})

    def availability_baremetal_regions_v1(self,
            DCID: "Location to check availability.",
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        return self.request("get", "/v1/regions/availability_baremetal", {"DCID": DCID})

    def availability_regions_v1(self,
            DCID: "Location to check availability.",
            _type: "The type of plans for which to include availability. Possible values: \"all\", \"vc2\", \"ssd\", \"vdc2\", \"dedicated\"." = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert _type and isinstance(_type, str), "type must be string"
        return self.request("get", "/v1/regions/availability", {"DCID": DCID, "type": _type})

    def availability_vc2_regions_v1(self,
            DCID: "Location to check availability.",
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        return self.request("get", "/v1/regions/availability_vc2", {"DCID": DCID})

    def availability_vdc2_regions_v1(self,
            DCID: "Location to check availability.",
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        return self.request("get", "/v1/regions/availability_vdc2", {"DCID": DCID})

    def backup_disable_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/backup_disable", {"SUBID": SUBID})

    def backup_enable_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/backup_enable", {"SUBID": SUBID})

    def backup_get_schedule_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/backup_get_schedule", {"SUBID": SUBID})

    def backup_set_schedule_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            cron_type: "Backup cron type. Can be one of 'daily', 'weekly', 'monthly', 'daily_alt_even', or 'daily_alt_odd'.",
            hour: "Hour value (0-23). Applicable to crons: 'daily', 'weekly', 'monthly', 'daily_alt_even', 'daily_alt_odd'" = None,
            dow: "Day-of-week value (0-6). Applicable to crons: 'weekly'." = None,
            dom: "Day-of-month value (1-28). Applicable to crons: 'monthly'." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert cron_type and isinstance(cron_type, str), "cron_type must be string"
        assert hour and isinstance(hour, int), "hour must be integer"
        assert dow and isinstance(dow, int), "dow must be integer"
        assert dom and isinstance(dom, int), "dom must be integer"
        return self.request("post", "/v1/server/backup_set_schedule", {"SUBID": SUBID, "cron_type": cron_type, "hour": hour, "dow": dow, "dom": dom})

    def bandwidth_baremetal_v1(self):
        return self.request("get", "/v1/baremetal/bandwidth", {})

    def bandwidth_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/bandwidth", {"SUBID": SUBID})

    def conf_info_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/conf_info", {"SUBID": SUBID})

    def convert_reservedip_v1(self,
            SUBID: "SUBID of the server that currently has the IP address you want to convert",
            ip_address: "IP address you want to convert (v4 must be a /32, v6 must be a /64)",
            label: "Label for this reserved IP" = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ip_address and isinstance(ip_address, str), "ip_address must be string"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/reservedip/convert", {"SUBID": SUBID, "ip_address": ip_address, "label": label})

    def create_baremetal_v1(self,
            DCID: "Location in which to create the server. See v1/regions/list.",
            METALPLANID: "Plan to use when creating this server. See v1/plans/list_baremetal.",
            OSID: "Operating system to use. See v1/os/list.",
            SCRIPTID: "The SCRIPTID of a startup script to execute on boot. This only works when using a Vultr supplied operating system. See v1/startupscript/list." = None,
            SNAPSHOTID: "If you've selected the 'snapshot' operating system, this should be the SNAPSHOTID (see v1/snapshot/list) to restore for the initial installation." = None,
            enable_ipv6: "'yes' or 'no'.  If yes, an IPv6 subnet will be assigned to the server." = None,
            label: "This is a text label that will be shown in the control panel." = None,
            SSHKEYID: "List of SSH keys to apply to this server on install (only valid for Linux/FreeBSD). See v1/sshkey/list. Separate keys with commas." = None,
            APPID: "If launching an application (OSID 186), this is the APPID to launch. See v1/app/list." = None,
            userdata: "Base64 encoded user-data." = None,
            notify_activate: "(optional, default 'yes') 'yes' or 'no'. If yes, an activation email will be sent when the server is ready." = None,
            hostname: "The hostname to assign to this server." = None,
            tag: "The tag to assign to this server." = None,
            reserved_ip_v4: "IP address of the floating IP to use as the main IP of this server." = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert METALPLANID and isinstance(METALPLANID, int), "METALPLANID must be integer"
        assert OSID and isinstance(OSID, int), "OSID must be integer"
        assert SCRIPTID and isinstance(SCRIPTID, int), "SCRIPTID must be integer"
        assert SNAPSHOTID and isinstance(SNAPSHOTID, str), "SNAPSHOTID must be string"
        assert enable_ipv6 and isinstance(enable_ipv6, str), "enable_ipv6 must be string"
        assert label and isinstance(label, str), "label must be string"
        assert SSHKEYID and isinstance(SSHKEYID, str), "SSHKEYID must be string"
        assert APPID and isinstance(APPID, int), "APPID must be integer"
        assert userdata and isinstance(userdata, str), "userdata must be string"
        assert notify_activate and isinstance(notify_activate, str), "notify_activate must be string"
        assert hostname and isinstance(hostname, str), "hostname must be string"
        assert tag and isinstance(tag, str), "tag must be string"
        assert reserved_ip_v4 and isinstance(reserved_ip_v4, str), "reserved_ip_v4 must be string"
        return self.request("post", "/v1/baremetal/create", {"DCID": DCID, "METALPLANID": METALPLANID, "OSID": OSID, "SCRIPTID": SCRIPTID, "SNAPSHOTID": SNAPSHOTID, "enable_ipv6": enable_ipv6, "label": label, "SSHKEYID": SSHKEYID, "APPID": APPID, "userdata": userdata, "notify_activate": notify_activate, "hostname": hostname, "tag": tag, "reserved_ip_v4": reserved_ip_v4})

    def create_block_v1(self,
            DCID: "DCID of the location to create this subscription in.  See /v1/regions/list",
            size_gb: "Size (in GB) of this subscription.",
            label: "Text label that will be associated with the subscription" = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert size_gb and isinstance(size_gb, int), "size_gb must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/block/create", {"DCID": DCID, "size_gb": size_gb, "label": label})

    def create_domain_dns_v1(self,
            domain: "Domain name to create",
            serverip: "Server IP to use when creating default records (A and MX)",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        assert serverip and isinstance(serverip, str), "serverip must be string"
        return self.request("post", "/v1/dns/create_domain", {"domain": domain, "serverip": serverip})

    def create_from_url_iso_v1(self,
            url: "Remote URL from where the ISO will be downloaded.",
        ):
        assert url and isinstance(url, str), "url must be string"
        return self.request("post", "/v1/iso/create_from_url", {"url": url})

    def create_from_url_snapshot_v1(self,
            url: "Remote URL from where the snapshot will be downloaded.",
        ):
        assert url and isinstance(url, str), "url must be string"
        return self.request("post", "/v1/snapshot/create_from_url", {"url": url})

    def create_ipv4_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            reboot: "(optional, default 'yes') 'yes' or 'no'. If yes, the server is rebooted immediately." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert reboot and isinstance(reboot, str), "reboot must be string"
        return self.request("post", "/v1/server/create_ipv4", {"SUBID": SUBID, "reboot": reboot})

    def create_loadbalancer_v1(self,
            DCID: "Location in which to create the load balancer. See \"v1/regions/list\".",
            label: "Text label that will be associated with the subscription." = None,
            config_ssl_redirect: "Forces redirect from HTTP to HTTPS." = None,
            sticky_sessions: "Enables sticky sessions for your load balancer - valid options are on or off." = None,
            cookie_name: "Name for your stick session." = None,
            balancing_algorithm: "Balancing algorithm for your load balancer - valid options are roundrobin or leastconn." = None,
            proxy_protocol: "Enables proxy protocol - valid options are on or off" = None,
            ssl_private_key: "The SSL certificates private key." = None,
            ssl_chain: "The SSL certificate chain." = None,
            attached_nodes: "List which instances you want attached to your load balancer." = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert label and isinstance(label, str), "label must be string"
        assert config_ssl_redirect and isinstance(config_ssl_redirect, boolean), "config_ssl_redirect must be boolean"
        assert sticky_sessions and isinstance(sticky_sessions, str), "sticky_sessions must be string"
        assert cookie_name and isinstance(cookie_name, str), "cookie_name must be string"
        assert balancing_algorithm and isinstance(balancing_algorithm, str), "balancing_algorithm must be string"
        assert proxy_protocol and isinstance(proxy_protocol, str), "proxy_protocol must be string"
        assert ssl_private_key and isinstance(ssl_private_key, str), "ssl_private_key must be string"
        assert ssl_chain and isinstance(ssl_chain, str), "ssl_chain must be string"
        assert attached_nodes and isinstance(attached_nodes, list), "attached_nodes must be list"
        return self.request("post", "/v1/loadbalancer/create", {"DCID": DCID, "label": label, "config_ssl_redirect": config_ssl_redirect, "sticky_sessions": sticky_sessions, "cookie_name": cookie_name, "balancing_algorithm": balancing_algorithm, "proxy_protocol": proxy_protocol, "ssl_private_key": ssl_private_key, "ssl_chain": ssl_chain, "attached_nodes": attached_nodes})

    def create_network_v1(self,
            DCID: "Location for the network. See v1/regions/list.",
            description: "Description of network." = None,
            v4_subnet: "IPv4 network to be used when attaching servers to this network." = None,
            v4_subnet_mask: "Network mask corresponding with the v4_subnet." = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert description and isinstance(description, str), "description must be string"
        assert v4_subnet and isinstance(v4_subnet, str), "v4_subnet must be string"
        assert v4_subnet_mask and isinstance(v4_subnet_mask, int), "v4_subnet_mask must be integer"
        return self.request("post", "/v1/network/create", {"DCID": DCID, "description": description, "v4_subnet": v4_subnet, "v4_subnet_mask": v4_subnet_mask})

    def create_objectstorage_v1(self,
            OBJSTORECLUSTERID: "Cluster to use for object storage. See /v1/objectstorage/list_cluster.",
            label: "Text label that will be associated with the subscription." = None,
        ):
        assert OBJSTORECLUSTERID and isinstance(OBJSTORECLUSTERID, int), "OBJSTORECLUSTERID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/objectstorage/create", {"OBJSTORECLUSTERID": OBJSTORECLUSTERID, "label": label})

    def create_record_dns_v1(self,
            domain: "Domain name to add record to",
            name: "Name (subdomain) of record",
            _type: "Type (A, AAAA, MX, etc) of record",
            data: "Data for this record",
            priority: "(only required for MX and SRV) Priority of this record (omit the priority from the data)",
            ttl: "TTL of this record" = None,
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        assert name and isinstance(name, str), "name must be string"
        assert _type and isinstance(_type, str), "type must be string"
        assert data and isinstance(data, str), "data must be string"
        assert ttl and isinstance(ttl, int), "ttl must be integer"
        assert priority and isinstance(priority, int), "priority must be integer"
        return self.request("post", "/v1/dns/create_record", {"domain": domain, "name": name, "type": _type, "data": data, "ttl": ttl, "priority": priority})

    def create_reservedip_v1(self,
            DCID: "Location to create this reserved IP in.  See v1/regions/list",
            ip_type: "'v4' or 'v6' Type of reserved IP to create",
            label: "Label for this reserved IP" = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert ip_type and isinstance(ip_type, str), "ip_type must be string"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/reservedip/create", {"DCID": DCID, "ip_type": ip_type, "label": label})

    def create_server_v1(self,
            DCID: "Location to create this virtual machine in. See v1/regions/list.",
            VPSPLANID: "Plan to use when creating this virtual machine. See v1/plans/list.",
            OSID: "Operating system to use. See v1/os/list.",
            ipxe_chain_url: "If you've selected the 'custom' operating system, this can be set to chainload the specified URL on bootup, via iPXE." = None,
            ISOID: "If you've selected the 'custom' operating system, this is the ID of a specific ISO to mount during the deployment." = None,
            SCRIPTID: "If you've not selected a 'custom' operating system, this can be the SCRIPTID of a startup script to execute on boot. See v1/startupscript/list." = None,
            SNAPSHOTID: "If you've selected the 'snapshot' operating system, this should be the SNAPSHOTID (see v1/snapshot/list) to restore for the initial installation." = None,
            enable_ipv6: "'yes' or 'no'. If yes, an IPv6 subnet will be assigned to the machine (where available)." = None,
            enable_private_network: "'yes' or 'no'. If yes, private networking support will be added to the new server." = None,
            NETWORKID: "List of private networks to attach to this server. Use either this field or enable_private_network, not both." = None,
            label: "This is a text label that will be shown in the control panel." = None,
            SSHKEYID: "List of SSH keys to apply to this server on install (only valid for Linux/FreeBSD). See v1/sshkey/list. Separate keys with commas." = None,
            auto_backups: "'yes' or 'no'. If yes, automatic backups will be enabled for this server (these have an extra charge associated with them)." = None,
            APPID: "If launching an application (OSID 186), this is the APPID to launch. See v1/app/list." = None,
            userdata: "Base64 encoded user-data" = None,
            notify_activate: "(optional, default 'yes') 'yes' or 'no'. If yes, an activation email will be sent when the server is ready." = None,
            ddos_protection: "(optional, default 'no') 'yes' or 'no'. If yes, DDOS protection will be enabled on the subscription (there is an additional charge for this)." = None,
            reserved_ip_v4: "IP address of the floating IP to use as the main IP of this server." = None,
            hostname: "The hostname to assign to this server." = None,
            tag: "The tag to assign to this server." = None,
            FIREWALLGROUPID: "The firewall group to assign to this server. See /v1/firewall/group_list." = None,
        ):
        assert DCID and isinstance(DCID, int), "DCID must be integer"
        assert VPSPLANID and isinstance(VPSPLANID, int), "VPSPLANID must be integer"
        assert OSID and isinstance(OSID, int), "OSID must be integer"
        assert ipxe_chain_url and isinstance(ipxe_chain_url, str), "ipxe_chain_url must be string"
        assert ISOID and isinstance(ISOID, str), "ISOID must be string"
        assert SCRIPTID and isinstance(SCRIPTID, int), "SCRIPTID must be integer"
        assert SNAPSHOTID and isinstance(SNAPSHOTID, str), "SNAPSHOTID must be string"
        assert enable_ipv6 and isinstance(enable_ipv6, str), "enable_ipv6 must be string"
        assert enable_private_network and isinstance(enable_private_network, str), "enable_private_network must be string"
        assert NETWORKID and isinstance(NETWORKID, list), "NETWORKID must be list"
        assert label and isinstance(label, str), "label must be string"
        assert SSHKEYID and isinstance(SSHKEYID, str), "SSHKEYID must be string"
        assert auto_backups and isinstance(auto_backups, str), "auto_backups must be string"
        assert APPID and isinstance(APPID, int), "APPID must be integer"
        assert userdata and isinstance(userdata, str), "userdata must be string"
        assert notify_activate and isinstance(notify_activate, str), "notify_activate must be string"
        assert ddos_protection and isinstance(ddos_protection, str), "ddos_protection must be string"
        assert reserved_ip_v4 and isinstance(reserved_ip_v4, str), "reserved_ip_v4 must be string"
        assert hostname and isinstance(hostname, str), "hostname must be string"
        assert tag and isinstance(tag, str), "tag must be string"
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        return self.request("post", "/v1/server/create", {"DCID": DCID, "VPSPLANID": VPSPLANID, "OSID": OSID, "ipxe_chain_url": ipxe_chain_url, "ISOID": ISOID, "SCRIPTID": SCRIPTID, "SNAPSHOTID": SNAPSHOTID, "enable_ipv6": enable_ipv6, "enable_private_network": enable_private_network, "NETWORKID": NETWORKID, "label": label, "SSHKEYID": SSHKEYID, "auto_backups": auto_backups, "APPID": APPID, "userdata": userdata, "notify_activate": notify_activate, "ddos_protection": ddos_protection, "reserved_ip_v4": reserved_ip_v4, "hostname": hostname, "tag": tag, "FIREWALLGROUPID": FIREWALLGROUPID})

    def create_snapshot_v1(self,
            SUBID: "Identifier of the virtual machine to create a snapshot from.  See v1/server/list",
            description: "Description of snapshot contents" = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert description and isinstance(description, str), "description must be string"
        return self.request("post", "/v1/snapshot/create", {"SUBID": SUBID, "description": description})

    def create_sshkey_v1(self,
            name: "Name of the SSH key",
            ssh_key: "SSH public key (in authorized_keys format)",
        ):
        assert name and isinstance(name, str), "name must be string"
        assert ssh_key and isinstance(ssh_key, str), "ssh_key must be string"
        return self.request("post", "/v1/sshkey/create", {"name": name, "ssh_key": ssh_key})

    def create_startupscript_v1(self,
            name: "Name of the newly created startup script.",
            script: "Startup script contents.",
            _type: "Type of startup script. Default is 'boot'." = None,
        ):
        assert name and isinstance(name, str), "name must be string"
        assert script and isinstance(script, str), "script must be string"
        assert _type and isinstance(_type, str), "type must be string"
        return self.request("post", "/v1/startupscript/create", {"name": name, "script": script, "type": _type})

    def create_user_v1(self,
            email: "Email address for this user",
            name: "Name for this user",
            acls: "List of ACLs that this user should have.  See /v1/user/list for information on possible ACLs",
            api_enabled: "'yes' or 'no'. If yes, this user's API key will work on api.vultr.com.  Default is yes" = None,
        ):
        assert email and isinstance(email, str), "email must be string"
        assert name and isinstance(name, str), "name must be string"
        assert api_enabled and isinstance(api_enabled, str), "api_enabled must be string"
        assert acls and isinstance(acls, list), "acls must be list"
        return self.request("post", "/v1/user/create", {"email": email, "name": name, "api_enabled": api_enabled, "acls": acls})

    def delete_block_v1(self,
            SUBID: "ID of the block storage subscription to delete",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/block/delete", {"SUBID": SUBID})

    def delete_domain_dns_v1(self,
            domain: "Domain name to delete",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        return self.request("post", "/v1/dns/delete_domain", {"domain": domain})

    def delete_record_dns_v1(self,
            domain: "Domain name to delete record from",
            RECORDID: "ID of record to delete (see /dns/records)",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        assert RECORDID and isinstance(RECORDID, int), "RECORDID must be integer"
        return self.request("post", "/v1/dns/delete_record", {"domain": domain, "RECORDID": RECORDID})

    def delete_user_v1(self,
            USERID: "ID of the user to delete",
        ):
        assert USERID and isinstance(USERID, int), "USERID must be integer"
        return self.request("post", "/v1/user/delete", {"USERID": USERID})

    def destroy_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/baremetal/destroy", {"SUBID": SUBID})

    def destroy_ipv4_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            ip: "IPv4 address to remove.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ip and isinstance(ip, str), "ip must be string"
        return self.request("post", "/v1/server/destroy_ipv4", {"SUBID": SUBID, "ip": ip})

    def destroy_iso_v1(self,
            ISOID: "Unique identifier for this ISO image. These can be found using the v1/iso/list call.",
        ):
        assert ISOID and isinstance(ISOID, int), "ISOID must be integer"
        return self.request("post", "/v1/iso/destroy", {"ISOID": ISOID})

    def destroy_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/loadbalancer/destroy", {"SUBID": SUBID})

    def destroy_network_v1(self,
            NETWORKID: "Unique identifier for this network.  These can be found using the v1/network/list call.",
        ):
        assert NETWORKID and isinstance(NETWORKID, str), "NETWORKID must be string"
        return self.request("post", "/v1/network/destroy", {"NETWORKID": NETWORKID})

    def destroy_objectstorage_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/objectstorage/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/objectstorage/destroy", {"SUBID": SUBID})

    def destroy_reservedip_v1(self,
            ip_address: "Reserved IP to remove from your account.",
        ):
        assert ip_address and isinstance(ip_address, str), "ip_address must be string"
        return self.request("post", "/v1/reservedip/destroy", {"ip_address": ip_address})

    def destroy_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/destroy", {"SUBID": SUBID})

    def destroy_snapshot_v1(self,
            SNAPSHOTID: "Unique identifier for this snapshot.  These can be found using the v1/snapshot/list call.",
        ):
        assert SNAPSHOTID and isinstance(SNAPSHOTID, str), "SNAPSHOTID must be string"
        return self.request("post", "/v1/snapshot/destroy", {"SNAPSHOTID": SNAPSHOTID})

    def destroy_sshkey_v1(self,
            SSHKEYID: "Unique identifier for this SSH key.  These can be found using the v1/sshkey/list call.",
        ):
        assert SSHKEYID and isinstance(SSHKEYID, str), "SSHKEYID must be string"
        return self.request("post", "/v1/sshkey/destroy", {"SSHKEYID": SSHKEYID})

    def destroy_startupscript_v1(self,
            SCRIPTID: "Unique identifier for this startup script. These can be found using the v1/startupscript/list call.",
        ):
        assert SCRIPTID and isinstance(SCRIPTID, str), "SCRIPTID must be string"
        return self.request("post", "/v1/startupscript/destroy", {"SCRIPTID": SCRIPTID})

    def detach_block_v1(self,
            SUBID: "ID of the block storage subscription to detach",
            live: "'yes' or 'no'.  If 'yes', this will be detached from the instance without a restart. (default is 'no')" = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert live and isinstance(live, str), "live must be string"
        return self.request("post", "/v1/block/detach", {"SUBID": SUBID, "live": live})

    def detach_reservedip_v1(self,
            ip_address: "Reserved IP to be detached. Include the subnet size in this parameter (e.g: /32 or /64).",
            detach_SUBID: "Unique identifier of the target server.",
        ):
        assert ip_address and isinstance(ip_address, str), "ip_address must be string"
        assert detach_SUBID and isinstance(detach_SUBID, int), "detach_SUBID must be integer"
        return self.request("post", "/v1/reservedip/detach", {"ip_address": ip_address, "detach_SUBID": detach_SUBID})

    def dnssec_enable_dns_v1(self,
            domain: "Domain name to update record",
            enable: "'yes' or 'no'.  If yes, DNSSEC will be enabled for the given domain",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        assert enable and isinstance(enable, str), "enable must be string"
        return self.request("post", "/v1/dns/dnssec_enable", {"domain": domain, "enable": enable})

    def dnssec_info_dns_v1(self,
            domain: "Domain from which to gather DNSSEC keys.",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        return self.request("get", "/v1/dns/dnssec_info", {"domain": domain})

    def firewall_group_set_server_v1(self,
            SUBID: "Unique identifier for this subscription. See v1/server/list.",
            FIREWALLGROUPID: "The firewall group to apply to this server. A value of \"0\" means \"no firewall group\". See /v1/firewall/group_list.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        return self.request("post", "/v1/server/firewall_group_set", {"SUBID": SUBID, "FIREWALLGROUPID": FIREWALLGROUPID})

    def forward_rule_create_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
            frontend_protocol: "Endpoint protocol on load balancer side. Possible values: \"http\", \"https\", \"tcp\".",
            frontend_port: "Endpoint port on load balancer side.",
            backend_protocol: "Endpoint protocol on instance side. Possible values: \"http\", \"https\", \"tcp\".",
            backend_port: "Endpoint port on instance side.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert frontend_protocol and isinstance(frontend_protocol, str), "frontend_protocol must be string"
        assert frontend_port and isinstance(frontend_port, int), "frontend_port must be integer"
        assert backend_protocol and isinstance(backend_protocol, str), "backend_protocol must be string"
        assert backend_port and isinstance(backend_port, int), "backend_port must be integer"
        return self.request("post", "/v1/loadbalancer/forward_rule_create", {"SUBID": SUBID, "frontend_protocol": frontend_protocol, "frontend_port": frontend_port, "backend_protocol": backend_protocol, "backend_port": backend_port})

    def forward_rule_delete_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
            RULEID: "Unique identifier of a forwarding rule. This can be found using the \"v1/loadbalancer/forward_rule_list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert RULEID and isinstance(RULEID, str), "RULEID must be string"
        return self.request("post", "/v1/loadbalancer/forward_rule_delete", {"SUBID": SUBID, "RULEID": RULEID})

    def forward_rule_list_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/forward_rule_list", {"SUBID": SUBID})

    def generic_info_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/generic_info", {"SUBID": SUBID})

    def generic_update_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
            label: "Label of your load balancer" = None,
            balancing_algorithm: "Balancing algorithm. Possible values: \"roundrobin\", \"leastconn\"." = None,
            sticky_sessions: "Enables sticky sessions for your load balancer - valid options are on or off." = None,
            cookie_name: "Name for your stick session." = None,
            ssl_redirect: "Force HTTP to HTTPS." = None,
            proxy_protocol: "(optionals) Enables proxy protocol - valid options are on or off" = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        assert balancing_algorithm and isinstance(balancing_algorithm, str), "balancing_algorithm must be string"
        assert sticky_sessions and isinstance(sticky_sessions, str), "sticky_sessions must be string"
        assert cookie_name and isinstance(cookie_name, str), "cookie_name must be string"
        assert ssl_redirect and isinstance(ssl_redirect, boolean), "ssl_redirect must be boolean"
        assert proxy_protocol and isinstance(proxy_protocol, str), "proxy_protocol must be string"
        return self.request("post", "/v1/loadbalancer/generic_update", {"SUBID": SUBID, "label": label, "balancing_algorithm": balancing_algorithm, "sticky_sessions": sticky_sessions, "cookie_name": cookie_name, "ssl_redirect": ssl_redirect, "proxy_protocol": proxy_protocol})

    def get_app_info_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/baremetal/get_app_info", {"SUBID": SUBID})

    def get_app_info_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/get_app_info", {"SUBID": SUBID})

    def get_user_data_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/baremetal/get_user_data", {"SUBID": SUBID})

    def get_user_data_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/get_user_data", {"SUBID": SUBID})

    def group_create_firewall_v1(self,
            description: "Description of firewall group." = None,
        ):
        assert description and isinstance(description, str), "description must be string"
        return self.request("post", "/v1/firewall/group_create", {"description": description})

    def group_delete_firewall_v1(self,
            FIREWALLGROUPID: "Firewall group to delete.",
        ):
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        return self.request("post", "/v1/firewall/group_delete", {"FIREWALLGROUPID": FIREWALLGROUPID})

    def group_list_firewall_v1(self,
            FIREWALLGROUPID: "Filter result set to only contain this firewall group." = None,
        ):
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        return self.request("get", "/v1/firewall/group_list", {"FIREWALLGROUPID": FIREWALLGROUPID})

    def group_set_description_firewall_v1(self,
            FIREWALLGROUPID: "Firewall group to update.",
            description: "Description of firewall group.",
        ):
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        assert description and isinstance(description, str), "description must be string"
        return self.request("post", "/v1/firewall/group_set_description", {"FIREWALLGROUPID": FIREWALLGROUPID, "description": description})

    def halt_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/baremetal/halt", {"SUBID": SUBID})

    def halt_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/halt", {"SUBID": SUBID})

    def health_check_info_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/health_check_info", {"SUBID": SUBID})

    def health_check_update_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
            protocol: "Connection protocol. Possible values: \"http\", \"https\"." = None,
            port: "Connection port." = None,
            check_interval: "Time in seconds to perform health check." = None,
            response_timeout: "Time in seconds to wait for a health check response." = None,
            unhealthy_threshold: "Number of failed attempts encountered before failover." = None,
            healthy_threshold: "Number of failed attempts encountered before failover." = None,
            path: "Path to page used for health check. The target page must return an HTTP 200 success code." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert protocol and isinstance(protocol, str), "protocol must be string"
        assert port and isinstance(port, int), "port must be integer"
        assert check_interval and isinstance(check_interval, int), "check_interval must be integer"
        assert response_timeout and isinstance(response_timeout, int), "response_timeout must be integer"
        assert unhealthy_threshold and isinstance(unhealthy_threshold, int), "unhealthy_threshold must be integer"
        assert healthy_threshold and isinstance(healthy_threshold, int), "healthy_threshold must be integer"
        assert path and isinstance(path, str), "path must be string"
        return self.request("post", "/v1/loadbalancer/health_check_update", {"SUBID": SUBID, "protocol": protocol, "port": port, "check_interval": check_interval, "response_timeout": response_timeout, "unhealthy_threshold": unhealthy_threshold, "healthy_threshold": healthy_threshold, "path": path})

    def info_account_v1(self):
        return self.request("get", "/v1/account/info", {})

    def info_auth_v1(self):
        return self.request("get", "/v1/auth/info", {})

    def instance_attach_loadbalancer_v1(self,
            SUBID: "Unique identifier of LoadBalancer subscription to attach to.",
            backendNode: "Unique identifier (SUBID) of VPS or baremetal subscription to attach.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert backendNode and isinstance(backendNode, int), "backendNode must be integer"
        return self.request("post", "/v1/loadbalancer/instance_attach", {"SUBID": SUBID, "backendNode": backendNode})

    def instance_detach_loadbalancer_v1(self,
            SUBID: "Unique identifier of LoadBalancer subscription to detach from.",
            backendNode: "Unique identifier (SUBID) of VPS or baremetal subscription to detach.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert backendNode and isinstance(backendNode, int), "backendNode must be integer"
        return self.request("post", "/v1/loadbalancer/instance_detach", {"SUBID": SUBID, "backendNode": backendNode})

    def instance_list_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/instance_list", {"SUBID": SUBID})

    def ipv6_enable_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/baremetal/ipv6_enable", {"SUBID": SUBID})

    def ipv6_enable_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/ipv6_enable", {"SUBID": SUBID})

    def iso_attach_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the /v1/server/list call.",
            ISOID: "The ISO that will be mounted. See the /v1/iso/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ISOID and isinstance(ISOID, int), "ISOID must be integer"
        return self.request("post", "/v1/server/iso_attach", {"SUBID": SUBID, "ISOID": ISOID})

    def iso_detach_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the /v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/iso_detach", {"SUBID": SUBID})

    def iso_status_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the /v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/iso_status", {"SUBID": SUBID})

    def label_set_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
            label: "This is a text label that will be shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/baremetal/label_set", {"SUBID": SUBID, "label": label})

    def label_set_block_v1(self,
            SUBID: "ID of the block storage subscription.",
            label: "Text label that will be shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/block/label_set", {"SUBID": SUBID, "label": label})

    def label_set_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
            label: "Text label that will be shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/loadbalancer/label_set", {"SUBID": SUBID, "label": label})

    def label_set_objectstorage_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/objectstorage/list call.",
            label: "Text label that will be shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/objectstorage/label_set", {"SUBID": SUBID, "label": label})

    def label_set_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            label: "This is a text label that will be shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("post", "/v1/server/label_set", {"SUBID": SUBID, "label": label})

    def list_app_v1(self):
        return self.request("get", "/v1/app/list", {})

    def list_backup_v1(self,
            SUBID: "Filter result set to only contain backups of this subscription object." = None,
            BACKUPID: "Filter result set to only contain this backup." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert BACKUPID and isinstance(BACKUPID, str), "BACKUPID must be string"
        return self.request("get", "/v1/backup/list", {"SUBID": SUBID, "BACKUPID": BACKUPID})

    def list_baremetal_plans_v1(self):
        return self.request("get", "/v1/plans/list_baremetal", {})

    def list_baremetal_v1(self,
            SUBID: "Unique identifier of a subscription. Only the subscription object will be returned." = None,
            tag: "A tag string. Only subscription objects with this tag will be returned." = None,
            label: "A text label string. Only subscription objects with this text label will be returned." = None,
            main_ip: "An IPv4 address. Only the subscription matching this IPv4 address will be returned." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert tag and isinstance(tag, str), "tag must be string"
        assert label and isinstance(label, str), "label must be string"
        assert main_ip and isinstance(main_ip, str), "main_ip must be string"
        return self.request("get", "/v1/baremetal/list", {"SUBID": SUBID, "tag": tag, "label": label, "main_ip": main_ip})

    def list_block_v1(self,
            SUBID: "Unique identifier of a subscription. Only the subscription object will be returned." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/block/list", {"SUBID": SUBID})

    def list_cluster_objectstorage_v1(self):
        return self.request("get", "/v1/objectstorage/list_cluster", {})

    def list_dns_v1(self):
        return self.request("get", "/v1/dns/list", {})

    def list_ipv4_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/baremetal/list_ipv4", {"SUBID": SUBID})

    def list_ipv4_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            public_network: "'yes' or 'no'. If 'yes', include information about the public network adapter (such as MAC address) with the \"main_ip\" entry." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert public_network and isinstance(public_network, str), "public_network must be string"
        return self.request("get", "/v1/server/list_ipv4", {"SUBID": SUBID, "public_network": public_network})

    def list_ipv6_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/baremetal/list_ipv6", {"SUBID": SUBID})

    def list_ipv6_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/list_ipv6", {"SUBID": SUBID})

    def list_iso_v1(self):
        return self.request("get", "/v1/iso/list", {})

    def list_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. Only the subscription object will be returned." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/list", {"SUBID": SUBID})

    def list_network_v1(self):
        return self.request("get", "/v1/network/list", {})

    def list_objectstorage_v1(self,
            include_s3: "(optional, default 'yes') 'yes' or 'no'. If 'yes', include S3 keys with each subscription entry." = None,
            SUBID: "Unique identifier of a subscription. Only the subscription object will be returned." = None,
            label: "A text label string. Only subscription objects with this text label will be returned." = None,
        ):
        assert include_s3 and isinstance(include_s3, str), "include_s3 must be string"
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert label and isinstance(label, str), "label must be string"
        return self.request("get", "/v1/objectstorage/list", {"include_s3": include_s3, "SUBID": SUBID, "label": label})

    def list_os_v1(self):
        return self.request("get", "/v1/os/list", {})

    def list_plans_v1(self,
            _type: "The type of plans to return. Possible values: \"all\", \"vc2\", \"ssd\", \"vdc2\", \"dedicated\", \"vc2z\"." = None,
        ):
        assert _type and isinstance(_type, str), "type must be string"
        return self.request("get", "/v1/plans/list", {"type": _type})

    def list_public_iso_v1(self):
        return self.request("get", "/v1/iso/list_public", {})

    def list_regions_v1(self,
            availability: "'yes' or 'no'. If 'yes', include the current availability with each region entry." = None,
        ):
        assert availability and isinstance(availability, str), "availability must be string"
        return self.request("get", "/v1/regions/list", {"availability": availability})

    def list_reservedip_v1(self):
        return self.request("get", "/v1/reservedip/list", {})

    def list_server_v1(self,
            SUBID: "Unique identifier of a subscription. Only the subscription object will be returned." = None,
            tag: "A tag string. Only subscription objects with this tag will be returned." = None,
            label: "A text label string. Only subscription objects with this text label will be returned." = None,
            main_ip: "An IPv4 address. Only the subscription matching this IPv4 address will be returned." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert tag and isinstance(tag, str), "tag must be string"
        assert label and isinstance(label, str), "label must be string"
        assert main_ip and isinstance(main_ip, str), "main_ip must be string"
        return self.request("get", "/v1/server/list", {"SUBID": SUBID, "tag": tag, "label": label, "main_ip": main_ip})

    def list_snapshot_v1(self,
            SNAPSHOTID: "Filter result set to only contain this snapshot." = None,
        ):
        assert SNAPSHOTID and isinstance(SNAPSHOTID, str), "SNAPSHOTID must be string"
        return self.request("get", "/v1/snapshot/list", {"SNAPSHOTID": SNAPSHOTID})

    def list_sshkey_v1(self):
        return self.request("get", "/v1/sshkey/list", {})

    def list_startupscript_v1(self):
        return self.request("get", "/v1/startupscript/list", {})

    def list_user_v1(self):
        return self.request("get", "/v1/user/list", {})

    def list_vc2_plans_v1(self):
        return self.request("get", "/v1/plans/list_vc2", {})

    def list_vc2z_plans_v1(self):
        return self.request("get", "/v1/plans/list_vc2z", {})

    def list_vdc2_plans_v1(self):
        return self.request("get", "/v1/plans/list_vdc2", {})

    def neighbors_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/neighbors", {"SUBID": SUBID})

    def os_change_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
            OSID: "Operating system to use. See /v1/baremetal/os_change_list.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert OSID and isinstance(OSID, int), "OSID must be integer"
        return self.request("post", "/v1/baremetal/os_change", {"SUBID": SUBID, "OSID": OSID})

    def os_change_list_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/baremetal/os_change_list", {"SUBID": SUBID})

    def os_change_list_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/os_change_list", {"SUBID": SUBID})

    def os_change_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            OSID: "Operating system to use. See /v1/server/os_change_list.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert OSID and isinstance(OSID, int), "OSID must be integer"
        return self.request("post", "/v1/server/os_change", {"SUBID": SUBID, "OSID": OSID})

    def private_network_disable_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            NETWORKID: "Unique identifier for the private network to remove from this subscription. This field is optional if there is only one private network in a given location. See the v1/network/list call." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert NETWORKID and isinstance(NETWORKID, str), "NETWORKID must be string"
        return self.request("post", "/v1/server/private_network_disable", {"SUBID": SUBID, "NETWORKID": NETWORKID})

    def private_network_enable_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            NETWORKID: "Unique identifier for the private network to attach to this subscription.  This field is optional if there is only one private network in a given location.  See the v1/network/list call." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert NETWORKID and isinstance(NETWORKID, str), "NETWORKID must be string"
        return self.request("post", "/v1/server/private_network_enable", {"SUBID": SUBID, "NETWORKID": NETWORKID})

    def private_networks_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/private_networks", {"SUBID": SUBID})

    def reboot_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/baremetal/reboot", {"SUBID": SUBID})

    def reboot_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/reboot", {"SUBID": SUBID})

    def records_dns_v1(self,
            domain: "Domain to list records for",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        return self.request("get", "/v1/dns/records", {"domain": domain})

    def reinstall_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/baremetal/reinstall", {"SUBID": SUBID})

    def reinstall_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
            hostname: "The hostname to assign to this server." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert hostname and isinstance(hostname, str), "hostname must be string"
        return self.request("post", "/v1/server/reinstall", {"SUBID": SUBID, "hostname": hostname})

    def resize_block_v1(self,
            SUBID: "ID of the block storage subscription to resize",
            size_gb: "New size (in GB) of the block storage subscription",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert size_gb and isinstance(size_gb, int), "size_gb must be integer"
        return self.request("post", "/v1/block/resize", {"SUBID": SUBID, "size_gb": size_gb})

    def restore_backup_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
            BACKUPID: "BACKUPID (see v1/backup/list) to restore to this instance",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert BACKUPID and isinstance(BACKUPID, str), "BACKUPID must be string"
        return self.request("post", "/v1/server/restore_backup", {"SUBID": SUBID, "BACKUPID": BACKUPID})

    def restore_snapshot_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
            SNAPSHOTID: "SNAPSHOTID (see v1/snapshot/list) to restore to this instance",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert SNAPSHOTID and isinstance(SNAPSHOTID, str), "SNAPSHOTID must be string"
        return self.request("post", "/v1/server/restore_snapshot", {"SUBID": SUBID, "SNAPSHOTID": SNAPSHOTID})

    def reverse_default_ipv4_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            ip: "IPv4 address used in the reverse DNS update. These can be found with the v1/server/list_ipv4 call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ip and isinstance(ip, str), "ip must be string"
        return self.request("post", "/v1/server/reverse_default_ipv4", {"SUBID": SUBID, "ip": ip})

    def reverse_delete_ipv6_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            ip: "IPv6 address used in the reverse DNS update. These can be found with the v1/server/reverse_list_ipv6 call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ip and isinstance(ip, str), "ip must be string"
        return self.request("post", "/v1/server/reverse_delete_ipv6", {"SUBID": SUBID, "ip": ip})

    def reverse_list_ipv6_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/reverse_list_ipv6", {"SUBID": SUBID})

    def reverse_set_ipv4_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            ip: "IPv4 address used in the reverse DNS update. These can be found with the v1/server/list_ipv4 call.",
            entry: "reverse DNS entry.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ip and isinstance(ip, str), "ip must be string"
        assert entry and isinstance(entry, str), "entry must be string"
        return self.request("post", "/v1/server/reverse_set_ipv4", {"SUBID": SUBID, "ip": ip, "entry": entry})

    def reverse_set_ipv6_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            ip: "IPv6 address used in the reverse DNS update. These can be found with the v1/server/list_ipv6 or v1/server/reverse_list_ipv6 calls.",
            entry: "reverse DNS entry.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ip and isinstance(ip, str), "ip must be string"
        assert entry and isinstance(entry, str), "entry must be string"
        return self.request("post", "/v1/server/reverse_set_ipv6", {"SUBID": SUBID, "ip": ip, "entry": entry})

    def rule_create_firewall_v1(self,
            FIREWALLGROUPID: "Target firewall group. See /v1/firewall/group_list.",
            direction: "Direction of rule. Possible values: \"in\".",
            ip_type: "IP address type. Possible values: \"v4\", \"v6\".",
            protocol: "Protocol type. Possible values: \"icmp\", \"tcp\", \"udp\", \"gre\".",
            subnet: "IP address representing a subnet. The IP address format must match with the \"ip_type\" parameter value.",
            subnet_size: "IP prefix size in bits.",
            port: "TCP/UDP only. This field can be an integer value specifying a port or a colon separated port range." = None,
            notes: "This field supports notes up to 255 characters." = None,
            source: "If the source string is given a value of \"cloudflare\" subnet and subnet_size will both be ignored, this will allow all of Cloudflare's IP space through the firewall. Possible values: \"\", \"cloudflare\"." = None,
        ):
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        assert direction and isinstance(direction, str), "direction must be string"
        assert ip_type and isinstance(ip_type, str), "ip_type must be string"
        assert protocol and isinstance(protocol, str), "protocol must be string"
        assert subnet and isinstance(subnet, str), "subnet must be string"
        assert subnet_size and isinstance(subnet_size, int), "subnet_size must be integer"
        assert port and isinstance(port, str), "port must be string"
        assert notes and isinstance(notes, str), "notes must be string"
        assert source and isinstance(source, str), "source must be string"
        return self.request("post", "/v1/firewall/rule_create", {"FIREWALLGROUPID": FIREWALLGROUPID, "direction": direction, "ip_type": ip_type, "protocol": protocol, "subnet": subnet, "subnet_size": subnet_size, "port": port, "notes": notes, "source": source})

    def rule_delete_firewall_v1(self,
            FIREWALLGROUPID: "Target firewall group. See /v1/firewall/group_list.",
            rulenumber: "Rule number to delete. See /v1/firewall/rule_list.",
        ):
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        assert rulenumber and isinstance(rulenumber, int), "rulenumber must be integer"
        return self.request("post", "/v1/firewall/rule_delete", {"FIREWALLGROUPID": FIREWALLGROUPID, "rulenumber": rulenumber})

    def rule_list_firewall_v1(self,
            FIREWALLGROUPID: "Target firewall group. See /v1/firewall/group_list.",
            direction: "Direction of firewall rules. Possible values: \"in\".",
            ip_type: "IP address type. Possible values: \"v4\", \"v6\".",
        ):
        assert FIREWALLGROUPID and isinstance(FIREWALLGROUPID, str), "FIREWALLGROUPID must be string"
        assert direction and isinstance(direction, str), "direction must be string"
        assert ip_type and isinstance(ip_type, str), "ip_type must be string"
        return self.request("get", "/v1/firewall/rule_list", {"FIREWALLGROUPID": FIREWALLGROUPID, "direction": direction, "ip_type": ip_type})

    def s3key_regenerate_objectstorage_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/objectstorage/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/objectstorage/s3key_regenerate", {"SUBID": SUBID})

    def set_user_data_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
            userdata: "Base64 encoded user-data",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert userdata and isinstance(userdata, str), "userdata must be string"
        return self.request("post", "/v1/baremetal/set_user_data", {"SUBID": SUBID, "userdata": userdata})

    def set_user_data_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            userdata: "Base64 encoded user-data",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert userdata and isinstance(userdata, str), "userdata must be string"
        return self.request("post", "/v1/server/set_user_data", {"SUBID": SUBID, "userdata": userdata})

    def soa_info_dns_v1(self,
            domain: "Domain from which to gather SOA information",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        return self.request("get", "/v1/dns/soa_info", {"domain": domain})

    def soa_update_dns_v1(self,
            domain: "Domain name to update record",
            nsprimary: "(Optional) Primary nameserver to store in the SOA record",
            email: "(Optional) Administrative email to store in the SOA record",
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        assert nsprimary and isinstance(nsprimary, str), "nsprimary must be string"
        assert email and isinstance(email, str), "email must be string"
        return self.request("post", "/v1/dns/soa_update", {"domain": domain, "nsprimary": nsprimary, "email": email})

    def ssl_add_loadbalancer_v1(self,
            SUBID: "Unique identifier of LoadBalancer subscription.",
            ssl_private_key: "The SSL certificates private key.",
            ssl_chain: "The SSL certificate chain." = None,
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert ssl_private_key and isinstance(ssl_private_key, str), "ssl_private_key must be string"
        assert ssl_chain and isinstance(ssl_chain, str), "ssl_chain must be string"
        return self.request("post", "/v1/loadbalancer/ssl_add", {"SUBID": SUBID, "ssl_private_key": ssl_private_key, "ssl_chain": ssl_chain})

    def ssl_info_loadbalancer_v1(self,
            SUBID: "Unique identifier of a load balancer subscription. This can be found using the \"v1/loadbalancer/list\" call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/loadbalancer/ssl_info", {"SUBID": SUBID})

    def ssl_remove_loadbalancer_v1(self,
            SUBID: "Unique identifier of LoadBalancer subscription.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/loadbalancer/ssl_remove", {"SUBID": SUBID})

    def start_server_v1(self,
            SUBID: "Unique identifier for this subscription.  These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("post", "/v1/server/start", {"SUBID": SUBID})

    def tag_set_baremetal_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/baremetal/list call.",
            tag: "The tag to assign to this server. This tag is shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert tag and isinstance(tag, str), "tag must be string"
        return self.request("post", "/v1/baremetal/tag_set", {"SUBID": SUBID, "tag": tag})

    def tag_set_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            tag: "The tag to assign to this server. This tag is shown in the control panel.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert tag and isinstance(tag, str), "tag must be string"
        return self.request("post", "/v1/server/tag_set", {"SUBID": SUBID, "tag": tag})

    def update_record_dns_v1(self,
            domain: "Domain name to update record",
            RECORDID: "ID of record to update (see /dns/records)",
            name: "Name (subdomain) of record" = None,
            data: "Data for this record" = None,
            ttl: "TTL of this record" = None,
            priority: "(only required for MX and SRV) Priority of this record (omit the priority from the data)" = None,
        ):
        assert domain and isinstance(domain, str), "domain must be string"
        assert RECORDID and isinstance(RECORDID, int), "RECORDID must be integer"
        assert name and isinstance(name, str), "name must be string"
        assert data and isinstance(data, str), "data must be string"
        assert ttl and isinstance(ttl, int), "ttl must be integer"
        assert priority and isinstance(priority, int), "priority must be integer"
        return self.request("post", "/v1/dns/update_record", {"domain": domain, "RECORDID": RECORDID, "name": name, "data": data, "ttl": ttl, "priority": priority})

    def update_sshkey_v1(self,
            SSHKEYID: "SSHKEYID of key to update (see /v1/sshkey/list)",
            name: "New name for the SSH key" = None,
            ssh_key: "New SSH key contents" = None,
        ):
        assert SSHKEYID and isinstance(SSHKEYID, str), "SSHKEYID must be string"
        assert name and isinstance(name, str), "name must be string"
        assert ssh_key and isinstance(ssh_key, str), "ssh_key must be string"
        return self.request("post", "/v1/sshkey/update", {"SSHKEYID": SSHKEYID, "name": name, "ssh_key": ssh_key})

    def update_startupscript_v1(self,
            SCRIPTID: "SCRIPTID of script to update (see /v1/startupscript/list).",
            name: "New name for the startup script." = None,
            script: "New startup script contents." = None,
        ):
        assert SCRIPTID and isinstance(SCRIPTID, int), "SCRIPTID must be integer"
        assert name and isinstance(name, str), "name must be string"
        assert script and isinstance(script, str), "script must be string"
        return self.request("post", "/v1/startupscript/update", {"SCRIPTID": SCRIPTID, "name": name, "script": script})

    def update_user_v1(self,
            USERID: "ID of the user to update",
            email: "New email address for this user" = None,
            name: "New name for this user" = None,
            password: "New password for this user" = None,
            api_enabled: "'yes' or 'no'. If yes, this user's API key will work on api.vultr.com" = None,
            acls: "List of ACLs that this user should have.  See /v1/user/list for information on possible ACLs" = None,
        ):
        assert USERID and isinstance(USERID, str), "USERID must be string"
        assert email and isinstance(email, str), "email must be string"
        assert name and isinstance(name, str), "name must be string"
        assert password and isinstance(password, str), "password must be string"
        assert api_enabled and isinstance(api_enabled, str), "api_enabled must be string"
        assert acls and isinstance(acls, list), "acls must be list"
        return self.request("post", "/v1/user/update", {"USERID": USERID, "email": email, "name": name, "password": password, "api_enabled": api_enabled, "acls": acls})

    def upgrade_plan_list_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        return self.request("get", "/v1/server/upgrade_plan_list", {"SUBID": SUBID})

    def upgrade_plan_server_v1(self,
            SUBID: "Unique identifier for this subscription. These can be found using the v1/server/list call.",
            VPSPLANID: "The new plan. See /v1/server/upgrade_plan_list.",
        ):
        assert SUBID and isinstance(SUBID, int), "SUBID must be integer"
        assert VPSPLANID and isinstance(VPSPLANID, int), "VPSPLANID must be integer"
        return self.request("post", "/v1/server/upgrade_plan", {"SUBID": SUBID, "VPSPLANID": VPSPLANID})
