import tomllib


config = tomllib.load(open(__file__ + "/../config.toml", "rb"))


def greet(name: str = config["name"]) -> None:
    print(f"Hello, {name}!")
