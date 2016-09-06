# Copyright (c) 2012-2013 LiuYC https://github.com/liuyichen/
# Copyright 2012-2014 ksyun.com, Inc. or its affiliates. All Rights Reserved.
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
from tests import unittest

import mock

import kscore.session


# Basic sanity checks for loader functionality.
# We're not using BaseEnvVar here because we don't actually
# want to patch out all of os.environ, we just want to ensure
# AWS_DATA_PATH doesn't affect our test results.
class TestLoaderBasicFunctionality(unittest.TestCase):
    def setUp(self):
        self.environ = os.environ.copy()
        self.patched = mock.patch('os.environ', self.environ)
        self.patched.start()
        self.environ.pop('KS_DATA_PATH', None)

        self.session = kscore.session.get_session()
        self.loader = self.session.get_component('data_loader')

    def tearDown(self):
        self.patched.stop()

    def test_search_path_has_at_least_one_entry(self):
        self.assertTrue(len(self.loader.search_paths) > 0)

    def test_can_list_available_services(self):
        # We don't want an exact check, as this list changes over time.
        # We just need a basic sanity check.
        available_services = self.loader.list_available_services(
            type_name='service-2')
        self.assertIn('kog', available_services)

    def test_can_determine_latest_version(self):
        api_versions = self.loader.list_api_versions(
            service_name='kog', type_name='service-2')
        self.assertEqual(
            self.loader.determine_latest_version(
                service_name='kog', type_name='service-2'),
            max(api_versions))

    def test_can_load_data(self):
        api_version = self.loader.determine_latest_version(
            service_name='kog', type_name='service-2')
        data = self.loader.load_data(
            os.path.join('kog', api_version, 'service-2'))
        self.assertIn('metadata', data)
