import ibm_db

def get_db_connection():
    conn_str = "DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLCertificate=DigiCertGlobalRootCA.crt;UID=pqb97761;PWD=s4o29lM0qlwVpAuz"
    conn = ibm_db.connect(conn_str, '', '')
    return conn

def fetch_skill_listings():
    conn = get_db_connection()
    stmt = ibm_db.exec_immediate(conn, "SELECT * FROM CHARGINGSTATIONS")
    result = ibm_db.fetch_assoc(stmt)
    skill_listings = []
    while result:
        skill_listings.append(result)
        result = ibm_db.fetch_assoc(stmt)
    ibm_db.close(conn)
    return skill_listings
