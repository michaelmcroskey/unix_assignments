TLDR - df
==========

Overview
--------

[df] is a command that reports file system disk space usage

Examples
--------

- **Report** disk space usage:

        $ df

- **Include** pseudo, duplicate, inaccessible file systems:

        $ df -a
        $ df -all

- **Print** sizes in powers of *1000*:

        $ df -H
        $ df --si

- **Limit** listing to local file systems:

        $ df -l
        $ df --local

Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/df.1.html)
