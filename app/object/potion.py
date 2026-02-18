class Potion:

    def __init__(self, potion_name: str, effect: dict) -> None:
        self.potion_name = potion_name
        self.effect = effect

    def __repr__(self) -> str:
        return f"<Potion name: {self.potion_name},\
             Potion effect: {self.effect}>"
