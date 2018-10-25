from __future__ import unicode_literals
from .models import ssm_backends
from ..core.models import base_decorator
from ..core.models import deprecated_base_decorator

ssm_backend = ssm_backends['us-east-1']
mock_ssm = base_decorator(ssm_backends)
mock_ssm_deprecated = deprecated_base_decorator(ssm_backends)
