import datetime
import hashlib

def compute_reset_token(val):
    # Create a specific datetime object for June 17, 1999 at exactly midnight
    specific_time = datetime.datetime(1999, 6, 17, 0, 0, 0)
    
    timestamp = specific_time.second
    to_hash = val + str(timestamp)
    
    resetToken = hashlib.sha1(to_hash.encode('utf-8')).hexdigest()
    return resetToken

val = "admin"
resetToken = compute_reset_token(val)

print(resetToken)
