class ResourceState:
    def __init__(self):
        self.state = 'Free'  # domyślnie ustawiamy stan zasobu na "Wolny"

    def occupy(self):
        if self.state == 'Free':
            self.state = 'Occupied'
        else:
            print("The resource is already occupied.")

    def release(self):
        if self.state == 'Occupied':
            self.state = 'Free'
        else:
            print("The resource is not occupied.")

    def service(self):
        if self.state == 'Occupied':
            self.state = 'Serviced'
        else:
            print("The resource is not occupied.")

    def check_state(self):
        return self.state