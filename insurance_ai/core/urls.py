from django.urls import path
from .views import claim_predict, compare, compare_page, hidden_clauses, policy_score, upload_policy
from .views import upload_policy, ask
from .views import upload_policy, ask, coverage
from .views import simulate
from .views import hidden_clauses
urlpatterns = [
    path('upload-policy/', upload_policy),
    path('ask/', ask),
    path('coverage/', coverage),
    path('simulate/', simulate),
    path('score/', policy_score),
    path('compare/', compare),
    path('hidden-clauses/', hidden_clauses),
    path('compare-page/', compare_page),
    path('hidden/', hidden_clauses),
    path('claim-predict/', claim_predict),
]