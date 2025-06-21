# 🐾 Animal-Dog Inheritance Example in Python

This is a simple Python project that demonstrates **Object-Oriented Programming (OOP)** concepts, specifically **inheritance** and **method overriding**.

## 📌 Overview

The project consists of two classes:

1. `Animal` – A **parent class** that contains shared attributes and behavior.
2. `Dog` – A **child class** that inherits from `Animal` and overrides one of its methods.

---

## 🔶 1. Animal Class (Parent Class)

```python
class Animal:
    location = "Australia"  # Class variable (same for all animals)

    def __init__(self, name):
        self.name = name  # Instance variable (different for each animal)

    def speak(self):
        print("Animal generic sound")



| Concept           | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| Class             | Blueprint for creating objects (`Animal`, `Dog`)                       |
| Object            | Instance of a class (`d = Dog("Bruno")`)                               |
| Constructor       | `__init__()` method runs automatically when object is created          |
| Inheritance       | `Dog` gets properties and methods from `Animal`                        |
| Method Overriding | `Dog` defines its own `speak()` method to override the one in `Animal` |
| Class Variable    | `location = "Australia"` shared by all instances                       |
| Instance Variable | `self.name` is unique for each object                                  |
