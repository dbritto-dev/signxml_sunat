import xmlsec
from lxml import etree

class XMLCore:
    def get_root(self, data):
        try:
            return etree.parse(data).getroot()
        except:
            return etree.fromstring(data).getroot()
    
    def get_signature_node(self, template):
        return xmlsec.tree.find_node(template, xmlsec.Node.SIGNATURE)

    def get_signature_context(self):
        return xmlsec.SignatureContext()
    
    def get_key(self, key_data, password):
        try:
            return xmlsec.Key.from_file(key_data, xmlsec.KeyFormat.PEM, password)
        except:
            return xmlsec.Key.from_memory(key_data, xmlsec.KeyFormat.PEM, password)

    def get_cert(self, cert_data, key):
        try:
            return key.load_cert_from_file(cert_data, xmlsec.KeyFormat.PEM)
        except:
            return key.load_cert_from_memory(cert_data, xmlsec.KeyFormat.PEM)
    
    def get_key_info(self, signature_node):
        key_info = xmlsec.template.ensure_key_info(signature_node)
        x509 = xmlsec.template.add_x509_data(key_info)
        xmlsec.template.x509_data_add_certificate(x509)
        xmlsec.template.x509_data_add_subject_name(x509)

        return key_info

class XMLSigner:
    def __init__(self,
                 method=xmlsec.Transform.ENVELOPED,
                 signature_algorithm=xmlsec.Transform.RSA_SHA1,
                 digest_algorithm=xmlsec.Transform.SHA1,
                 c14n_algorithm=xmlsec.Transform.EXCL_C14N):
        self.core = XMLCore()
        self.method = method
        self.signature_algorithm = signature_algorithm
        self.digest_algorithm = digest_algorithm
        self.c14n_algorithm = c14n_algorithm

    def get_root(self, data):
        return self.core.get_root(data)

    def _get_signature_node(self, template):
        signature_node = xmlsec.template.create(template,
                                                c14n_method=self.c14n_algorithm,
                                                sign_method=self.signature_algorithm)
        template.append(signature_node)
        ref = xmlsec.template.add_reference(signature_node, self.digest_algorithm)
        xmlsec.template.add_transform(ref, self.method)
        
        return signature_node

    def get_signature_node(self, template):
        return self.core.get_signature_node(template) or self._get_signature_node(template)

    def get_key_info(self, signature_node):
        return self.core.get_key_info(signature_node)

    def get_signature_context(self):
        return self.core.get_signature_context()
    
    def get_key(self, key_data, password):
        return self.core.get_key(key_data, password)

    def get_cert(self, cert_data, key):
        return self.core.get_cert(cert_data, key)

    def sign(self, data, key_data, cert_data, password=None):
        # Load document file.
        template = self.get_root(data)
        # Create or Get a signature template for RSA-SHA1 enveloped signature.
        signature_node = self.get_signature_node(template)
        # Add the <ds:KeyInfo/> and <ds:KeyName/> nodes.
        key_info = self.get_key_info(signature_node)
        # Create a digital signature context (no key manager is needed).
        ctx = self.get_signature_context()
        # Load private key
        key = self.get_key(key_data, password)
        # Load the certificate and add it to the key.
        cert = self.get_cert(cert_data, key)
        # Set the key on the context.
        ctx.key = key
        # Sign the template.
        ctx.sign(signature_node)
        # Return the template
        return template


class XMLVerifier:
    def __init__(self):
        self.core = XMLCore()

    def get_root(self, data):
        return self.core.get_root(data)

    def get_signature_node(self, template):
        return self.core.get_signature_node(template)

    def get_signature_context(self):
        return self.core.get_signature_context()

    def get_key(self, key_data, password):
        return self.core.get_key(key_data, password)

    def verify(self, data, key_data, password=None):
        # Load document file.
        template = self.get_root(data)
        # Create or Get a signature template for RSA-SHA1 enveloped signature.
        signature_node = self.get_signature_node(template)
        # Create a digital signature context (no key manager is needed).
        ctx = self.get_signature_context()
        # Load private key
        key = self.get_key(key_data, password)
        # Set the key on the context.
        ctx.key = key

        try:
            return ctx.verify(signature_node) is None
        except:
            return False
