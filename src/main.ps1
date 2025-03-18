# Este script muestra los 19 programas y permite ejecutarlos
$rutaSrc = ".\src\"
$archivos = Get-ChildItem -Path $rutaSrc -Filter *.exe, *.py, *.js

Write-Host "Programas disponibles:"
for ($i = 0; $i -lt $archivos.Count; $i++) {
    Write-Host "$($i + 1). $($archivos[$i].Name)"
}

$opcion = Read-Host "Elige el número del programa que quieres ejecutar"
if ($opcion -match '^\d+$' -and $opcion -le $archivos.Count) {
    Start-Process $archivos[$opcion - 1].FullName
} else {
    Write-Host "Opción no válida."
}
