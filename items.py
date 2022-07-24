class Items:
    pass


class FlaskHP(Items):
    def __init__(self):
        self.recovered_hp = 20
        self.volume = 60

    def recover_health(self, player):
        setattr(player, 'hp', player.hp + self.recovered_hp)
        self.volume -= self.recovered_hp

    def upgrade(self, item):
        pass


class FlaskFP(Items):
    def __init__(self):
        self.recovered_fp = 20
        self.volume = 60

    def recover_fp(self, player):
        setattr(player, 'fp', player.fp + self.recovered_fp)
        self.volume -= self.recovered_fp

class Inventory:
    def __init__(self):
        self.size = 10
        self.storage = []

    def add_item(self, item):
        self.size -= 1
        self.storage.append(item)

    def use_item(self):
        self.size += 1
        self.storage.pop()

    def show(self):
        return self.storage

