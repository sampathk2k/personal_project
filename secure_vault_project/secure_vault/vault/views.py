from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SecureDocument
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

@login_required
def dashboard(request):
    """ Display the dashboard with user-uploaded secure documents. """
    documents = SecureDocument.objects.filter(user=request.user)  # Fetch user's documents
    return render(request, "dashboard.html", {"documents": documents})

@login_required
def upload_document(request):
    if request.method == "POST":
        file = request.FILES['document']
        encrypted_data = cipher_suite.encrypt(file.read())

        SecureDocument.objects.create(
            user=request.user,
            file_name=file.name,
            encrypted_data=encrypted_data
        )
        return redirect("dashboard")  # Redirect to dashboard after upload
    return render(request, "upload.html")

@login_required
def download_document(request, doc_id):
    document = get_object_or_404(SecureDocument, id=doc_id, user=request.user)
    decrypted_data = cipher_suite.decrypt(document.encrypted_data)

    response = HttpResponse(decrypted_data, content_type="application/octet-stream")
    response["Content-Disposition"] = f'attachment; filename="{document.file_name}"'
    return response