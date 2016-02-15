TLDR - gzip
==========

Overview
--------

[gzip] is a way to decrease the size of a file keeping the same ownership modes, access and modification times as before

Examples
--------

- **Decrease** size of a file:

	$ gzip file

- **Decrease size** of multiple files:
		
	$ gzip file.txt file2 file3.doc

- **Compress** multiple files into single file:
		
	$ cat file2.doc file1 file3 | gzip > compressedFiles.gz 
		

Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/gzip.1.html)
