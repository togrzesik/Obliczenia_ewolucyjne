class FileWriter:
    @staticmethod
    def write_value_over_generation(file_name, values):
        file = open(file_name, "w")
        epoch = 1

        for value in values:
            file.write(f"{epoch}: {value}\n")
            epoch = epoch + 1

        file.close()