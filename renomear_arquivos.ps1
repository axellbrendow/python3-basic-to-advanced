ls | where { $_ -match ".*?-aula\d" } | foreach {
    mv $_ ($_ -replace "aula0", "aula")
}
