#!/bin/bash
set -e

# cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# see also ".mailmap" for how email addresses and names are deduplicated

{
	cat <<-'EOH'
	# This file lists all individuals having contributed content to the repository.
	# For how it is generated, see `AirBnB_clone/authors.sh`.
	EOH
	echo
	git log --format='%aN <%aE>' | sort -uf
} > AUTHORS
