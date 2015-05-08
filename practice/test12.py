# encoding:utf-8

rfd=open("F:\\resultlog\\resultlog.txt",'r')
wfd=file("F:\\resultlog\\resultlog11.txt",'w')
h={}
for i in rfd:

    if not h.has_key(i):
        h[i]=2
        wfd.write(i)