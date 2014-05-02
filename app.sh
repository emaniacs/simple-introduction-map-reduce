#!/usr/bin/env bash

echo -n 'Remove and create output directory.. '
rm -rf ./output && mkdir -p ./output/grouper
ok=$?

if test ${ok} -eq 0 ; then
    echo ' Done.'
    echo -n 'Run mapper..'
    python ./mapper.py
    ok=$?
else
    echo ' Fail.'
    exit
fi

if test ${ok} -eq 1 ; then
    echo ' Done'
    echo -n 'Run grouper..'
    python ./grouper.py
    ok=$?
else
    echo ' Fail.'
    exit
fi

if test ${ok} -eq 1 ; then
    echo ' Done'
    echo -n 'Run reducer..'
    python ./reducer.py
else
    echo 'Fail.'
    exit
fi

if test ${ok} -eq 1 ; then
    echo ' Done'
    echo 'Process done'
    echo 'Check statistic on ./output/reducer.output'
else
    echo 'Got error'
fi

exit $ok


