import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from .model.Department import Department as DepartmentModel
from .model.Employee import Employee as EmployeeModel
from .model.Role import Role as RoleModel
from .model.Task import Task as TaskModel


class Department(MongoengineObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (Node,)


class Role(MongoengineObjectType):
    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Task(MongoengineObjectType):
    class Meta:
        model = TaskModel
        interfaces = (Node,)


class Employee(MongoengineObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(Employee)
    all_roles = MongoengineConnectionField(Role)
    role = graphene.Field(Role)


schema = graphene.Schema(query=Query, types=[Department, Employee, Role])
