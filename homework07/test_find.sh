#!/bin/bash

if ! diff -u <(find -L /etc 2> /dev/null| sort) \
             <(./find.py /etc | sort); then
    echo "find no arguments test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -type f 2> /dev/null| sort) \
             <(./find.py /etc -type f | sort); then
    echo "find -type f argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -type d 2> /dev/null| sort) \
             <(./find.py /etc -type d | sort); then
    echo "find -type d argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -executable 2> /dev/null| sort) \
             <(./find.py /etc -executable  | sort); then
    echo "find -executable argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -readable 2> /dev/null| sort) \
             <(./find.py /etc -readable | sort); then
    echo "find -readable argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -writable 2> /dev/null| sort) \
             <(./find.py /etc -writable | sort); then
    echo "find -writable argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -empty 2> /dev/null| sort) \
             <(./find.py /etc -empty | sort); then
    echo "find -empty argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -name '*.conf' 2> /dev/null| sort) \
             <(./find.py /etc -name '*.conf' | sort); then
    echo "find -name argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -path '*security/*.conf' 2> /dev/null| sort) \
             <(./find.py /etc -path '*security/*.conf' | sort); then
    echo "find -path argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -regex '.*[0-9]+.*.conf$' 2> /dev/null| sort) \
             <(./find.py /etc -regex '.*[0-9]+.*.conf$' | sort); then
    echo "find -regex argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -perm 600 2> /dev/null| sort) \
             <(./find.py /etc -perm 600 | sort); then
    echo "find -perm argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -newer /etc/passwd 2> /dev/null| sort) \
             <(./find.py /etc -newer /etc/passwd | sort); then
    echo "find -newer argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -uid 0 2> /dev/null| sort) \
             <(./find.py /etc -uid 0 | sort); then
    echo "find -uid argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -gid 0 2> /dev/null| sort) \
             <(./find.py /etc -gid 0 | sort); then
    echo "find -gid argument test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -type f -executable 2> /dev/null| sort) \
             <(./find.py /etc -type f -executable | sort); then
    echo "find -type f -executable arguments test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -type d -readable 2> /dev/null| sort) \
             <(./find.py /etc -type d -readable | sort); then
    echo "find -type d -readable arguments test failed!"
    exit 1
fi

if ! diff -u <(find -L /etc -type d -name '*conf*' 2> /dev/null| sort) \
             <(./find.py /etc -type d -name '*conf*' | sort); then
    echo "find -type d -name arguments test failed!"
    exit 1
fi
echo "find test successful!"
