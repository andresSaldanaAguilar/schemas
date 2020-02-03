import glob
md = '''
# TM Forum Open-API Schema Repository

[![CircleCI](https://circleci.com/gh/tmforum-rand/schemas/tree/master.svg?style=svg)](https://circleci.com/gh/tmforum-rand/schemas/tree/master)

This repository contains the collection of JSON-Schema files that define the entities used within the TM Forum Open-API Catalog. The directories are structured according to the Open-API Map Level-0 categories:

| Level-0 |  |
|-----------------|---|
| [Marketing/Sales](https://github.com/tmforum-rand/schemas/tree/master/MarketingSales) | The Market/Sales domain supports the sales and marketing activities needed to gain business from customers and potential customers. |
| | <schemas>${MarketingSales}<br></schemas> | |
| [Product](https://github.com/tmforum-rand/schemas/tree/master/Product/) | The Product domain is concerned with the lifecycle of products offered to and procured by customers. |
| | <schemas>${Product}<br></schemas> | |
| [Customer](https://github.com/tmforum-rand/schemas/tree/master/Customer) | The Customer domain represents individuals or organizations that obtain products from an enterprise, such as a service provider. It represents of all types of contact with the customer, the management of the relationship, and the administration of customer data. |
| | <schemas>${Customer}<br></schemas> | |
| [Service](https://github.com/tmforum-rand/schemas/tree/master/Service) | The Service Domain is concerned with the definition, development, and operational aspects of Services used to realize offerings to the market. |
| | <schemas>${Service}<br></schemas> | |
| [Resource](https://github.com/tmforum-rand/schemas/tree/master/Resource) | The Resource domain is concerned with the definition, development, and operational aspects of the applications, computing, and networks which represent the infrastructure of an enterprise. |
| | <schemas>${Resource}<br></schemas> | |
| [Engaged Party](https://github.com/tmforum-rand/schemas/tree/master/EngagedParty) | The Engaged Party domain encompasses planning of strategies for Engaged Parties, handling of all types of contact with Engaged Parties, the management of the relationship, and the administration of Engaged Parties data. |
| | <schemas>${EngagedParty}<br></schemas> | |
| [Enterprise](https://github.com/tmforum-rand/schemas/tree/master/Enterprise) | The Enterprise domain provides support and sets policy for the overall business, enterprise or Service Provider. It also includes activities that are common to all enterprises across all industries such as accounting and human resource management. |
| | <schemas>${Enterprise}<br></schemas> | |
| [Common](https://github.com/tmforum-rand/schemas/tree/master/Common) | The common domain is of different nature from the above defined ones as the processes, information data and applications described there do not necessarily have relationships. |
| | <schemas>${Common}<br></schemas> | |

All schemas conform to JSON-Schema draft-07, and to [the design guidelines described here](https://github.com/tmforum-rand/TMF630_REST_API_Design_Guidelines). The schemas are used in the construction of the TM Forum Open-API catalog.


'''
schemaTree = {}
for domain in glob.glob("../*/"):
    domainName = domain.split('/')[-2].replace("/","")
    schemaTree[domainName] = {}
    schemasForDomain = glob.glob(domain+"*")
    for schema in schemasForDomain:
        schema = schema.split("/")[-1]
        schemaTree[domainName][schema] = {
            "name": schema,
            "url": "https://raw.githubusercontent.com/tmforum-rand/schemas/gh-pages/"+domainName+"/"+schema 
        }

for domain in schemaTree:
    print(domain)
    schemaMd = ""
    for schema in schemaTree[domain]:
        schemaMd += "["+schemaTree[domain][schema]['name']+"]"+"("+schemaTree[domain][schema]['url']+")<br>"
    md = md.replace("${"+domain+"}",schemaMd)
with open('../README.md',"w+") as out:
    out.write(md)