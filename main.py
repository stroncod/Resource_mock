import strawberry
from schema import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
