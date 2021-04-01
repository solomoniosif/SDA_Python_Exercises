from rich.console import Console
from rich.text import Text

console = Console()


console.print('Test string', style='bold red')
text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)
console.print(text)

console.log("Hello, World!")

console.print('Google', style="link https://google.com")