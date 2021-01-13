"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="WingBeats",
    version="0.0.1",
    openapi_version="3.0.3",
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

# add swagger tags that are used for endpoint annotation
tags = [
    {
        'name': 'File',
        'description': 'For managing a file/files'
    },
    {
        'name': 'Upload',
        'description': 'For uploading a file'
    },
    {
        'name': 'Prediction',
        'description': 'For triggering prediction on a file'
    },
]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)


class FileDescSchema(Schema):
    filename = fields.Str()
    type = fields.Str()


class FilesSchema(Schema):
    files = fields.List(fields.Nested(FileDescSchema))


class DescSchema(Schema):
    description = fields.Str()
