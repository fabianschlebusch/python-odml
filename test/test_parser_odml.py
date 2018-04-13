"""
This file tests proper saving and loading of odML Documents
with all supported odML parsers via the tools.odmlparser classes.
"""

import os
import shutil
import tempfile
import unittest

from odml.tools import odmlparser


class TestOdmlParser(unittest.TestCase):

    def setUp(self):
        # Set up test environment
        self.tmp_dir = tempfile.mkdtemp(suffix=".odml")

        self.basepath = 'doc/example_odMLs/'
        self.basefile = 'doc/example_odMLs/THGTTG.odml'

        self.json_file = os.path.join(self.tmp_dir, "test.json")
        self.xml_file = os.path.join(self.tmp_dir, "test.xml")
        self.yaml_file = os.path.join(self.tmp_dir, "test.yaml")

        self.xml_reader = odmlparser.ODMLReader(parser='XML')
        self.yaml_reader = odmlparser.ODMLReader(parser='YAML')
        self.json_reader = odmlparser.ODMLReader(parser='JSON')

        self.xml_writer = odmlparser.ODMLWriter(parser='XML')
        self.yaml_writer = odmlparser.ODMLWriter(parser='YAML')
        self.json_writer = odmlparser.ODMLWriter(parser='JSON')

        self.odml_doc = self.xml_reader.from_file(self.basefile)

    def tearDown(self):
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)

    def test_xml(self):
        self.xml_writer.write_file(self.odml_doc, self.xml_file)
        xml_doc = self.xml_reader.from_file(self.xml_file)

        self.assertEqual(xml_doc, self.odml_doc)

    def test_yaml(self):
        self.yaml_writer.write_file(self.odml_doc, self.yaml_file)
        yaml_doc = self.yaml_reader.from_file(self.yaml_file)

        self.assertEqual(yaml_doc, self.odml_doc)

    def test_json(self):
        self.json_writer.write_file(self.odml_doc, self.json_file)
        json_doc = self.json_reader.from_file(self.json_file)

        self.assertEqual(json_doc, self.odml_doc)

    def test_json_yaml_xml(self):
        self.json_writer.write_file(self.odml_doc, self.json_file)
        json_doc = self.json_reader.from_file(self.json_file)
        
        self.yaml_writer.write_file(json_doc, self.yaml_file)
        yaml_doc = self.yaml_reader.from_file(self.yaml_file)

        self.xml_writer.write_file(yaml_doc, self.xml_file)
        xml_doc = self.xml_reader.from_file(self.xml_file)

        self.assertEqual(json_doc, self.odml_doc)
        self.assertEqual(json_doc, yaml_doc)
        self.assertEqual(json_doc, xml_doc)
        
        self.assertEqual(yaml_doc, self.odml_doc)
        self.assertEqual(yaml_doc, xml_doc)
        self.assertEqual(yaml_doc, json_doc)

        self.assertEqual(xml_doc, self.odml_doc)
        self.assertEqual(xml_doc, json_doc)
        self.assertEqual(xml_doc, yaml_doc)
