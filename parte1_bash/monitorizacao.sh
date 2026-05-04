#!/bin/bash

echo "=== Monitorização Condições Ambientais ==="

mkdir -p outputs

data=$(date)

cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
mem=$(free -m | awk '/Mem:/ {print $3}')

echo "Data: $data" >> outputs/logs.txt
echo "CPU: $cpu%" >> outputs/logs.txt
echo "Memória: ${mem}MB" >> outputs/logs.txt

# Simulação alerta de risco 
if [ $mem -gt 1000 ]; then
    echo "⚠️ Alerta: condições potencialmente críticas para monitorização!" >> outputs/logs.txt
fi

echo "-------------------------" >> outputs/logs.txt
