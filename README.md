AWS IP Validation
=================
Quick and dirty tool to validate if a list of IPv4 addresses is an AWS IP address.

Requirements
------------
* Python 3

Usage
-----
Create a line-separated list of IP addresses and save as a text file. Example:

    echo -e "99.150.96.4\n192.168.0.1\n172.0.4.2\n150.222.5.187\n201.2.54.5\n150.222.3.189" > data/input.txt

Run the `aws-ip` script against that file:

    $ ./aws-ip data/input.txt
    
Will output something similar to:

    Updating AWS IP database.. done
    Loaded 3166 entries
    150.222.3.185,MATCH,ap-southeast-1,EC2
    192.168.0.1,NO MATCH,-,-
    172.0.4.2,NO MATCH,-,-
    150.222.5.187,MATCH,eu-central-1,AMAZON
    201.2.54.5,NO MATCH,-,-
    150.222.3.189,MATCH,ap-southeast-1,AMAZON

The CSV content is printed to stdout, other messages to stderr -

    $ ./aws-ip data/input.txt > data/out.csv 
    Updating AWS IP database.. done
    Loaded 3166 entries

    $ cat data/out.csv
    150.222.3.185,MATCH,ap-southeast-1,EC2
    192.168.0.1,NO MATCH,-,-
    172.0.4.2,NO MATCH,-,-
    150.222.5.187,MATCH,eu-central-1,AMAZON
    201.2.54.5,NO MATCH,-,-
    150.222.3.189,MATCH,ap-southeast-1,AMAZON
