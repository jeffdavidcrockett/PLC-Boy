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
    def __init__(self, ip):
        self.cur = SlcDriver()
        self.ip_address = ip
        self.cur.open(ip)

    def get_tag_value(self, tag):

        return self.cur.read_tag(tag)


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

    def extract_to_xclfile(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('PLC Values')
        slc_tool = Slc()

        style0 = xlwt.easyxf('font: name Arial, color-index red, bold on')
        style1 = xlwt.easyxf('font: name Arial')
        style2 = xlwt.easyxf('font: name Arial, bold on')
        style3 = xlwt.easyxf('font: name Arial; align: horiz left')

        ws.write(0, 0, 'Time', style0)
        ws.write(3, 0, 'Tag', style0)
        ws.write(3, 1, 'Value', style0)

        row_start = 4
        for key, value in self.tag_queue.items():
            if len(value) != 0:
                ws.write(row_start, 0, key, style2)
                row_start += 1
                for i in range(len(value)):
                    ws.write(row_start, 0, value[i], style1)
                    ws.write(row_start, 1, slc_tool.get_tag_value(value[i]), style3)
                    row_start += 1
                row_start += 1



        wb.save('test.xls')

# test = Xcl()
# test.extract_to_xclfile()




























