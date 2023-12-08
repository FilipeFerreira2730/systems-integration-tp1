import lxml.etree as ET
"""def validator(filename):
    xmlschema_doc = ET.parse("./rpc-server/XML/premierLeagueXSD.xsd")
    xmlschema = ET.XMLSchema(xmlschema_doc)

    xml_doc = ET.parse(f"./rpc-server/XML/{filename}.xml")
    result = xmlschema.validate(xml_doc)

    print (xmlschema.validate(xml_doc))
    for error  in xmlschema.error_log:
        print ("ERROR ON LINE %s: %s" % (error.line, error.message.encode("utf-8")))

    #print(result)"""

def validator(filename):
    try:
        # Load the XML Schema
        xmlschema_doc = ET.parse("./rpc-server/XML/ISXSD.xsd")
        xmlschema = ET.XMLSchema(xmlschema_doc)

        # Load the XML document
        xml_doc = ET.parse(f"./rpc-server/XML/{filename}.xml")

        # Validate the XML document against the XML Schema
        result = xmlschema.validate(xml_doc)

        # Print the validation result
        print(f"Validation Result: {result}")

        # Print any validation errors
        if not result:
            print("Validation Errors:")
            for error in xmlschema.error_log:
                print(f"ERROR ON LINE {error.line}: {error.message.encode('utf-8')}")

    except ET.XMLSchemaParseError as e:
        print(f"Error parsing XML Schema: {e}")
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML document: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

validator("test")