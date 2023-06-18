def biss (a):
  if a%4!=0:
    print(a,"n'est pas bissextile")

  else:
    if a%100==0 and a%400!=0:
      print(a,"n'est pas bissextile")
    else:
      print(a,"est bissextile")
