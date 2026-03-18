import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3:
        command_name, first_file, second_file = split_command
        if command_name == "mv":
            if "/" in second_file:
                parts = second_file.split("/")
                path = ""
                for part in parts[:-1]:
                    path = os.path.join(path, part)
                    if not os.path.exists(path):
                        os.mkdir(path)
                path = os.path.join(path, parts[-1])
                with (
                    open(first_file, "r") as file_in,
                    open(path, "w") as file_out
                ):
                    file_out.write(file_in.read())
                os.remove(first_file)
            else:
                with (
                    open(first_file, "r") as file_in,
                    open(second_file, "w") as file_out
                ):
                    file_out.write(file_in.read())
                os.remove(first_file)
