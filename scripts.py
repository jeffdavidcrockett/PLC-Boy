from pycomm.ab_comm.slc import Driver as SlcDriver


def check_connection(ip_address):
    d = SlcDriver()
    try:
        if d.open(ip_address):
            return 'Connection Successful'
    except Exception as e:
        return e


