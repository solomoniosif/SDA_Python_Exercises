# Good practices in Python

- Python is well known for its readability and pretty code…
- However it is developer’s responsibility to make their code follow suit
- There are no strict rules (the code will still execute)
- However some standards are enforced by the community
- Most of them are captured in two PEPs (Python Enhancement Proposals): PEP8and PEP20

## PEP20

**PEP20 outlines a general approach to Python**

- It might help you make a good decision when presented with a more general problem, than described in PEP8
- Regardless of the application, treat it as a set of good advices
- You can always find it, by typing ```import this```

```python
import this
```

```
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
```

## PEP8

**PEP8 defines an official formatting**

Main points:

- Line length limit –officially 79 characters, usually up to 90, depending on project
- Indentation –only spaces, 4 per indentation level
- Naming conventions –Capitalized class names, lowercase function, module & variable names, snake_case, capitalized
  constants
- selffor instance methods, clsfor class methods
- Trailing underscore for names potentially shadowing built-ins, like id_
- Consistent line-breaks
- No trailing whitespaces

## Linters

- Tracking all of those recommendations and rules can be daunting at first
- Even advanced developers sometimes need reminders of some of them
- This is why most people use linters
- Linters are built-in in most of the IDEs, but you can also install and use one on your own
- ```pip install --user pylint```

## Formatters

- Formatters are different than linters –they do not highlight any deficiencies
- Formatters are designed to fix minor things, like line length, line-breaks, trailing whitespace, blank lines, etc.
- They make your formatting more consistent
- There are many great formatters available, we will try out black

    - ##### **black**
        - Black is a bit different than other formatters
        - It does not allow any configuration –it works as its author intended or not at all
        - Since black’s author (Łukasz Langa) joined Python Software Foundationas Python Core Developer, black’s
          ownership has been transfered to the PSF
        - This means that while there is no one official formatter, this is as close as it gets
        - ```- pip install --user black```