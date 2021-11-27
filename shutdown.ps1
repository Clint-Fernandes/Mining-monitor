Start-Sleep -Seconds 3
#Test-Connection "10.200.200.99"

if(Test-Connection "10.200.200.999" -Count 1 -TimeToLive 135) {
   Write-Output "hello"
} else {
    Write-Output "bye"
}