# -*- coding: utf-8 -*-
# Author: Douglas Creager <dcreager@dcreager.net>
# This file is placed into the public domain.

# Source: https://gist.github.com/ampledata/3067886/download#
# Mod: pep386adapt() always returns something
# Mod: return "dev" instead of "post" releases
# Original: http://dcreager.net/2010/02/10/setuptools-git-version-numbers/

# Calculates the current version number.  If possible, this is the
# output of â€œgit describeâ€, modified to conform to the versioning
# scheme that setuptools uses.  If â€œgit describeâ€ returns an error
# (most likely because we're in an unpacked copy of a release tarball,
# rather than in a git working copy), then we fall back on reading the
# contents of the RELEASE-VERSION file.
#
# To use this script, simply import it your setup.py file, and use the
# results of get_git_version() as your package version:
#
# from version import *
#
# setup(
#     version=get_git_version(),
#     .
#     .
#     .
# )
#
# This will automatically update the RELEASE-VERSION file, if
# necessary.  Note that the RELEASE-VERSION file should *not* be
# checked into git; please add it to your top-level .gitignore file.
#
# You'll probably want to distribute the RELEASE-VERSION file in your
# sdist tarballs; to do this, just create a MANIFEST.in file that
# contains the following line:
#
#   include RELEASE-VERSION

__all__ = ("get_git_version")

from subprocess import Popen, PIPE

POST_TAG = 'dev'  # 'dev' or 'post', see PEP 386, http://www.python.org/dev/peps/pep-0386/


def call_git_describe(abbrev=4):
    try:
        p = Popen(['git', 'describe', '--abbrev=%d' % abbrev],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return line.strip()

    except:
        return None


def read_release_version():
    try:
        f = open("RELEASE-VERSION", "r")

        try:
            version = f.readlines()[0]
            return version.strip()

        finally:
            f.close()

    except:
        return None


def write_release_version(version):
    f = open("RELEASE-VERSION", "w")
    f.write("%s\n" % version)
    f.close()


def get_git_version(abbrev=4):
    # Read in the version that's currently in RELEASE-VERSION.

    release_version = read_release_version()

    # First try to get the current version using â€œgit describeâ€.

    version = call_git_describe(abbrev)

    #adapt to PEP 386 compatible versioning scheme
    version = pep386adapt(version)

    # If that doesn't work, fall back on the value that's in
    # RELEASE-VERSION.

    if version is None:
        version = release_version

    # If we still don't have anything, that's an error.

    if version is None:
        raise ValueError("Cannot find the version number!")

    # If the current version is different from what's in the
    # RELEASE-VERSION file, update the file to be current.

    if version != release_version:
        write_release_version(version)

    # Finally, return the current version.

    return version


def pep386adapt(version):
    if version is not None and '-' in version:
        # adapt git-describe version to be in line with PEP 386
        parts = version.split('-')
        parts[-2] = POST_TAG + parts[-2]
        version = '.'.join(parts[:-1])
    return version


if __name__ == "__main__":
    print get_git_version()