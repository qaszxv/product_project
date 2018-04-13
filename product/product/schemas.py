from marshmallow import Schema, fields


class Product(Schema):
    name = fields.Str(required=True)
    staple_name = fields.Str(required=True)
    description = fields.Str(required=True)
    preview_image = fields.Str(required=True)
    categories = fields.List(fields.String(), required=True)
    final_gross_price = fields.Integer(required=True)
    final_net_price = fields.Integer(required=True)
    url = fields.Str(required=True)
    manufacturer = fields.Str(required=True)