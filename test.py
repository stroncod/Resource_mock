from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="http://0.0.0.0:8000/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query{
            instruments(site:"s",date:"2019-02-01"){
                name
        }
    }
"""
)

# Execute the query on the transport
result = client.execute(query)
print(result)
