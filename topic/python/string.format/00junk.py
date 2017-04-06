def testing(one=1,two=2,**kwargs):
  print one
  print two
  print kwargs
  print 'dd' in kwargs
  print 'aa' in kwargs

testing(1,2,cc='33',aa='1',bb='22',)
