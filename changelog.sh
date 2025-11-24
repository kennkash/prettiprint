#! /bin/bash

git-changelog --output CHANGELOG.md -c angular -rt path:src/prettiprint/templates/changelog.j2 -s build,deps,fix,feat,refactor,style,tests
