url = input("Please enter your URL: ")

if not url.startswith("www."):
    print("URL doesn't start with 'www.'.")
elif "." not in url:
    print("URL must contain at least one dot ('.').")
elif not url.endswith((".com", ".ir", ".org", ".net")):
    print("URL doesn't end with a valid domain (.com, .ir, .org, .net).")
elif " " in url:
    print("URL contains spaces.")
else:
    print("URL is valid.")
