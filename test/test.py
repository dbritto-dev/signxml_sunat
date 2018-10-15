import unittest
from lxml import etree
from signxml_sunat import XMLSigner, XMLVerifier

class TestSignXMLSunat(unittest.TestCase):
    def test_sign(self):
        signed_doc = XMLSigner().sign('doc.xml', 'rsakey.pem', 'rsacert.pem')
        signed_doc_str = etree.tostring(signed_xml, xml_declaration=True, encoding='ISO-8859-1', pretty_print=True)
        result_signed_doc_str = open('signed_doc.xml').read()

        self.assertEqual(signed_doc, result_signed_doc_str)

    def test_verify(self):
        verify = XMLVerifier().verify('sunat_signed.xml', 'rsapub.pem)

        self.assertTrue(verify) 

if __name__ == '__main__':
    unittest.main()