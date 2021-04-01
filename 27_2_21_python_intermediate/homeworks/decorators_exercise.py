from datetime import datetime


def run_between(start, stop):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if start <= datetime.now().hour < stop:
                print(f"It's {datetime.now().strftime('%H:%M:%S')} o'clock!")
                func(*args, **kwargs)

        return wrapper

    return decorator


@run_between(10, 22)
def remind_me_to_study(subject):
    print(f"You should study some more {subject}")


remind_me_to_study('Python')
remind_me_to_study('Regular Expressions')
remind_me_to_study('SQL')
