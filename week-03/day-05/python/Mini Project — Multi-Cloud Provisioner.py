from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


@dataclass
class Server:
    name: str
    provider: str
    cpu_cores: int = 2
    status: str = "running"


class CloudProvider(ABC):
    name: str

    @abstractmethod
    def create_server(self, name: str, cpu_cores: int) -> Server:
        pass

    @abstractmethod
    def delete_server(self, server: Server) -> str:
        pass


class AzureProvider(CloudProvider):
    name = "azure"

    def create_server(self, name, cpu_cores):
        return Server(name=name, provider=self.name, cpu_cores=cpu_cores)

    def delete_server(self, server):
        server.status = "deleted"
        return f"Azure: deleted VM '{server.name}'"


class AWSProvider(CloudProvider):
    name = "aws"

    def create_server(self, name, cpu_cores):
        return Server(name=name, provider=self.name, cpu_cores=cpu_cores)

    def delete_server(self, server):
        server.status = "terminated"
        return f"AWS: terminated EC2 instance '{server.name}'"


@dataclass
class Provisioner:
    provider: CloudProvider
    servers: List[Server] = field(default_factory=list)

    def deploy(self, name, cpu_cores=2):
        server = self.provider.create_server(name, cpu_cores)
        self.servers.append(server)
        print(f"✅ Created {server}")
        return server

    def teardown_all(self):
        for server in self.servers:
            print(f"🗑️  {self.provider.delete_server(server)}")


if __name__ == "__main__":
    for provider in (AzureProvider(), AWSProvider()):
        print(f"\n=== Using {provider.name.upper()} ===")
        provisioner = Provisioner(provider)
        provisioner.deploy("web-1", cpu_cores=4)
        provisioner.deploy("db-1", cpu_cores=8)
        provisioner.teardown_all()