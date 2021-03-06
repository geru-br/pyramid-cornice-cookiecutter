from pyramid.view import view_config
from cornice import Service
import colander
from cornice.validators import colander_body_validator


@view_config(route_name='home', renderer='templates/mytemplate.{{ "pt" if "chameleon" == cookiecutter.template_language else cookiecutter.template_language }}')
def my_view(request):
    return {'project': '{{ cookiecutter.project_name }}'}



class RequestSchema(colander.MappingSchema):
    """
    """
    uuid = colander.SchemaNode(colander.String(), description='UUID')


requests_post = Service(name='resources_post', path='/api/v1/resource', tags=['resources'])
requests_get = Service(name='resource_get', path='/api/v1/resource/{uuid}', tags=['resources'])


@requests_post.post(schema=RequestSchema(), validators=(colander_body_validator,))
def _requests_post(request):
    uuid = request.validated['uuid']
    return uuid


@requests_get.get()
def _requests_get(request):
    return request.matchdict['uuid']
