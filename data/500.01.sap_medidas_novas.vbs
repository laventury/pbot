If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If
session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").text = "iw67"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/chkDY_QMSM").selected = false
session.findById("wnd[0]/usr/ctxtQMART-LOW").text = "zr"
session.findById("wnd[0]/usr/ctxtDATUV").text = "01.10.2018"
session.findById("wnd[0]/usr/ctxtDATUB").text = "04.10.2018"
session.findById("wnd[0]/usr/ctxtIWERK-LOW").text = "2160"
session.findById("wnd[0]/usr/ctxtVARIANT").text = "/PMEDIDAS"
session.findById("wnd[0]/usr/ctxtVARIANT").setFocus
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/mbar/menu[0]/menu[11]/menu[2]").select
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxtDY_PATH").text = "C:\Users\wu3y\Documents\PBOT"
session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "MEDIDASNOVAS.txt"
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/tbar[0]/btn[12]").press
session.findById("wnd[0]/tbar[0]/btn[12]").press
