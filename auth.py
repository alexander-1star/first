class BlueprintDesigner:
    def __init__(self):
        self.designs = []

    def create(self, name):
        create = f"create for {name}"
        self.designs.append(create)
        print(f"[Designer] Created: {create}")
        return create


class partsManager:
    def __init__(self):
        self.parts_inventory = {}

    def add_parts(self, material, quantity):
        self.parts_inventory[material] = self.parts_inventory.get(material, 0) + quantity
        print(f"[parts] Added {quantity} units of {material}.")

    def use_parts(self, material, quantity):
        if self.parts_inventory.get(material, 0) >= quantity:
            self.parts_inventory[material] -= quantity
            print(f"[Materials] Used {quantity} units of {material}.")
        else:
            print(f"[Materials] Not enough {material}!")



class ConstructionWorker:
    def __init__(self):
        self.tasks_done = []

    def build(self, name):
        self.tasks_done.append(f"Built {name}")
        print(f"[Worker] Built: {name}")


# Composite class: Builder Bob
class BuilderBob(BlueprintDesigner, partsManager, ConstructionWorker):
    def __init__(self):
        BlueprintDesigner.__init__(self)
        partsManager.__init__(self)
        ConstructionWorker.__init__(self)
        self.name = "Builder Bob"

    def finished(self, project_name):
        print(f"\n[{self.name}] Starting project: {project_name}")

        blueprint = self.create(project_name)
        self.add_parts("wood", 20)
        self.add_parts("nails", 100)
        self.use_parts("wood", 15)
        self.use_parts("nails", 80)
        self.build(project_name)

        print(f"[{self.name}] Project '{project_name}' Hooray!\n")



bob = BuilderBob()
bob.finished("Garage")

