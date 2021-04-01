# Design Patterns in Python

### Types of design patterns - *Gamma Categorization*
| Creational | Structural | Behavioral |
| :--------: | :--------: | :--------: |
| Builder | Adapter | Chain Of Responsability |
| Factories | Bridge | Command |
| Abstract Factory | Composite | Interpreter |
| Factory Method | Decorator | Iterator |
| Prototype | Facade | Mediator |
| Singleton | Flyweight | Memento |
| | Proxy | Observer |
| | | State |
| | | Strategy |
| | | Template Method |
| | | Visitor |


### SOLID design principles
1. **Single Responsability Principle** (SRP) or Separation Of Concern (SOC)
   - Every class should do one thing only
    - Different classes handling different, independent task/problems
2. **Open-Closed Principle** (OCP): 
   - Classes should be open for extensions but closed for modifications
   - When you add new functionality to a class you add it via extensions, not modifications
3. **Liskov Substitution Principle** (LSP)
   - You should be able to substitute a base type for a subtype
4. **Interface Segregation Principle** (ISP)
   - Don't put too much into an interface; split into separate interfaces
    - *YAGNI - You Ain't Going to Need It*
5. **Dependency Inversion Principle** (DIP)
   - Higher level classes or modules should not depend on low level classes/modules. Instead, they should depend on 
     abstraction.
   
## Creational Design Patterns

### 1. Builder
- When piecewise object construction is complicated, provide aan API fot doing it succinctly

### 2. Factory 
- A component responsible solely for the wholesale (not piecewise) creation of objects


