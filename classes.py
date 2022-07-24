def comment(func):
    def wrapper(self, obj):
        result = func(self, obj)
        print(result)
    return wrapper


def level_up(obj):
    obj.level += 1
    obj.exp -= 100
    obj.hp = obj.hp + obj.hp * 0.5
    obj.fp = obj.fp + obj.fp * 0.3
    obj.stamina = obj.stamina + obj.stamina * 0.4
    return "Level up!"


class Base:
    def __init__(self, name, health):
        self.hp = health
        self.stamina = 100
        self.fp = 50
        self.exp = 0
        self.level = 1
        self.damage = 10
        self.name = name

    def get_damaged(self, damage):
        self.hp -= damage

    def has_stamina(self):
        return self.stamina >= 0

    @comment
    def physical_attack(self, obj):
        obj.get_damaged(self.damage)
        if self.has_stamina():
            self.stamina -= 10
            return f'Attack: -{self.damage}'
        else:
            return f"Need a relax!"

    def go_to(self):
        if self.has_stamina():
            self.stamina -= 5
            return 5
        else:
            return f"Need a relax!"

    def run(self):
        if self.has_stamina():
            self.stamina -= 10
            return 10
        else:
            return f"Need a relax!"

    def is_alive(self):
        return self.hp > 0

    def death(self):
        del self

    def __str__(self):
        return f"HP: {self.hp}\nFP: {self.fp}\nStamina: {self.stamina}"


class Wizard(Base):
    def __init__(self, name):
        super().__init__(name, health=100)
        self.damage = 10

    @comment
    def magical_light_attack(self, obj):
        obj.get_damaged(self.damage)
        self.stamina -= 15
        self.fp -= 10
        return f"Magic attack: -{self.damage}"

    @comment
    def magical_heavy_attack(self, obj):
        damage = self.damage + self.damage * 0.3
        obj.get_damaged(damage)
        self.stamina -= 20
        self.fp -= 15
        return f"Magic attack: -{damage}"

    @comment
    def healing(self, obj):
        setattr(obj, 'hp', getattr(obj, 'hp', 0) + 25)
        self.stamina -= 20
        self.fp -= 20
        return f"Healing {getattr(obj, 'name', 'None')}"

    @comment
    def recover_stamina(self, obj):
        setattr(obj, 'stamina', getattr(obj, 'stamina', 0) + 50)
        self.stamina -= 15
        self.fp -= 20
        return f"Recovering {getattr(obj, 'name', 'None')}"

    def show_skills(self):
        return "Healing, Recover stamina"


class Paladin(Base):
    def __init__(self, name):
        super().__init__(name, health=100)
        self.damage = 13

    @comment
    def healing(self, obj):
        setattr(obj, 'hp', getattr(obj, 'hp', 0) + 30)
        self.stamina -= 20
        self.fp -= 20
        return f"Healing {getattr(obj, 'name', 'None')}"

    @comment
    def magical_light_attack(self, obj):
        obj.get_damaged(self.damage*0.7)
        self.stamina -= 15
        self.fp -= 10
        return f"Magic attack: -{self.damage}"

    @comment
    def magical_heavy_attack(self, obj):
        damage = self.damage
        obj.get_damaged(damage)
        self.stamina -= 20
        self.fp -= 15
        return f"Magic attack: -{damage}"


if __name__ == "__main__":
    player = Wizard("Artur")
    pl2 = Wizard("King")
    player.physical_attack(pl2)
    print(pl2)
    player.magical_light_attack(pl2)
    print(pl2)
    player.magical_heavy_attack(pl2)
    print(pl2)
    player.healing(pl2)
    print(pl2)
