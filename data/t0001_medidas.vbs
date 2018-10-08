'comment
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
session.findById("wnd[0]/usr/ctxtQMART-LOW").text = "zr"
session.findById("wnd[0]/usr/ctxtIWERK-LOW").text = "2160"
session.findById("wnd[0]/usr/chkDY_QMSM").selected = false
session.findById("wnd[0]/usr/ctxtVARIANT").text = "/PMEDIDAS"
session.findById("wnd[0]/usr/btn%_QMNUM_%_APP_%-VALU_PUSH").press
session.findById("wnd[1]/tbar[0]/btn[23]").press
session.findById("wnd[2]/usr/ctxtDY_PATH").text = "#PATH#"
session.findById("wnd[2]").sendVKey 0
session.findById("wnd[2]/usr/ctxtDY_FILENAME").text = "#FILEINPUT#"
session.findById("wnd[2]").sendVKey 0
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/mbar/menu[0]/menu[11]/menu[2]").select
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxtDY_PATH").text = "#PATH#"
session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "#FILEOUTPUT#"
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/tbar[0]/btn[12]").press
session.findById("wnd[0]/tbar[0]/btn[12]").press
