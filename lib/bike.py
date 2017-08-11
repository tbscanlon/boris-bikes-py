class Bike(object):
    def __init__(self, status = 'good'):
        self.status = status

    def is_working(self):
        return self.status == 'good'

    def damage(self):
        self.status == 'broken'
