#!/usr/bin/perl

=pod
    "convall2univ.pl", by Sean Soderman
    Modifies all text files *under* the directory tree to have
    UNIX line endings.
=cut


if (@ARGV < 1) {
    print "Usage: $0 root_directory\n";
    exit(1);
}

$root = $ARGV[0];
@files = `find $root`;
chomp @files;
@files = grep { -f && -T } @files;
foreach(@files) {
    `dos2unix $_`;
}
