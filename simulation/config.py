"""
A "request" is one HTTP request made by a virtual user. This operation is what 
causes memory usage to increase - when a "user" makes a request it will trigger a function that
artificially consumes a bunch of memory. These settings control various aspects of how 
requests are made and what their behavior is.
"""

# Number of threads to use for concurrent "user traffic"
TRAFFIC_THREADS=3

# Minimum and maximum amounts of memory in MB to be allocated per request
MEMORY_MB_MIN=10
MEMORY_MB_MAX=20

# Minimum and maximum time in seconds for which memory will be explicitly allocated
# Expiration of this time does not guarantee the memory will be completely freed, but it will
# no longer be used by the process
MEMORY_TIME_MIN=5
MEMORY_TIME_MAX=10

# Minimum and maximum time in seconds between requests in each thread
MIN_REQ_DELAY=3
MAX_REQ_DELAY=6

# List of state names for use in the user context randomization
# There's probably a better place for this
STATE_NAMES = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
