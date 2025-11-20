from abc import ABC, abstractmethod

class clud_storage(ABC):

    @abstractmethod
    def connect(self):
        """Establish connection to the cloud provider."""
        pass

    @abstractmethod
    def upload_file(self, file_path: str, destination: str):
        """Upload a specific file."""
        pass
# You can also have concrete (normal) methods in an Abstract class

    def log_activity(self, message: str):
        """Log activity for debugging or monitoring."""
        print(f"Activity: {message}")


class AWSStorage(clud_storage):
    def connect(self):
        print("Authenticating with AWS IAM...")

    def upload_file(self, file_path: str, destination: str):
        self.connect()
        print(f"Uploading '{file_path}' to S3 bucket '{destination}' via boto3.")


# 3. Concrete Class B (Google Cloud Implementation)


class GCSStorage(clud_storage):
    def connect(self):
        print("Authenticating with Google Cloud Service Account...")

    def upload_file(self, file_path: str, destination: str):
        self.connect()
        print(f"Uploading '{file_path}' to GCS bucket '{destination}' via google-cloud-storage.")



obj = AWSStorage()
obj.connect()
obj.upload_file("file.txt", "bucket")
obj.log_activity("File uploaded successfully.")

obj = GCSStorage()
obj.connect()
obj.upload_file("file.txt", "bucket")
obj.log_activity("File uploaded successfully.")
