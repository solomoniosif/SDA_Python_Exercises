from datetime import datetime


def run_only_between(from_=7, to_=22):
    def dec(func):
        def wrapper(*args, **kwargs):
            if from_ <= datetime.now().hour < to_:
                print(f"It's only {datetime.now().hour} o'clock!")
                func(*args, **kwargs)

        return wrapper

    return dec


@run_only_between(10, 15)
def remind_me_to_study(lang):
    print(f"You should study some more {lang}!")


remind_me_to_study('Python')

# run_only_between(12, 14)(remind_me_to_study)('SQL')

