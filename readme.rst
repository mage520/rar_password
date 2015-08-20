RAR_PASSWORD
============

RAR_PASSWORD is simple password finder for RAR files.


Requirements
------------

1. Python 3
2. UnRAR

You can install UnRAR by `apt-get` or `brew`

.. code-block:: console

   $ sudo apt-get install unrar

or

.. code-block:: console

   $ brew install unrar


Installation
------------

You can install it by pip.

.. code-block:: console

   $ pip3 install rar_password


Usage
-----

.. code-block:: console

   $ rar_password filename.rar > password.txt

You can find more options with `--help` option.

.. code-block:: console

   $ rar_password --help


License
-------

MIT
