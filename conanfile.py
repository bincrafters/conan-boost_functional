#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostFunctionalConan(base.BoostBaseConan):
    name = "boost_functional"
    url = "https://github.com/bincrafters/conan-boost_functional"
    lib_short_names = ["functional"]
    header_only_libs = ["functional"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_function_types",
        "boost_iterator",
        "boost_mpl",
        "boost_optional",
        "boost_preprocessor",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility"
    ]
