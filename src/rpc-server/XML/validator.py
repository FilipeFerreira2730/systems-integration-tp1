import lxml.etree as ET
def validator(filename):
    xmlschema_doc = ET.parse("./rpc-server/XML/premierLeagueXSD.xsd")
    xmlschema = ET.XMLSchema(xmlschema_doc)

    xml_doc = ET.parse(f"./rpc-server/XML/{filename}.xml")
    result = xmlschema.validate(xml_doc)

    print (xmlschema.validate(xml_doc))
    for error  in xmlschema.error_log:
        print ("ERROR ON LINE %s: %s" % (error.line, error.message.encode("utf-8")))

    #print(result)