# Design Patterns in Python

#### *What are design patterns?*

- Design patterns can be defined as well defined solutions to common problems
- Some issues and concepts are universal to all platforms and languages
- Design patterns should be treated as a suggestionof a solution for those issues
- They are handy for naming structures that naturally occur in code: adapters, decorators, builders 17

#### *What design patterns are NOT?*

- Design patterns are not copy-paste solutions
- They do not solve problems by themselves
- Forcefully applying pattern to a code it does not fit always* results in failure and worse code
- Design patterns are not rulebooks, you can take a concept and modify it to your needs 18

### Categories and examples of patterns

| Creational | Structural | Behavioral |
| :--------: | :--------: |:---------: |
| Singleton | Adapter | Chain of responsability |
| Builder | Bridge | Command |
| Factory | Facade | Interpreter |
| Abstract Factory | Decorator | Iterator |
| Dependency Injection | Proxy | Strategy |
| | Flyweight | Observer |

## Creational Patterns

#### *What are creational patterns?*

Creational patterns increase flexibility and resusability of code by extending code creation.

### 1. Singleton

- Its main feature is the fact that you can create only one instance of it.
- Even if you create more objects, they will all be a reference to the same instance.

```python
class Singleton:
    _instance = None

    def __init__(self, name='S1'):
        print(f"- Instance initialization: name={name}")
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("- Create a new instance")
            cls._instance = object.__new__(cls)
        print("- Returning existing instance")
        return cls._instance
```

### 2. Builder

- Builder is a very useful pattern, allowing us to construct objects from smaller pieces
- Sometimes we need to create many objects which behave in a similar way
- Reusing code is a good idea
- Builder helps us use common objects and mix and match them

```python
class Message:
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self._text


class Capitalized:
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg).capitalize()


class WithExclamation:
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg) + "!"


class WithQuestion:
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg) + "?"


m = Message("really")
happy = Capitalized(WithExclamation(m))
print(str(happy))
confused = Capitalized(WithQuestion(WithExclamation(m)))
print(str(confused))
```

```
Really!
Really!?
```

### 3. Factory method

- Factory method creates objects without the need to specify class
- Classes fulfill the same interface, but differ when used
- Factories are often used when it’s the config, which decides which one we should pick –the pick is made dynamically

```python
class RoyalMail:
    cost = 15.0
    duration = 3

    def __init__(self, package):
        self.package = package

    def ship(self):
        print(f"Shipping{self.package}in{self.duration}days"
              f"for{self.cost}via{self.__class__.__name__}")


class ShadyCourier:
    cost = 1.0
    duration = 30

    def __init__(self, package):
        self.package = package

    def ship(self):
        print(f"Shipping{self.package}in{self.duration}days"
              f"for{self.cost}via{self.__class__.__name__}")


class OnlineStore:
    _companies = {"RoyalMail": RoyalMail, "ShadyCourier": ShadyCourier}

    def proces_shipment(self, package, company="RoyalMail"):
        return self._companies[company](package)


if __name__ == "__main__":
    store = OnlineStore()
    fast_shipment = store.proces_shipment("Vase")
    fast_shipment.ship()
    slow_shipment = store.proces_shipment("Flamingo", "ShadyCourier")
    slow_shipment.ship()
```

```
Shipping Vase in 3 days for 15.0 via RoyalMail
Shipping Flamingo in 30 days for 1.0 via ShadyCourier
```

## Structural Patterns

#### *What are structural patterns?*

Structural patterns make connecting objects easier, or allow to compose them into logical structures.

### 1. Decorator

Their main feature is extending object capabilities without modifying them.

```python
import time


class TimerDecorator:
    def __init__(self, func):
        self.times = []
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        delta_time = time.time() - start_time
        self.times.append(delta_time)
        print(f"Function {self.func.__name__} has been executed in {delta_time}s "
              f"with the following arguments: {args} {kwargs}")
        return result


@TimerDecorator
def calculate_product_a_million_times(small_number):
    for _ in range(1_000_000):
        large_number = 4 ** 39
        _ = large_number * small_number + small_number ** 39


if __name__ == "__main__":
    calculate_product_a_million_times(10)
```

```
Function calculate_product_a_million_times has been executed in 0.40529298782348633s with the following arguments: (10,) {}
```

### 2. Adapter

- Adapter enables communication with a class, when it does not implement methods or fields required by the class
  attempting communication
- It is often used to adapt to classes provided by external libraries, since there is no easy way to modify them

```python
class Container:
    def __init__(self, elem):
        self.elements = list(range(elem))

    def __repr__(self):
        return f"<Container({len(self.elements)}elem)>"


class DictAdapter:
    def __init__(self, d):
        self.d = d

    def __repr__(self):
        return f"<Container({len(self.d)}elem)>"


containers = [Container(1), Container(2), DictAdapter({"A": 1})]
print(containers)
```

``` 
[<Container (1 elem)>, <Container (2 elem)>, <Container (1 elem)>]
```

