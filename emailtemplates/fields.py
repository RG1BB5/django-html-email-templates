from django.db import models
from .settings import get_email_template_model


class EmailTemplateField(models.ForeignKey):
    def __init__(self, on_delete, **kwargs):
        model = get_email_template_model()
        kwargs['to'] = "{0}.{1}".format(model._meta.app_label, model._meta.model_name)
        kwargs['on_delete'] = on_delete
        super().__init__(**kwargs)
