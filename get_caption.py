
import os
import pickle

def run(path):
  os.system("python "+os.path.dirname(os.path.realpath(__file__))+"/caption.py "+path)
  dbfile = open(os.path.dirname(os.path.realpath(__file__))+'/temp.pickle', 'rb')      
  db = pickle.load(dbfile) 
  dbfile.close() 
  os.remove(os.path.dirname(os.path.realpath(__file__))+"/temp.pickle")
  return db
  
if __name__=="__main__":
  print(run('/home/aditya/Im2txt-20200726T055020Z-001/Im2txt/CAPTION/download.jpeg'))
