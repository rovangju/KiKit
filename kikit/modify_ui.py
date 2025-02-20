import click

@click.command()
@click.argument("board", type=click.Path(dir_okay=False, exists=True))
@click.option("--show/--hide", "-s", help="Show/hide references mathing a pattern")
@click.option("--generous/--strict", "-g", help="Hide all text items with reference")
@click.option("--pattern", "-p", type=str, help="Regular expression for references")
def references(board, show, generous, pattern):
    """
    Show or hide references on the board matching a pattern.
    """
    from kikit import modify
    from kikit.common import fakeKiCADGui
    app = fakeKiCADGui()

    b = modify.pcbnew.LoadBoard(board)
    modify.references(b, show, pattern, generous)
    b.Save(board)

@click.command()
@click.argument("board", type=click.Path(dir_okay=False, exists=True))
@click.option("--show/--hide", "-s", help="Show/hide values mathing a pattern")
@click.option("--generous/--strict", "-g", help="Hide all text items with value")
@click.option("--pattern", "-p", type=str, help="Regular expression for values")
def values(board, show, generous, pattern):
    """
    Show or hide values on the board matching a pattern.
    """
    from kikit import modify
    from kikit.common import fakeKiCADGui
    app = fakeKiCADGui()

    b = modify.pcbnew.LoadBoard(board)
    modify.values(b, show, pattern, generous)
    b.Save(board)

@click.group()
def modify():
    """
    Modify board items
    """
    pass

modify.add_command(references)
modify.add_command(values)
