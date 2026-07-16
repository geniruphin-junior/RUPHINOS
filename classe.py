class Ruphin:

    def __init__(self):

        self.name = "Ruphin Bahati"

        self.role = "Python Developer"

        self.location = "Democratic Republic of the Congo 🇨🇩"

        self.languages = ["Python", "C++", "JavaScript"]

        self.interests = [
            "Artificial Intelligence",
            "Data Science",
            "Scientific Computing",
            "Software Architecture",
        ]

    def mission(self):
        return "Build software that solves real-world problems."


ruphin = Ruphin().location()
print(ruphin)
