import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from XML.converter import converter
from XML.insertData import insertData
from XML.validator import validator
from functions.Connection import get_connection
from XML.softDeleteExp import deleteData
from functions.string_length import string_length
from functions.string_reverse import string_reverse
from functions.queries import jogos_fora, total_vitorias, result_jogos, media_golos, datas_jogos, count_jogos
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
    server.register_function(insertData)
    server.register_function(validator)
    server.register_function(get_connection)
    server.register_function(deleteData)
    server.register_function(jogos_fora)
    server.register_function(total_vitorias)
    server.register_function(result_jogos)
    server.register_function(media_golos)
    server.register_function(datas_jogos)
    server.register_function(count_jogos)
    

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
