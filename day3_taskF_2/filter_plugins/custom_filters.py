class FilterModule(object):

    def filters(self):
        return {
            'srch': self.srch
        }

    def srch(self, somelist, label='Identity'):
        for item in somelist:
            if item['name'] == label:
                return "{}: {}".format(label, item['id'])
