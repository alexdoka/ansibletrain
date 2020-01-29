class FilterModule(object):

    def filters(self):
        return {
            'rev': self.rev,
        }

    def rev(self, value):
        if type(value) != list:
            return str(value)[::-1]
        else:
            return value[::-1]