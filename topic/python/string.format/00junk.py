def demo(*args):
  print "\n".join(str(vxx) for vxx in (['asdf'] + list(args)))

demo(*[1,2,3])
