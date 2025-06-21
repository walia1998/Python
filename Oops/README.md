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
