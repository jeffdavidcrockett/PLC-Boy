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
        self.tag_queue = {'I': [], 'O': [], 'B': [],
                          'N': [], 'F': []}

    def queue_tag(self, tag):
        for key in self.tag_queue.keys():
            if tag[0] == key:
                self.tag_queue[key].append(tag)

    def tags_is_empty(self):
        state = False
        for val in self.tag_queue.values():
            if len(val) != 0:
                state = True

        return state

    def duplicate_tags_check(self, tag):
        for val in self.tag_queue.values():
            if tag in val:
                return True

        return False


    def clear_queue(self):
        self.tag_queue = {'I': [], 'O': [], 'B': [],
                          'N': [], 'F': []}


# test = Xcl()
# print test.tags_is_empty()




























