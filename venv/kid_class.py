class Ranui:
    def __init__(self, name, allowance):
        self.name = name
        self.allowance = allowance

nikau = Ranui("Nikau", 300)
print(f"{nikau.name} has an allowance of ${nikau.allowance}")

hana = Ranui("Hana", 300)
print(f"{hana.name} has an allowance of ${hana.allowance}")

tia = Ranui("Tia", 300)
print(f"{tia.name}  has an allowance of ${tia.allowance}")