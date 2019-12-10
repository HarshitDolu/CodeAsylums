from google.colab import drive
from google.colab import files
files.upload()
drive.mount('/content/drive')
def eval(dict1):
  s=""
  if type(dict1['lhs'])==dict:
    t=eval(dict1['lhs'])
    s=s+' '+t
  else:
      t=str(dict1['lhs'])
      s=s+''+t

  s=s+''+dict1['op']

  if type(dict1['rhs'])==dict:
      t=eval(dict1['rhs'])
      s=s+' '+t
  else:
      t=str(dict1['rhs'])
      s=s+''+t
  return s

file=open('/content/drive/My Drive/Colab Notebooks/data.txt',"r")
data=json.load(file)
print(eval(data))
