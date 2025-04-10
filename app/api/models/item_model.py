# This function is used to Validating and Serializing Data with Flask-RestX

from flask_restx import fields

def get_item_model(api): 
    return api.model('Item', {
        'id' : fields.Integer(readOnly=True, description='The unique identifier of an item'), 
        'name' : fields.String(required=True, description='Item name'), 
        'price' : fields.Float(required=True, description='Price of items')
    }) 