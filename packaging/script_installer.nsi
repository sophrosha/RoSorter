Unicode true
!include "MUI2.nsh"

!define PROJECT_ROOT ".."

Name "RoSorter"
OutFile "RoSorter-Installer.exe"
InstallDir "$APPDATA\RoSorter"
RequestExecutionLevel user

!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

!insertmacro MUI_PAGE_LICENSE "${PROJECT_ROOT}\LICENSE"

!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "Russian"

Function .onInit
  !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd

Section "Install"
  SetOutPath "$INSTDIR"

  File /r "${PROJECT_ROOT}\dist\RoSorter\*.*"

  CreateDirectory "$SMPROGRAMS\RoSorter"
  CreateShortCut "$SMPROGRAMS\RoSorter\RoSorter.lnk" "$INSTDIR\RoSorter.exe"
  CreateShortCut "$DESKTOP\RoSorter.lnk" "$INSTDIR\RoSorter.exe"

  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\RoSorter" "DisplayName" "RoSorter"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\RoSorter" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\RoSorter" "InstallLocation" "$INSTDIR"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\RoSorter" "DisplayIcon" "$INSTDIR\RoSorter.exe"

  WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

Section "Uninstall"
  RMDir /r "$INSTDIR"
  Delete "$SMPROGRAMS\RoSorter\RoSorter.lnk"
  RMDir "$SMPROGRAMS\RoSorter"
  Delete "$DESKTOP\RoSorter.lnk"
  DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\RoSorter"
  DeleteRegKey HKCU "Software\RoSorter"
SectionEnd