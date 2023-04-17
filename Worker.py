class Worker:
    id = 0

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "id = " + str(self.id)