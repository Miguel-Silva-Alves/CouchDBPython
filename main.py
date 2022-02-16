import couchdb


class MyCouchDB():
    
    def __init__(self, login, password) -> None:
        self.couchserver = couchdb.Server("http://%s:%s@127.0.0.1:5984/" % (login, password))
    
    def getDatabases(self):
        lista = []
        for dbname in self.couchserver:
            lista.append(dbname)
        return lista
    
    def createDatabase(self, name):
        if name not in self.couchserver:
            self.couchserver.create(name)
        return self.couchserver[name]
        

user = "admin"
password = "996057295"
couch = MyCouchDB(user, password)
print(couch.getDatabases())
db = couch.createDatabase('test1')
# doc_id, doc_rev = db.save({'chave1': 'miguel'})
# print(doc_id, doc_rev)

count = 0
for docid in db.view('_all_docs'):
    i = docid['id']
    print(i)

# docs = [{'key': 'value1'}, {'key': 'value2'}]
# for (success, doc_id, revision_or_exception) in db.update(docs):
#     print(success, doc_id, revision_or_exception)






# db = couch.create('test1')
# db = couch['mydb']
# doc = {'foo': 'bar'}
# db.save(doc)
# print(doc)