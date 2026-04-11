from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.get_size() == 0:
            return None

        temp_list = []
        for item in self.pakuri_list:
            temp_list.append(item.get_species())

        return temp_list

    def get_stats(self, species):
        if self.get_size() == 0:
            return None

        for item in self.pakuri_list:
            if item.species == species:
                return [item.get_attack(), item.get_defense(), item.get_speed()]

        return None

    def sort_pakuri(self):
        self.pakuri_list.sort()

    def add_pakuri(self, species):
        if self.get_size() >= self.capacity:
            return False

        for item in self.pakuri_list:
            if item.get_species() == species:
                return False

        self.pakuri_list.append(Pakuri(species))
        return True

    def evolve_species(self, species):
        if self.get_size() == 0:
            return False

        for item in self.pakuri_list:
            if item.species == species:
                item.evolve()
                return True

        return False
