from json import dump, load

def load_json(filepath, print_error_message=False):
    try:
        with open(filepath, "r") as file:
            data_set = load(file)
            return data_set
    except FileNotFoundError:
        if print_error_message:
            print(f"File {filepath} was not found.")
    except Exception as e:
        if print_error_message:
            print()