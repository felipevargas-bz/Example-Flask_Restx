# Create app
from flask import Flask, request
from flask_restx import Api, fields, Resource, Namespace
from datetime import datetime
from .schemas import InvoiceModel, json_data

# Creamos la app Flask normalmente
app = Flask(__name__)

# Esta linea de codigo es para desactivar un campo llamado X-Fields
# Que se genera automaticamente por defecto por flask-restx 
app.config['RESTX_MASK_SWAGGER'] = False

# Aquí lo que hacemos es crear una instancia de la Api
# le pasamos el objeto app que creamos anteriormente
# le pasamos un nombre, una descripción y una versión
# el prefix es el prefijo que se usará en todas las rutas
api = Api(
    app,
    version='1.0',
    title='Certificates API',
    description='A simple Certificates API',
    prefix='/api/v1',
)
"""
Mediante el objeto api, creamos un nuevo namespace

los namespaces son una forma de organizar nuestras rutas
es decir, si tenemos una ruta /api/v1/certs/something

para saber que es certs, vayanse aal final de este archivo
ahí encontrarán la siguiente linea de codigo
'api.add_namespace(ns, path='/certs')'
que lo que hace es agregar un nuevo namespace a la api


funcionan igual que el Blueprint de Flask

puedes crear tantos namespaces como quieras
"""



ns = Namespace('certificates', description='Certificates operations')


"""
Lo que siguiente es una forma de crear un schema de datos

Estos schemas son los usados en la documentación como ejemplo
de que datos se van a mandar a nuetra API y también que datos se
van a responder de nuestra API.

Para definir un schema de datos, debemos usar el objeto api.model
o también con nestros namespaces creados desde la clase Namespace
bien sea con el objeto api o con el objeto ns ambas son válidas.
recibe un nombre y un diccionario con los datos del schema

el diccionario tiene que tener una clave 'type' y un valor
el valor se debe definir mediante el objeto fields importado de flask-restx
que nos permite definir los tipos de datos que se van a usar.

podemos definir schemas de datos mas complejos, como una lista de datos
o un diccionario de datos que contiene otro diccionario de datos o una lista
de diccionarios de datos

aquí un ejemplo de un schema de datos complejo {InvoiceModel}

este schema representa lo siguiente en formato JSON: {json_data}
""".format(InvoiceModel, json_data)

ByidModel = ns.model('GetByid', {
    'id': fields.Integer(required=True, description='The unique identifier of a Certificate')
})

# Aqui un ejemplo de un schema de datos mas simple
CertsModel = ns.model('Cert', {
    'CreateDate': fields.DateTime(description='The date this Certificate was created'),
    'UpdateDate': fields.DateTime(description='The date this Certificate was updated'),
    'CreateBy': fields.String(description='The user that created this Certificate'),
    'UpdateBy': fields.String(description='The user that updated this Certificate'),
    'IsDeleted': fields.Boolean(description='Is this Certificate deleted?'),
    'IssuerNit': fields.String(required=True, description='The Nit of the Issuer of this Certificate'),
    'Key': fields.String(required=True, description='The Key of this Certificate'),
    'Format': fields.String(required=True, description='The Format of this Certificate'),
    'Description': fields.String(description='The Description of this Certificate'),
    'DueDate': fields.DateTime(required=True, description='The DueDate of this Certificate'),
})

ListCertsModel = ns.model('ListCerts', {
    'Certificates': fields.List(fields.Nested(CertsModel))   
})

ErorModel = ns.model('Error', {
    'message': fields.String(required=True, description='The error message')
})

# Creamos una ruta para nuestra API con el objeto ns
# de la clase Namespace
# la ruta es /api/v1/certs/get
# muy similar a lo que hacemos con los Blueprint de Flask
@ns.route('/get')
# Creamos una clase que hereda de Resource
# que es la forma en que se define y ejecutan las acciones
# de nuestra API
class GetAll(Resource):
    # empezamos dandole un indicativo a la documentación diciendole que estamos haciendo
    # en el siguiente formato
    @ns.doc('get_all_certificates')
    # El marshal_with indica a nuestra documentación que datos se esperan revolver desde nuestra API
    # Por lo que usamos un schema de respuesta para indicarlo
    @ns.marshal_with(ListCertsModel)
    # Aquí en modo de función indicamos en metodo por el que se va a llamar
    # a nuestra ruta, y debajo las acciones tal cual y como se definen en Flask normal.
    
    # Prestar mucha atención a los demás ajemplos
    
    def get(self):
        """
        Get all Certificates


        Obtiene todos los Certificates almacenados en la base de datos
        """
        return [
            {
            'id': 1,
            'CreateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'UpdateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'CreateBy': 'admin',
            'UpdateBy': 'admin',
            'IsDeleted': False,
            'IssuerNit': '123456789',
            'Key': '123456789',
            'Format': '123456789',
            'Description': '123456789',
            'DueDate': '123456789',
        },
            {
            'id': 2,
            'CreateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'UpdateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'CreateBy': 'admin',
            'UpdateBy': 'admin',
            'IsDeleted': False,
            'IssuerNit': '123456789',
            'Key': '123456789',
            'Format': '123456789',
            'Description': '123456789',
            'DueDate': '123456789',
        },
            {
            'id': 3,
            'CreateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'UpdateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'CreateBy': 'admin',
            'UpdateBy': 'admin',
            'IsDeleted': False,
            'IssuerNit': '123456789',
            'Key': '123456789',
            'Format': '123456789',
            'Description': '123456789',
            'DueDate': '123456789',
        },
        ]

"""
Este ejemplo es una forma de definir una ruta que recibe un parámetro
y como vemos se muestra la forma en que se le indica a la Documentación

que codigos de respuesta y con que descripción se van a devolver
"""
@ns.route('/data/<int:id>/get')
@ns.response(404, 'Certificate not found')
@ns.response(500, 'Internal Server Error')
@ns.response(400, 'Bad Request')
@ns.response(200, 'OK')
# en este apartado de param, incicamos en caso de que el parámetro
# o los parametros a recibir sean variables normales, y no complejas como
# un json, o una lista de datos
# Al igual que @ns.response, podemos poner varios según la necesidad
# y cantidad de parametros que se van a recibir con su respectiva descripción
@ns.param('id', 'The Certificate identifier')
class GetByid(Resource):
    @ns.doc('get_certificate_by_id')
    @ns.marshal_with(CertsModel)
    def get(self, id):
        """
        Get Certificate by id
        
        
        Obtiene un Certificado dado su id
        """
        return {
            'id': id,
            'CreateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'UpdateDate': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'CreateBy': 'admin',
            'UpdateBy': 'admin',
            'IsDeleted': False,
            'IssuerNit': '123456789',
            'Key': '123456789',
            'Format': '123456789',
            'Description': '123456789',
            'DueDate': '123456789',
        }


"""
Este ejemplo nos muestra como definir una ruta que recibe como parametro
un JSON y que también responde un JSON
"""
@ns.route('/new')
@ns.response(201, 'Certificate successfully created.')
class NewData(Resource):
    @ns.doc('create_new_certificate')
    # el @ns.expect sirve para indicarle a la documentación un modelo de lo que esperamos
    # recibir en nuestra API, este modelo sirve para rellenar un JSON que posterior mente será enviado
    # a nuestra API
    @ns.expect(CertsModel)
    # el @ns.marshal_with como ya se indicó nos sirve para indicar un modelo de respuesta de nuestra API
    @ns.marshal_with(CertsModel)
    def post(self):
        """
        Create a new Certificate
        
        
        Crea un nuevo Certificado
        """
        return {
            'data': {
                'CreateDate': request.json['CreateDate'],
                'UpdateDate': request.json['UpdateDate'],
                'CreateBy': request.json['CreateBy'],
                'UpdateBy': request.json['UpdateBy'],
                'IsDeleted': request.json['IsDeleted'],
                'IssuerNit': request.json['IssuerNit'],
                'Key': request.json['Key'],
                'Format': request.json['Format'],
                'Description': request.json['Description'],
                'DueDate': request.json['DueDate']
            }
        }


@ns.route('/update')
@ns.response(201, 'Certificate successfully updated.')
class UpdateData(Resource):
    @ns.doc('update_certificate')
    @ns.marshal_with(CertsModel)
    def put(self):
        """
        Update a Certificate
        
        
        Actualiza un Certificado
        """
        return {
            'data': {
                'CreateDate': request.json['CreateDate'],
                'UpdateDate': request.json['UpdateDate'],
                'CreateBy': request.json['CreateBy'],
                'UpdateBy': request.json['UpdateBy'],
                'IsDeleted': request.json['IsDeleted'],
                'IssuerNit': request.json['IssuerNit'],
                'Key': request.json['Key'],
                'Format': request.json['Format'],
                'Description': request.json['Description'],
                'DueDate': request.json['DueDate']
            }
        }


@ns.route('/delete/<int:id>')
@ns.response(404, 'Certificate not found.')
class DeleteData(Resource):
    @ns.doc('delete_certificate')
    @ns.marshal_with(CertsModel)
    def delete(self, id):
        """
        Delete a Certificate by id
        
        
        Elimina un Certificado dado su id
        """
        return {'OK': 'El Certificado con id {} ha sido eliminado'.format(id)}

"""
De la siguiente manera podemos registrar nuestros ns o namespaces
que como se indicó anteriormente, son una forma de agrupar todas las rutas

es similar o casi identico a lo que es el Blueprint de Flask
podemos crear tantos como  queramos y le podemos undicar un prefix que en este caso de ve como
path='/certs'
"""
api.add_namespace(ns, path='/certs')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
