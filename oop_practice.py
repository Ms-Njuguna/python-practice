class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}. I'm {self.age} years old and I’m studying {self.course}.")

# Create student objects
student1 = Student("Patricia", 25, "Full Stack Software Engineering")
student2 = Student("Amani", 22, "Data Science")

# Call their introduce method
student1.introduce()
student2.introduce()
