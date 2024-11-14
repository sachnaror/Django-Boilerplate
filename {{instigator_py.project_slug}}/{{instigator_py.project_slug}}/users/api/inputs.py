import graphene


class CreateUserInput(graphene.InputObjectType):
    {%- if instigator_py.username_type == "email" %}
    email = graphene.String()
     {%- else %}
    username = graphene.String()
    {%- endif %}
    password = graphene.String()
    phone_number = graphene.String()

class UpdateUserInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name= graphene.String()
    {%- if instigator_py.username_type == "email" %}
    email = graphene.String()
    {%- else %}
    username = graphene.String()
    {%- endif %}
