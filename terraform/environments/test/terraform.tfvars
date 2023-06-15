# Azure subscription vars
subscription_id = "7e85fec4-83b3-4c93-ba22-d3451c71e552"
client_id = "ad8cadab-12e5-4c8e-bbc5-5a9a02a8e969"
client_secret = "YFy8Q~J0kPrBafbqhcvw1qgbqZJCgDemhNwDWcAk"
tenant_id = "d9677abc-e9da-460d-9fc5-5c6ca1393129"

# Resource Group/Location
location = "East US 2"
resource_group = "udacity-3"
application_type = "sriapplicationqa007" # This name has to be globally unique.
#application_type = "AppService"

# Network
virtual_network_name = "sri-v-net"
address_space = ["10.5.0.0/16"]
# address_prefix_test values directly parsed as network needs list of strings and nsg-test needs strings
address_prefix_test = "10.5.1.0/24"

