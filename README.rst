SignXML Sunat: XML Signature in Python for SUNAT
================================

*SignXML Sunat* is an implementation of the W3C `XML Signature <http://en.wikipedia.org/wiki/XML_Signature>`_ standard in
Python.
*SignXML Sunat* implements all of the required components of the standard, and most recommended ones. Its features are:

* Well-supported, portable, reliable dependencies: `lxml <https://github.com/lxml/lxml>`_, `xmlsec
  <https://github.com/mehcode/python-xmlsec>`_, `
* Simple interface with useful defaults
* Compactness, readability, and extensibility

Installation
------------
::

    pip install signxml_sunat

Note: SignXML depends on `lxml <https://github.com/lxml/lxml>`_ and `xmlsec
<https://github.com/mehcode/python-xmlsec>`_

+--------------+----------+-------------------------------------------------------------------------------------------------+
| OS           | Python   | Command                                                                                         |
+==============+==========+=================================================================================================+
+--------------+----------+-------------------------------------------------------------------------------------------------+
| Ubuntu 16.04,| Python 3 |                                                                                                 |
| 18.04        |          | ``pip install lxml xmlsec``                                                                     |
+--------------+----------+-------------------------------------------------------------------------------------------------+

Note: In windows you need install a binary for lxml and xmlsec <https://www.lfd.uci.edu/~gohlke/pythonlibs>

Synopsis
--------

SignXML uses the ElementTree API (also supported by lxml) to work with XML data.

.. code-block:: python

    from signxml import XMLSigner, XMLVerifier

    signed_root = XMLSigner().sign('doc.xml', key_data='rsakey.pem', cert_data='rsacert.pem')
    # if you need password
    # signed_root = XMLSigner().sign('doc.xml', key_data='rsakey.pem', cert_data='rsacert.pem', password='p4ssw0rd')
    verified = XMLVerifier().verify('signed_doc.xml', key_data='rsakey.pem')
    # if you need password
    # verified_data = XMLVerifier().verify('signed_doc.xml', key_data='rsakey.pem', password='p4ssw0rd')


Authors
-------
* Danilo Britto Nuñez

Bugs
~~~~
Please report bugs, issues, feature requests, etc. on `GitHub <https://github.com/danilobrinu/signxml_sunat/issues>`_.