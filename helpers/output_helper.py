def prepare_output(capsys) -> list:
    """
    Captures and processes the output.

    :param capsys: The pytest capsys fixture used for capturing output.
    :return: A list of output lines.
    """

    new_output = capsys.readouterr().out.strip().splitlines()
    return new_output
