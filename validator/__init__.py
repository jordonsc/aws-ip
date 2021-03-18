from aws import IpCache
import ipaddress


class Validator:
    def __init__(self, ip_cache: IpCache):
        self.cache = ip_cache

    def examine(self, fn):
        with open(fn, "r") as in_data:
            ip_list = in_data.readlines()
            in_data.close()

        for ip in ip_list:
            ip = ip.strip()
            match = False

            for cidr, t in self.cache.cidr_list.items():
                if ipaddress.ip_address(ip) in ipaddress.ip_network(cidr):
                    print("{},MATCH,{},{}".format(ip, *t))
                    match = True
                    break

            if not match:
                print("{},NO MATCH,-,-".format(ip))
