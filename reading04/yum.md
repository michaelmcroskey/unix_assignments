TLDR - yum
==========

Overview
--------

[yum] is an interactive package manager (stands for Yellowdog Updater Modified)


Examples
--------

- **Install** an example package without having to confirm yes or no:

		$ yum -y install example.x86_64

- **Uninstall** example package:

        $ yum remove example.x86_64

- **Update** example package:
		
		$ yum update example.x86_64
		

- **Show** more information about a particular package:
		
		$ yum info particular.i686
		

- **List** available yum packages:
		
		$ yum list | less
				

Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/yum.1.html)
