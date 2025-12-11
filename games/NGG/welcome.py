from time import sleep

def welcome(times_played):
    try:
        print_text_file(f"games/NGG/text/intro/{times_played}.txt", 0.5, True) 
        sleep(3)
    except FileNotFoundError:
        print_text_file("games/NGG/text/intro/_.txt")
def print_text_file(filepath, line_latency=0, print_error=False):
    try:
        # open file and print each line
        with open(filepath, "r", encoding='utf-8') as file:
            for line in file:
                sleep(line_latency)
                print(line.strip()) # strip removes trailing and other whitespaces before and after the line

    # error handling if the file does not exist
    except FileNotFoundError:
        if print_error:
            print(f"Error: The file '{filepath}' was not found.")
        return FileNotFoundError
    
    # other error (idk what might happen, but it's best to be prepared)
    except Exception as e:
        if print_error:
            print(f"An error occurred: {e}")
        return e