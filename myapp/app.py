from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listVehicles_resolver, getVehicle_resolver
from api.mutations import create_vehicle_resolver, update_vehicle_resolver, delete_vehicle_resolver
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport



query = ObjectType("Query")
query.set_field("listVehicles", listVehicles_resolver)
query.set_field("getVehicle", getVehicle_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createVehicle", create_vehicle_resolver)
mutation.set_field("updateVehicle", update_vehicle_resolver)
mutation.set_field("deleteVehicle", delete_vehicle_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation,
                                snake_case_fallback_resolvers)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code


# @app.route('/getVehicle')
# def getVehicleById():
#     id = request.args.get('id')
#     print("ID  = ", id)
#     # Provide a GraphQL query
#     query = gql("""
#     query Query {
#     getVehicle(id: %s) {
#         success
#         errors
#         vehicle {
#         model
#         wheel
#         created_at
#         id
#         }
#     }
#     }
#     """ % id)

#     # Execute the query on the transport
#     result = client.execute(query)
#     return result

# @app.route('/listVehicles')
# def allVehicles():
#     # Provide a GraphQL query
#     query = gql("""
#     query Query{
#     listVehicles {
#         success
#         errors
#         vehicles {
#         id
#         model
#         wheel# # Select your transport with a defined url endpoint
# transport = AIOHTTPTransport(url="http://127.0.0.1:5000/graphql")

# # Create a GraphQL client using the defined transport
# client = Client(transport=transport, fetch_schema_from_transport=True)

#     # Execute the query on the transport
#     result = client.execute(query)
#     return result

# @app.route('/createVehicle')
# def createVehicle():
#     model = request.args.get('model')
#     wheel = request.args.get('wheel')
#     # Provide a GraphQL query
#     query = gql("""
#     mutation Mutation{
#     createVehicle(model: %s, wheel: %s) {
#         success
#         errors
#         vehicle {
#         id
#         model
#         wheel
#         created_at
#         }
#     }
#     }
#     """ % (model, wheel))

#     # Execute the query on the transport
#     result = client.execute(query)
#     return result

