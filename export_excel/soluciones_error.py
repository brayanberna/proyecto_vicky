"""
    #wb2.save('export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx').encode('utf-8')
    #wb2.save('export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx'.encode('utf-8'))
    #wb2.save('export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx'.encode('utf-8'))
    #wb2.save(str('export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx'.encode('utf-8') + '.xlsx'))
    #wb2.save('export_excel/static/files/FORMATO CONTROL NI'+'Ñ'.encode('utf-8')+'O SANO.xlsx')
    #wb2.save(str(export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx).encode('utf-8'))
    #nombre = "export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx".encode('utf-8')
    #wb2.save(str('export_excel/static/files/FORMATO CONTROL NIÑO SANO').encode('utf-8') + '.xlsx')
    #wb2.save('%s.xlsx'%nombre)
    #wb2.save('%s'%nombre)
    #wb2.save(nombre)
    #wb2.save(nombre + '.xlsx')
    #$('#imagePreview').html("<img src='"+e.target.result+"' width='"+180+"' height='"+170+"' class='"+'img-fluid'+"' />");
    #wb2.save(str('export_excel/static/files/FORMATO CONTROL NIÑO SANO').encode('utf-8').xlsx)
    #print("Nombre Archivo 1: ", str(workbook_name).encode('utf-8'))

    #wb2.save('export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx').decode('utf-8')
    #wb2.save('export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx'.decode('utf-8'))
    #nombre = "export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx".encode("ASCII", "UTF-8")
    #nombre = "export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx".decode('utf8')
    #nombre = export_excel/static/files/FORMATO CONTROL NIÑO SANO.xlsx.decode('utf-8')
    #wb2.save('%s'%nombre)
    
heroku run "locale -a"
-----------------------------------------------------------------------------------------
heroku buildpacks:add heroku-community/locale
------------------------------------------------------------------------------------------
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-locale
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
--------------------------------------------------------------------------
# -*- coding: utf-8 -*-
import sys
sys.getfilesystemencoding()
from django.utils.translation import ugettext_lazy as _ 
--------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from pathlib import Path
import os

MEDIA_ROOT = os.path.join('D:', u' INVESTIGACIÓN_P')
--------------------------------------------------------------------------
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
-+------------------------------------------------------------------------
.encode('utf-8', 'ignore').decode('utf-8')
.encode('ascii','ignore').decode()
--------------------------------------------------------------------------
# encoding=utf8
import sys
--------------------------------------------------------------------------
.decode('ascii', 'ignore')
--------------------------------------------------------------------------
.encode('utf-8')
--------------------------------------------------------------------------
print("Nombre Archivo 1: ", guargar_excel.encode('ascii','ignore').decode())
--------------------------------------------------------------------------
def index(request, encoding='utf-8'):

  .encode('utf-8')
--------------------------------------------------------------------------
    #response = HttpResponse(content_type='application/vnd.ms-excel')
    #response = HttpResponse(content_type='application/vnd.xls')
    #response = HttpResponse(content_type='application/xls')
    #response = HttpResponse(content_type='text/xlsx') 
        
    #response = HttpResponse(content_type='application/vnd.ms-excel')
    #response['Content-Disposition'] = 'attachment; filename="resultadoplop.xlsx"'
    #response.write(wb2)

    #response.content_type = 'application/octet-stream;'
    #response.set_header('Content-Disposition', 'attachment; filename=myexport.xlsx')
    
    #response = HttpResponse(content=save_virtual_workbook(wb2), mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    #response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
    #     #response.body = save_virtual_workbook(wb2)"""