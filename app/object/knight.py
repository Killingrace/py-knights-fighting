
from app.object.armour import Armour
from app.object.potion import Potion
from app.object.weapon import Weapon


class Knight:
    protection = 0

    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 armour: list[Armour],
                 potion: Potion | None,
                 weapon: Weapon) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.potion = potion
        self.weapon = weapon

    def __repr__(self) -> str:
        return f"""
\n<
    Knight Name: {self.name}
    Knight HP: {self.hp}
    Knigh Protection: {self.protection}
    Knight Power: {self.power}
    Knight Armour: {self.armour}
    Knight Potion: {self.potion}
    Knight Weapon: {self.weapon}
>
"""
