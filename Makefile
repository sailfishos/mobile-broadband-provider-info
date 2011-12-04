PKG_NAME := mobile-broadband-provider-info
SPECFILE = $(addsuffix .spec, $(PKG_NAME))
YAMLFILE = $(addsuffix .yaml, $(PKG_NAME))

include /usr/share/packaging-tools/Makefile.common

