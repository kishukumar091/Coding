class Property:
    def _init_(self, prop_id, address, price, status):
        self.prop_id = prop_id
        self.address = address
        self.price = price
        self.status = status

class Tenant:
    def _init_(self, tenant_id, name, property_id):
        self.tenant_id = tenant_id
        self.name = name
        self.property_id = property_id

class RealEstateManagementSystem:
    def _init_(self):
        self.properties = []
        self.tenants = []

    def add_property(self, prop_id, address, price, status):
        property_obj = Property(prop_id, address, price, status)
        self.properties.append(property_obj)
        print("Property added successfully.")

    def add_tenant(self, tenant_id, name, property_id):
        tenant_obj = Tenant(tenant_id, name, property_id)
        self.tenants.append(tenant_obj)
        print("Tenant added successfully.")

    def generate_property_report(self):
        print("Property Report:")
        for property_obj in self.properties:
            print(f"Property ID: {property_obj.prop_id}, Address: {property_obj.address}, Price: {property_obj.price}, Status: {property_obj.status}")

    def generate_tenant_report(self):
        print("Tenant Report:")
        for tenant_obj in self.tenants:
            print(f"Tenant ID: {tenant_obj.tenant_id}, Name: {tenant_obj.name}, Property ID: {tenant_obj.property_id}")

# Sample usage
if __name__ == "_main_":
    real_estate_system = RealEstateManagementSystem()

    # Adding properties
    real_estate_system.add_property(1, "123 Main St", 200000, "Available")
    real_estate_system.add_property(2, "456 Elm St", 300000, "Rented")

    # Adding tenants
    real_estate_system.add_tenant(101, "John Doe", 1)
    real_estate_system.add_tenant(102, "Jane Smith", 2)

    # Generating reports
    real_estate_system.generate_property_report()
    real_estate_system.generate_tenant_report()