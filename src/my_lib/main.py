import tomllib


config = tomllib.load(open("config.toml", "rb"))


def greet(name: str = config["name"]) -> None:
    print(f"Hello, {name}!")
