#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

import os
import logging
from typing import Dict

from .variable import Variable

log = logging.getLogger(__name__)


class ImmoCore:

    def __init__(self):
        self.variables: Dict[Variable.name, Variable] = {}

    def load_variables_from_directory(self, dir_path):
        """
        Recursively explores a directory and adds all variables found to ImmoCore.
        """
        import glob

        py_files = glob.glob(os.path.join(dir_path, "*.py"))
        for py_file in py_files:
            self.load_variables_from_file(py_file)

        subdirectories = glob.glob(os.path.join(dir_path, "*/"))
        for subdirectory in subdirectories:
            self.load_variables_from_directory(subdirectory)

    def load_variables_from_file(self, file_path):
        """
        Adds all variables contained in a given file to ImmoCore.
        """
        import imp
        import inspect

        try:
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            #  As Python remembers loaded modules by name, in order to prevent collisions, we need to make sure that:
            #  - Files with the same name, but located in different directories, have a different module names. Hence the file path hash in the module name.
            #  - The same file, loaded by different ImmoCore, has distinct module names. Hence the `id(self)` in the module name.
            module_name = '{}_{}_{}'.format(id(self), hash(os.path.abspath(file_path)), file_name)

            module_directory = os.path.dirname(file_path)
            try:
                module = imp.load_module(module_name, *imp.find_module(file_name, [module_directory]))
            except NameError as e:
                log.error(
                    str(e) +
                    ": if this code used to work, this error might be due to a major change in ImmoCore.")
                raise

            potential_variables = [getattr(module, item) for item in dir(module) if not item.startswith('__')]
            for pot_variable in potential_variables:
                # We only want to get the module classes defined in this module (not imported)
                if inspect.isclass(pot_variable) and issubclass(
                        pot_variable, Variable) and pot_variable.__module__ == module_name:
                    self.load_variable(pot_variable)
        except Exception:
            log.error('Unable to load ImmoCore variables from file "{}"'.format(file_path))
            raise

    def load_variable(self, variable_class):
        name = variable_class.__name__

        # Check if a Variable with the same name is already registered.
        if self.variables.get(name, None):
            raise Exception('Variable "{}" is already defined'.format(name))

        variable = variable_class()  # instantiate variable
        self.variables[variable.name] = variable

    def build_population(self):
        # return Population()
        pass
