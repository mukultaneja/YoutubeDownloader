============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/mukultaneja/YoutubeDownloader/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

ytdownloader could always use more documentation, whether as part of the
official ytdownloader docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/mukultaneja/YoutubeDownloader/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

``ytdownloader`` runs on 2.7+ and Python 3+ in any OS. To set up the development
environment:

1. Fork the `YoutubeDownloader repo <https://github.com/mukultaneja/YoutubeDownloader>`__
2. Clone your fork locally::

    git clone git@github.com:your_user_id/YoutubeDownloader.git

3. Install your local copy into a virtualenv. If you have `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/install.html>`__ installed, this is how you set up your fork for local development::

    $ mkvirtualenv YoutubeDownloader
    $ cd YoutubeDownloader/
    $ python setup.py develop

4. Create a branch for local development::

    git checkout -b <branch-name>

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8::

6. Commit your changes and push your branch to GitHub. Then send a pull
   request::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push --set-upstream origin <branch-name>

7. To delete your branch::

    git branch -d <branch-name>
    git push origin --delete <branch-name>

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
2. The pull request should work for Python 2.7 and 3+.

Release
-------

1. Update ``__version__ = x.x.x`` in :mod:`ytdownloader`

2. Update ``HISTORY.rst`` with changes

3. Commit, create an annotated tag and push the code::

    git commit .
    git tag -a vx.x.x
    git push --follow-tags

4. To `release to PyPi`_, run::

    make clean
    python setup.py sdist bdist_wheel --universal
    twine upload dist/*

.. _release to PyPi: https://packaging.python.org/en/latest/distributing.html