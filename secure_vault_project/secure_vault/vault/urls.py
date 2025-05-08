from django.urls import path
from .views import dashboard, upload_document, download_document

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("upload/", upload_document, name="upload_document"),
    path("download/<int:doc_id>/", download_document, name="download_document"),
]