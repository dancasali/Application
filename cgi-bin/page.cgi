#!/bin/bash
echo "Content-Type: text/html"
echo ""
echo "<center>"
echo "<h1>"
echo "Running application on OpenShift on Power Servers on premises and proprietary x86 kubernetes concurrently" 
echo "The PVCs for the application are on a single namespace replicated across multiple clouds"
echo "Replication is controlled on the Perstistent Volume layer using RWX feature"
echo "</h1>"
echo "<h1>"
echo "Today is $(date)"
echo "</h1>"
echo "<h1>"
echo "$(uname -a)"
echo "</h1>"
echo "<h1>"
echo SERVER_SOFTWARE = $SERVER_SOFTWARE
echo "</h1>"
echo "</center>"
