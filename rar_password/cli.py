import os.path

from click import argument, command, echo, option

from .case import make_cases
from .check import check
from .util import case_to_str


@command()
@option('--verbose/--no-verbose', '-v/-V', default=False,
        help='Display now progress. Default value is False.')
@option('--integer/--no-integer', '-i/-I', default=True,
        help='Include integer to password cases. Default value is True.')
@option('--lower/--no-lower', '-l/-L', default=True,
        help=('Include lower alphabets to password cases.'
              'Default value is True.'))
@option('--upper/--no-upper', '-u/-U', default=True,
        help=('Include upper alphabets to password cases.'
              ' Default value is True.'))
@option('--special/--no-special', '-s/-S', default=False,
        help=('Include special characters to password cases.'
              ' Default value is False.'))
@option('--min', '-m', default=1, type=int,
        help='Minimum length of password cases. Default value is 1.')
@option('--max', '-M', default=10, type=int,
        help='Maximum length of password cases. Default value is 10.')
@argument('filename')
def main(verbose, integer, lower, upper, special, min, max, filename):
    """Find RAR File Password."""

    cases = make_cases(integer, lower, upper, special, min, max)

    if not os.path.exists(filename):
        echo('File is not exists.', err=True)
        raise SystemExit(1)

    if not os.path.isfile(filename):
        echo('Given path is not file.', err=True)
        raise SystemExit(1)

    if not filename.lower().endswith('.rar'):
        echo('File is not RAR.', err=True)
        raise SystemExit(1)

    for case in cases:
        password = case_to_str(case)
        if check(case, filename):
            if verbose:
                echo('Password: {}'.format(password))
            else:
                echo(password)
            break
        else:
            if verbose:
                echo('{} is not correct password.'.format(password), err=True)
