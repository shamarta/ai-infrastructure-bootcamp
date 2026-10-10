from abc import ABC, abstractmethod


class CloudProvider(ABC):
    @abstractmethod
    def create_server(self, name):
        pass

    @abstractmethod
    def delete_server(self, name):
        pass


class AzureProvider(CloudProvider):
    def create_server(self, name):
        return f"Azure: created VM '{name}'"

    def delete_server(self, name):
        return f"Azure: deleted VM '{name}'"


class BrokenProvider(CloudProvider):
    def create_server(self, name):
        return f"Created '{name}'"
    # delete_server رو پیاده‌سازی نکرده!


azure = AzureProvider()
print(azure.create_server("web-1"))

try:
    broken = BrokenProvider()
except TypeError as e:
    print(f"❌ {e}")

try:
    generic = CloudProvider()
except TypeError as e:
    print(f"❌ {e}")