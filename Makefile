# This option defines which mock configuration to use -- see /etc/mock for 
# the available configuration files for your system.
MOCK_CONFIG=epel-6-x86_64
SHELL=/bin/bash

SPEC=check-ntp-when.spec
NAME=$(shell grep 'define name' $(SPEC) | awk '{ print $$3 }')
VERSION=$(shell grep 'define unmangled_version' $(SPEC) | awk '{ print $$3 }')
RELEASE=$(shell grep 'define release' $(SPEC) | awk '{ print $$3 }')
# only query mock if it's installed
MOCK_ROOT=$(shell type -p mock >/dev/null && /usr/bin/mock -r $(MOCK_CONFIG) --print-root-path)
MOCK_RESULT=$(shell /usr/bin/readlink -f $(MOCK_ROOT)/../result)

NVR=$(NAME)-$(VERSION)-$(RELEASE)
MOCK_SRPM=$(NVR).el6.src.rpm
RPM=$(NVR).el6.noarch.rpm

.DEFAULT: all

all: mock

mock: mock-rpm
	@echo "BUILD COMPLETE; RPMS are in $(MOCK_RESULT)"

srpm:
	rpmbuild -bs $(SPEC)

rpm:
	rpmbuild -bb $(SPEC)

mock-srpm:
	mock -r $(MOCK_CONFIG) --init
	mock -r $(MOCK_CONFIG) --buildsrpm --spec $(SPEC) --sources . --resultdir .

mock-rpm: mock-srpm
	mock -r $(MOCK_CONFIG) --rebuild $(MOCK_SRPM) --resultdir .

clean: mock-clean

mock-clean:
	mock -r $(MOCK_CONFIG) --clean
	rm -f $(MOCK_SRPM) $(RPM) available_pkgs installed_pkgs *.log
