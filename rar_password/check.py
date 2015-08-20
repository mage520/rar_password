import subprocess

from .util import case_to_str


def check(case, filename):
    password = case_to_str(case)
    cmd = ['unrar', 't', '-y', '-p'+password, filename]
    msg, err = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()

    if msg is not None:
        msg = msg.decode('u8')

        return 'All OK' in msg

    return False
