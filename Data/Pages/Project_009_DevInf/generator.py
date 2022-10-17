#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

dpistep = 1
widthstep = 1
aspectstep = 2

with open(sys.path[0]+"/index.html", "wt")as f:

    f.write("<style>\n")
    for i in range(100, 500, dpistep):
        f.write("@media (max-resolution: "+str(i-1) +
                "dpi) {#dpi"+str(i)+"{display:none;}}\n")
        f.write("@media (min-resolution: "+str(i+dpistep) +
                "dpi) {#dpi"+str(i)+"{display:none;}}\n")
    for i in range(100, 3000, widthstep):
        f.write("@media (max-width: "+str(i-1) +
                "px) {#width"+str(i)+"{display:none;}}\n")
        f.write("@media (min-width: "+str(i+widthstep) +
                "px) {#width"+str(i)+"{display:none;}}\n")
    for i in range(100, 400, aspectstep):
        f.write("@media (max-aspect-ratio: "+str(i-1) +
                " / 200) {#aspect"+str(i)+"{display:none;}}\n")
        f.write("@media (min-aspect-ratio: "+str(i+widthstep) +
                " / 200) {#aspect"+str(i)+"{display:none;}}\n")
    f.write("</style>\n")
    f.write("<body>\n")
    for i in range(100, 500, dpistep):
        f.write("<div id='dpi"+str(i)+"'>Resolution: "+str(i)+"dpi</div>\n")
    for i in range(100, 3000, widthstep):
        f.write("<div id='width"+str(i)+"'>Width: "+str(i)+"px</div>\n")
    for i in range(100, 400, aspectstep):
        f.write("<div id='aspect"+str(i) +
                "'>Aspect ratio: "+str(i)+" / 200</div>\n")
    f.write("</body>\n")
    f.write("""<script type="text/javascript">
    document.write("<div>User agent: " + navigator.userAgent + "</div>");
    document.write("<div>App name: " + navigator.appName + "</div>");
    document.write("<div>App code name: " + navigator.appCodeName + "</div>");
    document.write("<div>App version: " + navigator.appVersion + "</div>");
    document.write("<div>App minor version: " + navigator.appMinorVersion + "</div>");
    document.write("<div>Platform: " + navigator.platform + "</div>");
    document.write("<div>Cookie enabled: " + navigator.cookieEnabled + "</div>");
    document.write("<div>Online: " + navigator.onLine + "</div>");
    document.write("<div>User language: " + navigator.language + "</div>");
    </script>""")
