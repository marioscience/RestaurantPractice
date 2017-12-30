import graphene
import restaurant.schema


class Mutation(restaurant.schema.Mutation, graphene.ObjectType):
	pass


class Query(restaurant.schema.Query, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query, mutation=Mutation)