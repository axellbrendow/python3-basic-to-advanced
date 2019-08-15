ls | where { $_.Name -match ".*?-aula\d" } | foreach { Rename-Item $_.Name -NewName ($_.Name -replace "aula0", "aula") }
