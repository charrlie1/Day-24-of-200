# Day-24-of-200

In this reimplementation:
→ The Person class itself acts as the ADT.
→The __init__ method initializes the internal data (first name, last name, birthday), which are attributes of the Person object. The user interacts with the Person object without directly manipulating these attributes from outside the class.
 → Methods like get_full_name() and get_age() provide an interface to access information derived from the internal data. The user doesn't need to know how the full name is constructed or how the age is calculated.
→The special methods __lt__ and __str__ overload operators and the string conversion function, providing abstract ways to compare Person objects and get a string representation of them.
This example shows how ADTs explains data and behavior, providing a clear and abstract interface for interacting with the Person object.
