#!/bin/sh

# Three Claw
yell() { echo "$0: $*" >&2; }
die() { yell "$*"; exit 111; }
try() { "$@" || die "cannot $*"; }

# variable=${something:-default_something}

# From http://blackskyresearch.net/shelltables.txt
# ----------------------------------------------
# Evaluation and Substitution of Shell Variables

# $var			Value of var; nothing if var undefined.  ENV variables are, by convention, typically typed all caps.

# ${var}			Same as $var, useful if alphanumerics follow variable name.

# ${var-thing}		Value of var if defined, otherwise thing, $var remains unchanged.

# ${var:-word}		If var exists and isn't null, return it's value; otherwise, return word.
#       Purpose: To return a default value if the variable is undefined.
#       Example: ${count:-0} evaluates to 0 if count is undefined.

# ${var:=word}		If var exists and isn't null, return it's value; otherwise set it to word and return it's value.
#       Purpose: To set a variable to a default value if it is undefined.
#       Example: ${count:=0} sets count to 0 if it is undefined.

# ${var:?message}		If var exists and isn't null, return it's value; otherwise, print 'var: message', and abort the current command of script.  Omitting message produces the default message parameter null or not set.  Note, however, that interactive shells do not have to abort.  (Behavior and exit code varies across shells.)
#       Purpose: To catch errors that result from variables being undefined.
#       Example: ${count:?"undefined!"} prints 'count: undefined!' and exits if count is undefined.

# ${var:+word}		If var exists and isn't null, return word; otherwise, return null.
#       Purpose: To test for the existence of a variable.
#       Example: ${count:+1} returns 1 (which could mean "true") if count is defined.
