import typer

from commands.tail import Tail


def tail(
    file_name: str = typer.Argument(..., help="The name of the file to read."),
    follow: bool = typer.Option(
        False,
        "-f",
        help="""
        The -f option causes tail to not stop when end of file is
        reached, but rather to wait for additional data to be appended to
        the input.""",
    ),
) -> None:
    tail = Tail(file_name=file_name, follow=follow)
    tail()


if __name__ == "__main__":
    typer.run(tail)
