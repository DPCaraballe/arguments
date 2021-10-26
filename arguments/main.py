# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name: str, greeting_template: str = "Hello, <name>!"):
    greeting = greeting_template.replace("<name>", name)
    return greeting


planets = {
    "sun": 274,
    "jupiter": 24.9,
    "neptune": 11.1,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6

}


def force(mass=5.972 * (10 ** 24), body: str = "earth"):
    gravity = ""
    if body == "earth":
        gravity = 9.8
    elif body in planets:
        gravity = planets[body]
    result = mass * gravity
    print(f"The force of {body} is {mass} * {gravity} = {result:.2f}N ")
    return result


def pull(first_mass: float, second_mass: float, distance: float):
    G = 6.674 * (10 ** -11)
    result = G * ((first_mass * second_mass) / (distance ** 2))
    return result
