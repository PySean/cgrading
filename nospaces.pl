#!/usr/bin/perl

=pod
    "nospaces", by Sean Soderman
    Replaces all spaces within filenames *under* the current
    directory with underscores.
=cut

@dude = `find`;
chomp @dude;
foreach(@dude) {
    if ($_ ne "nospaces.pl") {
        $old = $_;
        $new = s/\s/\_/g;
        print `mv "$old" $_`;
    }
}
