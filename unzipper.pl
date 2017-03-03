#!/usr/bin/perl -w


@zips = `ls`;
chomp @zips;
foreach(@zips) {
    if (/(.*)\.zip/) {
        `unzip $_ -d $1`
    }
}
