from graphene_django.types import DjangoObjectType
import graphene
from . import models

## TODO: Figure out how to do partial updates using graphene

# Category Schema
class CategoryType(DjangoObjectType):
	class Meta:
		model = models.Category


class CreateCategory(graphene.Mutation):
	class Arguments:
		name = graphene.String()
		description = graphene.String()

	success = graphene.Boolean()
	category = graphene.Field(lambda: CategoryType)

	@staticmethod
	def mutate(self, info, name, description):
		category = models.Category.objects.create(name=name, description=description)
		success = True
		return CreateCategory(category=category, success=success)


class UpdateCategory(graphene.Mutation):
	class Arguments:
		category_id = graphene.String()
		name = graphene.String()
		description = graphene.String()

	success = graphene.Boolean()
	category = graphene.Field(lambda: CategoryType)

	@staticmethod
	def mutate(self, info, category_id, name, description):
		category = models.Category.objects.get(pk=category_id)

		category.name = name
		category.description = description

		category.save()
		success = True
		return CreateCategory(category=category, success=success)


class DeleteCategory(graphene.Mutation):
	class Arguments:
		category_id = graphene.String()

	success = graphene.Boolean()

	@staticmethod
	def mutate(self, info, category_id):
		models.Category.objects.get(pk=category_id).delete()
		success = True
		return DeleteCategory(success=success)


# Dish Schema
class DishType(DjangoObjectType):
	class Meta:
		model = models.Dish


class CategoryInputType(graphene.InputObjectType):
	id = graphene.String()


class CreateDish(graphene.Mutation):
	class Arguments:
		name = graphene.String()
		category = graphene.Argument(CategoryInputType)
		description = graphene.String()
		price = graphene.Float()

	success = graphene.Boolean()
	dish = graphene.Field(lambda: DishType)

	@staticmethod
	def mutate(self, info, name, category, description, price):
		category_obj = models.Category.objects.get(id=category.id)
		dish = models.Dish.objects.create(name=name, category=category_obj, description=description, price=price)
		success = True
		return CreateDish(dish=dish, success=success)


class UpdateDish(graphene.Mutation):
	class Arguments:
		dish_id = graphene.String()
		name = graphene.String()
		category = graphene.Argument(CategoryInputType)
		description = graphene.String()
		price = graphene.Float()

	success = graphene.Boolean()
	dish = graphene.Field(lambda: DishType)

	@staticmethod
	def mutate(self, info, dish_id, name, category, description, price):
		dish_obj = models.Dish.objects.get(pk=dish_id)

		category_obj = models.Category.objects.get(pk=category.id)
		dish_obj.category = category_obj
		dish_obj.name = name
		dish_obj.description = description
		dish_obj.price = price
		dish_obj.save()

		success = True
		return UpdateDish(dish=dish_obj, success=success)


class DeleteDish(graphene.Mutation):
	class Arguments:
		dish_id = graphene.String()

	success = graphene.Boolean()

	@staticmethod
	def mutate(self, info, dish_id):
		models.Dish.objects.get(pk=dish_id).delete()
		success = True
		return DeleteDish(success=success)


# Mutations
class Mutation(graphene.ObjectType):
	create_category = CreateCategory.Field()
	update_category = UpdateCategory.Field()
	delete_category = DeleteCategory.Field()

	create_dish = CreateDish.Field()
	update_dish = UpdateDish.Field()
	delete_dish = DeleteDish.Field()


# Read Queries
class Query(object):
	all_categories = graphene.List(CategoryType)
	all_dishes = graphene.List(DishType)

	@staticmethod
	def resolve_all_categories(self, info):
		return models.Category.objects.all()

	@staticmethod
	def resolve_all_dishes(self, info):
		return models.Dish.objects.all()