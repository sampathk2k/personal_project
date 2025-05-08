from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

# Generate and store key securely (use environment variables in production)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

class SecureDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    encrypted_data = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def encrypt_file(self, raw_data):
        """ Encrypt the file before saving. """
        return cipher_suite.encrypt(raw_data)

    def decrypt_file(self):
        """ Decrypt the file upon retrieval. """
        return cipher_suite.decrypt(self.encrypted_data)