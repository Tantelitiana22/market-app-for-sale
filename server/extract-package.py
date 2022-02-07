from pipfile import Pipfile

parsed = Pipfile.load(filename="Pipfile")
package = parsed.data.get("default")
value = "".join([f"{key}{value}\n" for (key, value) in package.items()])

with open("requirements.txt", "w") as file:
    file.write(value)
