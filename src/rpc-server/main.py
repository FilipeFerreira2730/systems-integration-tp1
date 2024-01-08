import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from XML.converter import converter
from XML.insertData import insertData1
from XML.validator import validator
from functions.Connection import get_connection
from XML.softDeleteExp import deleteData
from functions.string_length import string_length
from functions.string_reverse import string_reverse
from functions.queries import jogos_casa, jogos_ano, resultado_jogos, total_golos, media_golos_equipa, numero_vitorias
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()


    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(string_reverse)
    server.register_function(string_length)
    server.register_function(converter)
    server.register_function(insertData1)
    server.register_function(validator)
    server.register_function(get_connection)
    server.register_function(deleteData)
    server.register_function(jogos_casa)
    server.register_function(jogos_ano)
    server.register_function(resultado_jogos)
    server.register_function(total_golos)
    server.register_function(media_golos_equipa)
    server.register_function(numero_vitorias)
    

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
