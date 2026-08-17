# IP_LOOKUP_TOOL
IP Lookup Tool — A simple command-line utility that queries the ip-api.com API to retrieve geolocation details (country, city, region, timezone) for a given IP address. Built with a basic menu loop for repeated lookups, useful for quick network reconnaissance or troubleshooting during authorized testing.

What it does:
The script is a simple command-line Python program that takes an IP address as input and sends a request to the ip-api.com API to retrieve geolocation information about it — country, city, region, and timezone. It wraps this in a menu loop so a user can run multiple lookups in one session without restarting the script, and it includes basic error handling to catch invalid IPs or failed network requests.

How it works:

Displays a simple menu (lookup or quit)
Takes an IP address as input
Sends a GET request to ip-api.com's free JSON endpoint
Parses the JSON response and prints the relevant fields
Loops back to the menu, or exits cleanly

Purpose:
This kind of tool is commonly used for:

Network troubleshooting — quickly identifying where a connection or server is geographically located
Learning REST APIs — a beginner-friendly, practical example of sending HTTP requests and parsing JSON in Python
Reconnaissance in authorized security testing — geolocation is often an early, passive step in mapping out infrastructure during a sanctioned penetration test or research project (i.e., using only publicly available data, not intrusive scanning)

It's a "read-only," passive tool — it doesn't touch or interact with the target IP directly, just looks up public metadata about it through a third-party API, which is why it's a common, low-risk starting point for people learning basic security or networking tooling.
