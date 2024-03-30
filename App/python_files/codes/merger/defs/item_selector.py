import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
def item_selector(thisPath,thisCase):
  os.chdir(thisPath)
  print(" ")
  for item in thisCase:
      print(_make_farsi_text(item))
  print()
  selected = input(_make_farsi_text(" : لطفاً عدد متناظر با درخواست خود را انتخاب فرمایید "))
  prtLines(2)
  return selected
#   if isinstance(selected,int):
