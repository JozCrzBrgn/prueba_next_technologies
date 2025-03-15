class NaturalNumbers:
    def __init__(self):
        # Crear un conjunto con los números naturales del 1 al 100
        self.nat_numbers = set(range(1, 101))

    def extract(self, number):
        # Si el número no está en el conjunto devolver -1
        if number not in self.nat_numbers:
            return -1
        # Remover el número del conjunto
        self.nat_numbers.remove(number)

    def lost(self):
        # Devolver la lista de números faltantes
        return list(set(range(1, 101)) - self.nat_numbers)