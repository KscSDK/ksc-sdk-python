# Copyright (c) 2020 xuyaming
# Copyright 2020 ksyun.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import os
import logging

import kscore.configloader
from kscore.exceptions import ConfigNotFound, PartialCredentialsError

logger = logging.getLogger(__name__)


def create_domain_resolver(session):
    providers = [
        KsDomainProvider()
    ]
    return DomainResolver(providers=providers)


class KsDomainProvider(object):
    METHOD = 'ksc-config'
    KSC_CONFIG_ENV = 'KSC_CONFIG'
    DEFAULT_CONFIG_FILENAMES = ['/etc/kscore.cfg', './.kscore.cfg', 'C:\\kscore.cfg']
    KS_DOMAIN = 'ks_domain'

    def __init__(self, environ=None, ini_parser=None):
        if environ is None:
            environ = os.environ
        if ini_parser is None:
            ini_parser = kscore.configloader.raw_config_parse
        self._environ = environ
        self._ini_parser = ini_parser

    def _extract_domain_from_mapping(self, mapping, *key_names):
        found = []
        for key_name in key_names:
            try:
                found.append(mapping[key_name])
            except KeyError:
                raise PartialCredentialsError(provider=self.METHOD,
                                              cred_var=key_name)
        return found

    def load(self):
        if self.KSC_CONFIG_ENV in self._environ:
            potential_locations = [self._environ[self.KSC_CONFIG_ENV]]
        else:
            potential_locations = self.DEFAULT_CONFIG_FILENAMES
        for filename in potential_locations:
            try:
                config = self._ini_parser(filename)
            except ConfigNotFound:
                # Move on to the next potential config file name.
                continue
            if 'Domain' in config:
                domain = config['Domain']
                if self.KS_DOMAIN in domain:
                    logger.info("Found Domain in ksc config file: %s",
                                filename)
                    ks_domain = self._extract_domain_from_mapping(
                        domain, self.KS_DOMAIN)
                    return Domain(ks_domain[0])


class Domain(object):
    def __init__(self, ks_domain=None):
        self.ks_domain = ks_domain


class DomainResolver(object):
    def __init__(self, providers):
        self.providers = providers

    def load_domain(self):
        """
        Goes through the credentials chain, returning the first ``Credentials``
        that could be loaded.
        """
        # First provider to return a non-None response wins.
        for provider in self.providers:
            logger.debug("Looking for domain via: %s", provider.METHOD)
            domain = provider.load()
            if domain is not None:
                return domain

        # If we got here, no credentials could be found.
        # This feels like it should be an exception, but historically, ``None``
        # is returned.
        #
        # +1
        # -js
        return None
