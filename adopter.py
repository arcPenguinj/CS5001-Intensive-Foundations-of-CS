class Adopter:
    def __init__(self, name, species, has_pets):
        self.name = name
        self.species_choice = species
        self.has_pets = has_pets


    def __eq__(self, other):
        return self.name == other.name and self.species_choice == other.species_choice and self.has_pets == other.has_pets


    def __str__(self):
        if self.has_pets:
            output = "yes"
        else:
            output = "no"
        return self.name + ". Species choice: " + self.species_choice + ". Other pets: " + output + "."


    def is_match(self, pet):
        species_match = self.species_choice == pet.species
        if self.has_pets is False:
            return species_match
        else:
            return species_match and pet.can_live_with_pets