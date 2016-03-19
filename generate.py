from easyprocess import EasyProcess
query = '''BASE <http://example.org/> PREFIX rqg-ite: <http://w3id.org/sparql-generate/ite/> PREFIX rqg-fn: <http://w3id.org/sparql-generate/fn/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> GENERATE { [] rdfs:label ?body . } SOURCE <http://www.pdfconvertonline.com/htm-to-jpg-online.html> AS ?source ITERATOR rqg-ite:CSSPath(?source, "title") AS ?body WHERE { BIND(rqg-fn:HTMLTag(?body, "title") AS ?title ) }'''
query = query.replace("\"","\\\"")
command = "java -jar g.jar -qs \""+query+"\""
command_results = EasyProcess(command).call().stdout
print command_results.split("RDF Output:")[1]
