from ldap3 import Server, Connection, ALL, SUBTREE

# LDAP server details
ldap_server = 'ldap://dc-10.di.fc.ul.pt'
base_dn = 'OU=Funcionarios,DC=di,DC=fc,DC=ul,DC=pt'  # Base DN for your directory

# User credentials to verify
username = 'cvgamboa@di.fc.ul.pt'
password = 'password123!'

# Create a server object
server = Server(ldap_server, get_info=ALL)

# Try to bind with the user's credentials
try:
    conn = Connection(server, user=username, password=password)
    if conn.bind():
        print("Authentication successful!")
        
        # Optionally, search for the user in the directory
        search_filter = f'(userPrincipalName={username})'
        conn.search(search_base=base_dn, search_filter=search_filter, search_scope=SUBTREE, attributes=['cn', 'mail'])
        
        if conn.entries:
            print("User found in directory:")
            for entry in conn.entries:
                print(entry)
        else:
            print("User not found in directory.")
    else:
        print("Authentication failed.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.unbind()