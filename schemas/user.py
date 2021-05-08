from marshmallow import Schema, fields


class UserSchema(Schema):
    userUUID = fields.UUID()
    firstName = fields.Str()
    lastName = fields.Str()
    email = fields.Email()
    password = fields.Str()
    primaryPhone = fields.Str()
    secondaryPhone = fields.Str()
    role = fields.Str()
