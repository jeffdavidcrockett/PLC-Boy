from pycomm.ab_comm.slc import Driver as SlcDriver
import xlwt


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


class Slc:
    def __init__(self):
        self.cur = SlcDriver()
        self.ip_address = None

    def set_ip_address(self, ip):
        self.ip_address = ip

    def open_connection(self):
        self.cur.open(self.ip_address)

    def close_connection(self):
        self.cur.close()

    def get_tag_value(self, tag):
        return self.cur.read_tag(tag)

    def check_tag(self, tag):
        if self.ip_address:
            self.open_connection()
            try:
                if self.cur.read_tag(tag):
                    self.close_connection()
                    return True
            except Exception as e:
                self.close_connection()
                return False


class Xcl:
    def __init__(self):
        self.tag_queue = {'I': [], 'O': [], 'B': [],
                          'N': [], 'F': [], 'T': []}
        self.style0 = xlwt.easyxf('font: name Arial, color-index red, bold on')
        self.style1 = xlwt.easyxf('font: name Arial')
        self.style2 = xlwt.easyxf('font: name Arial, bold on')
        self.style3 = xlwt.easyxf('font: name Arial; align: horiz left')
        self.sheet_name = 'PLC Values'
        self.file_name = 'test.xls'

    def queue_tag(self, tag):
        for key in self.tag_queue.keys():
            if tag[0] == key:
                self.tag_queue[key].append(tag)

    def tags_is_empty(self):
        state = True
        for val in self.tag_queue.values():
            if len(val) != 0:
                state = False

        return state

    def duplicate_tags_check(self, tag):
        for val in self.tag_queue.values():
            if tag in val:
                return True

        return False

    def clear_queue(self):
        self.tag_queue = {'I': [], 'O': [], 'B': [],
                          'N': [], 'F': []}

    def count_queue_tags(self):
        count = 0
        for val in self.tag_queue.values():
            count += len(val)

        return count

    def remove_tag(self, tag):
        for key in self.tag_queue.keys():
            if tag in self.tag_queue[key]:
                tag_index = self.tag_queue[key].index(tag)
                self.tag_queue[key].pop(tag_index)

    def extract_to_xclfile(self, slc_tool):
        wb = xlwt.Workbook()
        ws = wb.add_sheet(self.sheet_name)

        ws.write(0, 0, 'Time', self.style0)
        ws.write(3, 0, 'Tag', self.style0)
        ws.write(3, 1, 'Value', self.style0)

        row_start = 4
        for key, value in self.tag_queue.items():
            if len(value) != 0:
                ws.write(row_start, 0, key, self.style2)
                row_start += 1
                for i in range(len(value)):
                    ws.write(row_start, 0, value[i], self.style1)
                    ws.write(row_start, 1, slc_tool.get_tag_value(value[i]), self.style3)
                    row_start += 1
                row_start += 1

        wb.save(self.file_name)
