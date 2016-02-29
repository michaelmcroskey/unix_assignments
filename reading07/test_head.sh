#!/bin/sh

WORKSPACE=/tmp/head.$(id -u)

error() {
    echo 1>&2 "ERROR: $@"
    [ -r $WORKSPACE/test ] && cat $WORKSPACE/test
    exit 1
}

cleanup() {
    rm -fr $WORKSPACE
    exit $1
}

mkdir $WORKSPACE

trap "cleanup 0" EXIT
trap "cleanup 1" INT TERM

head < /etc/passwd > $WORKSPACE/output
./head.sh < /etc/passwd | diff -y - $WORKSPACE/output > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed /etc/passwd test"
fi

head -n 2 < /etc/passwd > $WORKSPACE/output
./head.sh -n 2 < /etc/passwd | diff -y - $WORKSPACE/output > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed /etc/passwd test (-n 2)"
fi

echo "head.sh test succesful!"
exit 0
