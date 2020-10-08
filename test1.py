import urllib.request

A=urllib.request.urlopen("https://sites.google.com/d/1z8aoD3p8ad-qtxzlIsjaAG-gNcu2WM6O/p/1Vbu7B7VdaQ2u969Jf5cwEozT-GuUaQkQ/edit")
data = A.read()

print(data)