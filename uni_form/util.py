from django.template.loader import render_to_string
from django.template import Context

class BaseInput(object):
    """
        An base Input class to reduce the amount of code in the Input classes.
    """
    template = "uni_form/input.html"
    
    def __init__(self,name,value):
        self.name = name
        self.value = value
        
    def render(self, **extra_context):
        vars = dict(extra_context, input=self)
        if hasattr(self.template, "render"):
            return self.template.render(Context(vars))
        return render_to_string(self.template, vars)

class Toggle(object):
    """
        A container for holder toggled items such as fields and buttons.
    """
    
    fields = []
