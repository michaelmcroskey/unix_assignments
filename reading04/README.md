Reading 04
==========

1) Extract the contents of file.tar.gz.

	$ gzip -d file.tar.gz
	
2) Create an archive named data.tar.gz which consists of the contents of the directory data.

	$ tar z data.tar.gz data

3) Extract the contents of file.zip.

	$ unzip file.zip

4) Create an archive named data.zip which consists of the contents of the directory data.

	$ zip -r data.zip data

5) Install a package on a Debian based distribution.

	$ apt-get install package

6) Install a package on a Red Hat based distribution.

	$ yum install package

7) Install a Python package.

	$ python setup.py install

8) Paste the contents of a file to an online pastebin.

	$ cat ~/myfile.txt | nc termbin.com 9999

9) Run commands as the root user.

	$ sudo su
