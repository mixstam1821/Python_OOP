class ByzantineEmperor:
    def __init__(self, name, reign_start, reign_end):
        self.name = name
        self.reign_start = reign_start
        self.reign_end = reign_end

    def length_of_reign(self):
        return self.reign_end - self.reign_start

    def __str__(self):
        return f"{self.name}, reigned from {self.reign_start} to {self.reign_end}"

class ByzantineEmpire:
    def __init__(self):
        self.emperors = []

    def add_emperor(self, emperor):
        self.emperors.append(emperor)

    def select_emperor(self, name):
        for emperor in self.emperors:
            if emperor.name == name:
                return emperor
        return None

# Example usage:
byzantine_empire = ByzantineEmpire()

emperor1 = ByzantineEmperor("Justinian I", 527, 565)
emperor2 = ByzantineEmperor("Constantine XI", 1449, 1453)
emperor3 = ByzantineEmperor("Alexios I Komnenos", 1081, 1118)
emperor4 = ByzantineEmperor("Basil II", 976, 1025)

byzantine_empire.add_emperor(emperor1)
byzantine_empire.add_emperor(emperor2)
byzantine_empire.add_emperor(emperor3)
byzantine_empire.add_emperor(emperor4)

print("Available emperors:")
for emperor in byzantine_empire.emperors:
    print(emperor.name)

selected_emperor_name = input("Enter the name of the emperor you want to select: ")
selected_emperor = byzantine_empire.select_emperor(selected_emperor_name)
if selected_emperor:
    print("Selected Emperor:", selected_emperor)
    print("Length of reign:", selected_emperor.length_of_reign(), "years")
else:
    print("Emperor not found")
