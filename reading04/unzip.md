TLDR - unzip
==========

Overview
--------

[unzip] is a command that lists, tests and extracts compressed files in a ZIP archive


Examples
--------

- **Extract** all members of the archive letters.zip into the current directory:

		$ unzip letters.zip

- **Unzip** files to a particular folder (destination_folder):

        $ unzip letters.zip -d destination_folder

- **Freshen** existing files - extract only those files that already exist on disk and that are newer than the disk copies:
		
		$ unzip -f letters.zip


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/unzip.1.html)
