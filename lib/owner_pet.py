class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string")
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to the pet if it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by their name"""
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name='{self.name}')"


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type '{pet_type}'. Must be one of {Pet.PET_TYPES}")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance or None")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

    def __repr__(self):
        owner_name = self.owner.name if self.owner else None
        return f"Pet(name='{self.name}', type='{self.pet_type}', owner='{owner_name}')"
