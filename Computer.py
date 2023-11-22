from abc import ABC , abstractmethod


# Product
class OperatingSystem:
    def __init__(self, name, default_applications=None, bit_version=None, kernel_version=None, release_date=None):
        self.name = name
        self.default_applications = default_applications or []  # Assuming a list of default applications
        self.bit_version = bit_version
        self.kernel_version = kernel_version
        self.release_date = release_date

    def __str__(self):
        return f"OperatingSystem(name={self.name}, bit_version={self.bit_version}, kernel_version={self.kernel_version}, release_date={self.release_date}, default_applications={self.default_applications})"


class Computer:
    def __init__(self, cpu, ram, storage, system, motherboard, cooling):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.system = system
        self.motherboard = motherboard
        self.cooling = cooling

    def __str__(self):
        return f"Computer [CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, System: {self.system}, Motherboard: {self.motherboard}, Cooling: {self.cooling}]"

# Builder
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("Default CPU", "Default RAM", "Default Storage", "Default System", "Default Motherboard", "Default Cooling")

    def build(self):
        return self.computer

    def with_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def with_ram(self, ram):
        self.computer.ram = ram
        return self

    def with_storage(self, storage):
        self.computer.storage = storage
        return self

    def with_system(self, system):
        self.computer.system = system
        return self

    def with_motherboard(self, motherboard):
        self.computer.motherboard = motherboard
        return self

    def with_cooling(self, cooling):
        self.computer.cooling = cooling
        return self
    
class OperatingSystemBuilder:
    def __init__(self, name):
        self.os = OperatingSystem(name)

    def with_default_applications(self, default_applications):
        self.os.default_applications = default_applications
        return self

    def with_bit_version(self, bit_version):
        self.os.bit_version = bit_version
        return self

    def with_kernel_version(self, kernel_version):
        self.os.kernel_version = kernel_version
        return self

    def with_release_date(self, release_date):
        self.os.release_date = release_date
        return self

    def build(self):
        return self.os

# Director
class ComputerDirector:
    def build_high_end_computer(self, builder):
        return builder.with_cpu("Intel i9").with_ram("32GB").with_storage("1TB SSD").with_system("Windows 10").with_motherboard("XYZ Model").with_cooling("Liquid Cooling").build()

    def build_minimal_requirement_pc(self, builder, cpu, ram, storage):
        return builder.with_cpu(cpu).with_ram(ram).with_storage(storage).build()
    
# Client
if __name__ == "__main__":
    
    os_builder = OperatingSystemBuilder("ExampleOS")
    os = os_builder.with_default_applications(["App1", "App2"]).with_bit_version(64).with_kernel_version("2.6.32").with_release_date("2023-01-01").build()

    
    builder = ComputerBuilder()
    director = ComputerDirector()

    high_end_computer = director.build_high_end_computer(builder)
    print(high_end_computer)

    minimal_computer = director.build_minimal_requirement_pc(builder, "Intel i5", "8GB", "256GB SSD")
    print("Minimal requirement PC:", minimal_computer)