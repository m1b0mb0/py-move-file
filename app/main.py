import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3:
        command_name, first_file, second_file = split_command
        if command_name == "mv":
            directory = os.path.dirname(second_file)
            filename = os.path.basename(second_file)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with (
                open(first_file, "r") as file_in,
                open(os.path.join(directory, filename), "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(first_file)
