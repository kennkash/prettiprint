# Changelog

prettiprint changelog history.  


<!-- insertion marker -->

## [v0.2.3] - 2025-10-24


### Features

- (prettiprint) added a new argument to the dictionary method to provide the option of expanding or collapsing the width of the panel surrounding the the dictionary ([939b22f] by k.kashmiry).

### Tests

- (demo) adding an example of the dictionary method utilizing the new expand argument ([2a9ec05] by k.kashmiry).


## [v0.2.2] - 2025-10-24


### Features

- (prettiprint) added a new spacer method to allow for spacing between print statements, utilized new spacer method in header method; added a space before and after each header, added a new argument to the code method to provide the option to word wrap the code ([bbe85ef] by k.kashmiry).

### Tests

- (demo) added example code to showcase the new spacer method and the new word wrap argument in the code method ([db442a7] by k.kashmiry).


## [v0.2.1] - 2025-10-22


### Features

- (prettiprint) adding more arguments to panel utility (border_style, box, expand, padding) ([87cfd2c] by k.kashmiry).

### Tests

- (demo) updating to no longer include section utility and adding more examples of how to use the updated panel utility ([e903297] by k.kashmiry).


## [v0.2.0] - 2025-10-22


### Features

- (prettiprint) adding the ability to change the color of the label for rule utility, removing section utility as well ([726afd9] by k.kashmiry).


## [v0.1.1] - 2025-10-22


### Tests

- (demo) updating import order ([79887a3] by k.kashmiry).


## [v0.1.0] - 2025-10-22


### Build

- (pylint) editing pylint to only check package file and ignore conventions and warnings ([5e46db4] by k.kashmiry).
- (pyproject) enabling verbose mode for tbump version regex, literal new-line and space characters were not allowing the current version to be parsed correctly ([2110f98] by k.kashmiry).

### Bug Fixes

- (prettyprint) update to hide events at verbosity 1 and hide DEBUG events at verbosity 2, removed default 'dict' branch/node from tree output ([5d151f8] by k.kashmiry).

### Code Refactoring

- (.gitignore) including dev-requirements.txt in repo ([4bbeca5] by k.kashmiry).
- (Makefile) for update target, changing repo name to prettyprint from template repo name ([53df1fa] by k.kashmiry).

### Tests

- (demo) adding a test function for pytest to locate and run ([f9ea646] by k.kashmiry).

