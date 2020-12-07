"""

Ideas from
- https://github.com/rvinzent/django-dynamic-models

"""

import sys
from django.db import models
from django.apps import apps


__all__ = []

DEFS = {'models':
        [{'name': 'Boat',
          'fields': [['type', 'char10'],
                     ['name', 'char'],
                     ['inauguration', 'datetime']]
          },
         {'name': 'Sail',
          'fields': [['type', 'char40'],
                     ['color', 'char20']]
         },
         ]
        }


FIELDTYPES = {
    'char': models.CharField,
    'datetime': models.DateTimeField,
}


current_module = sys.modules[__name__]
app_name = apps.get_app_config('trial').name
for model in DEFS['models']:
    fields = {}
    for field in model['fields']:
        typ = field[1]
        # Set field attributes where given
        attrs = {}
        if typ.startswith('char'):
            length = typ[4:]
            length = int(length) if length else 80
            attrs['max_length'] = length
            # Adjust type
            typ = 'char'
        # Set the actual field type; fail hard when the type does
        # not exist
        fields[field[0]] = FIELDTYPES[typ](**attrs)
    # Add attributes required by Django
    fields['__module__'] = app_name

    name = model['name']
    model = type(name.capitalize(), (models.Model,), fields)

    __all__.append(name.capitalize())
    setattr(current_module, name, model)
