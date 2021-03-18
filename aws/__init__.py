import os
import time
import json
import sys


class IpCache:
    """
    Downloads the AWS IP range database, or updates it if it's old.
    """
    AWS_IP_DATABASE = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    cidr_list = {}

    def __init__(self, cache_fn, max_age=86400):
        self.cache_fn = cache_fn
        self.max_age = max_age

    def download(self):
        """
        Downloads a fresh copy of the database.
        :return:
        """
        import urllib.request

        print("Updating AWS IP database..", end='', file=sys.stderr)
        urllib.request.urlretrieve(self.AWS_IP_DATABASE, self.cache_fn)
        print(" done", file=sys.stderr)

    def update(self):
        """
        Calls download() only if the database is missing or out of date.
        :return: bool
        """
        if not os.path.isfile(self.cache_fn) or (time.time() - os.stat(self.cache_fn).st_mtime > self.max_age):
            self.download()
            return True
        else:
            return False

    def load(self):
        """
        Loads the local database into memory, updates/downloads if required.
        :return:
        """
        self.update()
        self.cidr_list = {}

        with open(self.cache_fn, "r") as db:
            aws_data = json.load(db)
            db.close()

        for p in aws_data["prefixes"]:
            self.cidr_list[p["ip_prefix"]] = (p["region"], p["service"])

        print("Loaded {} entries".format(len(self.cidr_list)), file=sys.stderr)
