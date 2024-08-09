initial_velocity = eval(input("Enter the initial velocity of the object: "))
final_velocity = eval(input("Enter the final velocity of the object: "))
acceleration = eval(input("Enter the acceleration of the object: "))
displacement = (final_velocity ** 2 - initial_velocity ** 2) / (2 * acceleration)
print(f"The displacement of the object is: {displacement}")

