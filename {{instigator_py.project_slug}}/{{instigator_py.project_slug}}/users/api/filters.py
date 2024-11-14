from django_filters import *
from {{ instigator_py.project_slug }}.users.models import User


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
             {%- if instigator_py.username_type == "email" %}
            'email': ['exact'],
            {%- else %}
            'username': ['exact'],
            {%- endif %}
        }
