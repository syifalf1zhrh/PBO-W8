class QueenBand:
    members = ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"]

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    @property
    def band_name(self):
        return f"The band's name is {self.name}"

    @classmethod
    def get_members(cls):
        return f"Members of Queen: {', '.join(cls.members)}"

    @staticmethod
    def famous_song():
        return "One of Queen's most famous songs is 'Bohemian Rhapsody'."

queen = QueenBand("Queen", "Rock")

# Access the band's name using @property
print(queen.band_name)

# Access the members using @classmethod
print(QueenBand.get_members())

# Access the famous song using @staticmethod
print(QueenBand.famous_song())