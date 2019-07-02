from pycomm.ab_comm.slc import Driver as SlcDriver


def check_connection(ip_address):
    d = SlcDriver()
    try:
        if d.open(ip_address):
            return True
    except Exception as e:
        return e


def generate_values(upto):
    nums = []
    for i in range(upto):
        nums.append(i)

    return nums


class Xcl:
    def __init__(self):
        self.tag_queue = []

    def queue_tag(self, tag):
        self.tag_queue.append(tag)

    def clear_queue(self):
        self.tag_queue = []































